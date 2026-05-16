async function sendMessage() {

    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    // User message
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    // Auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    // Bot message
    chatBox.innerHTML += `
        <div class="bot-message">
            ${data.response}
        </div>
    `;

    // Auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}


function clearChat() {

    document.getElementById("chat-box").innerHTML = `
        <div class="bot-message">
            🤖 Welcome to NIELIT Admission Assistant!
        </div>
    `;
}


function toggleTheme() {
    document.body.classList.toggle("dark-mode");
}


// Enter key support
document
.getElementById("user-input")
.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }
});