fetch("http://localhost:5000/api/message")
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    })
    .catch(err => {
        document.getElementById("message").innerText = "Erreur : impossible de contacter le backend";
    });