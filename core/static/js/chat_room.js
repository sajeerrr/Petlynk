document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const container = document.getElementById('msg-container');

    if (!container) return;

    let lastMessageId = 0;
    let isPolling = false;

    // Get the last message ID from existing messages
    const existingMessages = container.querySelectorAll('.message');
    if (existingMessages.length > 0) {
        const lastMsg = existingMessages[existingMessages.length - 1];
        lastMessageId = parseInt(lastMsg.dataset.msgId || '0') || 0;
    }

    // Auto-scroll to bottom on page load
    function scrollToBottom() {
        setTimeout(() => {
            container.scrollTop = container.scrollHeight;
        }, 100);
    }

    scrollToBottom();

    // Poll for new messages every 3 seconds
    function pollNewMessages() {
        if (isPolling) return;
        isPolling = true;
        const profileId = input.dataset.profileId;
        const pollUrl = `/get-new-messages/${profileId}/?last_msg_id=${lastMessageId}`;
        fetch(pollUrl).then(res => res.json()).then(data => {
            if (data.status === 'success' && data.messages && data.messages.length > 0) {
                data.messages.forEach(msg => {
                    const msgDiv = document.createElement('div');
                    msgDiv.className = msg.is_mine ? 'message sent' : 'message received';
                    msgDiv.dataset.msgId = msg.id;
                    msgDiv.innerHTML = `${msg.content}<span class="msg-time">${msg.timestamp}</span>`;
                    container.appendChild(msgDiv);
                    lastMessageId = Math.max(lastMessageId, msg.id);
                });
                scrollToBottom();
            }
        }).catch(err => console.error('Polling error:', err)).finally(() => { isPolling = false; });
    }
    setInterval(pollNewMessages, 3000);

    function sendMessage() {
        const text = input.value.trim();
        if (!text) return;

        // Get context from data attributes (cleaner than hardcoding)
        const profileId = input.dataset.profileId;
        const sendUrl = input.dataset.sendUrl;
        const csrfToken = input.dataset.csrf;

        input.value = '';

        fetch(sendUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify({ "content": text })
        }).then(res => res.json()).then(data => {
            if (data.status === "success") {
                const msgDiv = document.createElement('div');
                msgDiv.className = 'message sent';
                msgDiv.dataset.msgId = data.msg_id;
                msgDiv.innerHTML = `${data.content}<span class="msg-time">${data.timestamp}</span>`;
                container.appendChild(msgDiv);
                lastMessageId = Math.max(lastMessageId, data.msg_id);
                scrollToBottom();
            } else {
                console.error('Failed to send message:', data.message);
                alert('Failed to send message: ' + data.message);
            }
        }).catch(err => {
            console.error('Error sending message:', err);
            alert('Error sending message. Please try again.');
        });
    }

    if (sendBtn) {
        sendBtn.onclick = sendMessage;
    }

    if (input) {
        input.onkeypress = (e) => {
            if (e.key === 'Enter') sendMessage();
        };
    }
});
