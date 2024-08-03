document.addEventListener('DOMContentLoaded', function() {
    const chatBox = document.getElementById('chat-box');
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message');

    function fetchMessages() {
        fetch('/chat')
            .then(response => response.json())
            .then(data => {
                chatBox.innerHTML = data.chat.split('\n').map(line => `<div>${line}</div>`).join('');
                chatBox.scrollTop = chatBox.scrollHeight;
            });
    }

    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const message = messageInput.value;
        if (message.trim()) {
            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({ 'message': message })
            })
            .then(response => response.json())
            .then(() => {
                messageInput.value = '';
                fetchMessages();
            });
        }
    });

    fetchMessages();
});
