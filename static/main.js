document.querySelector('button').addEventListener('click', async function() {
    const inputElement = document.querySelector('input');
    const message = inputElement.value;

    if (message.trim() === '') return;  // Do nothing if the input is empty

    displayMessage(message, 'user');

    const response = await sendMessageToBackend(message);
    displayMessage(response, 'bot');

    inputElement.value = '';  // Clear the input
});

function displayMessage(message, sender) {
    const messagesContainer = document.querySelector('.chat-messages');
    const messageElement = document.createElement('div');
    messageElement.className = sender;
    messageElement.textContent = message;
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;  // Scroll to the bottom
}

async function sendMessageToBackend(message) {
    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    return data.response;
}
