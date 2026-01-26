document.addEventListener('DOMContentLoaded', () => {
    // Future Notification Interactivity (e.g. real-time updates via WebSocket or long-polling)
    console.log("Notification system initialized. 📬");

    // Smooth entry for cards
    const cards = document.querySelectorAll('.notif-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = '0.5s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});
