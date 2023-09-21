document.addEventListener("DOMContentLoaded", function () {
    const getStartedButton = document.getElementById("getStartedButton");
    const nameInput = document.getElementById("nameInput");

    getStartedButton.addEventListener("click", function (e) {
        e.preventDefault();

        const userName = nameInput.value.trim();

        if (!userName) {
            alert("Please enter your name.");
            return;
        }

        const welcomeMessage = `Welcome, ${userName}! Let's get started.`;
        alert(welcomeMessage);
    });
});
document.addEventListener("DOMContentLoaded", function () {
    // Load the login page using AJAX and insert it into the login-container div
    const loginContainer = document.getElementById("login-container");

    // Define the URL of the login.html file
    const loginPageURL = "login.html";

    // Create a new XMLHttpRequest object
    const xhr = new XMLHttpRequest();

    // Define a callback function to handle the response
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Insert the response HTML into the login-container div
            loginContainer.innerHTML = xhr.responseText;
        }
    };

    // Open and send the GET request to fetch the login page content
    xhr.open("GET", loginPageURL, true);
    xhr.send();
});

