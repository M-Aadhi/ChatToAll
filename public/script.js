document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatInput = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-box");

    const loadChat = async () => {
        const response = await fetch('/ChatToAll/ChatServlet');
        const data = await response.text();
        chatBox.innerHTML = data.replace(/\n/g, '<br>');
        chatBox.scrollTop = chatBox.scrollHeight;
    };

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const message = chatInput.value;
        await fetch('/ChatToAll/ChatServlet', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `message=${encodeURIComponent(message)}`
        });
        chatInput.value = '';
        loadChat();
    });

    loadChat();
    setInterval(loadChat, 5000);
});
