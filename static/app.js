function uploadPDF() {
    var fileInput = document.getElementById('pdf-upload');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('pdf', file);

    fetch('/upload_pdf', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
    });
}

function sendMessage() {
    var input = document.getElementById("user-input");
    var message = input.value;

    // Use AJAX to send message to server and get response
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'message': message
        })
    })
    .then(response => response.json())
    .then(data => {
        var chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += '<p><span class=".user-label"><b>You</b>:</span> ' + message + '</p>';
        chatBox.innerHTML += '<p><span class=".bot-label"><b>Bot</b>:</span> ' + data.answer + '</p>';
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom to see the latest message
    });

    input.value = ""; // Clear the input field
}

document.getElementById('pdf-upload').addEventListener('change', function(e) {
    var fileName = e.target.value.split('\\').pop();
    document.getElementById('selected-filename').textContent = fileName || "No file selected.";
});
