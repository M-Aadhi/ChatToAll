document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message');

    function fetchMessages() {
        fetch('/chatlog')
            .then(response => response.json())
            .then(data => {
                const chatLogElement = document.getElementById('chat-log');
                chatLogElement.innerHTML = data.chat.join('<br>');
            })
            .catch(error => console.error(error));
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
            })
            .catch(error => console.error(error));
        }
    });

    fetchMessages();
});