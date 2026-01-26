document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const container = document.getElementById('msg-container');

    if (!container) return;

    // Auto-scroll to bottom
    container.scrollTop = container.scrollHeight;

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
                msgDiv.innerHTML = `${data.content}<span class="msg-time">${data.timestamp}</span>`;
                container.appendChild(msgDiv);
                container.scrollTop = container.scrollHeight;
            }
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
