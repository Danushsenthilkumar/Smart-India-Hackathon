document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        // You can add your own validation logic here.
        if (!username || !password) {
            alert("Please fill in both username and password fields.");
            return;
        }

        // If validation passes, you can proceed with further actions, e.g., AJAX login request.
        // For this example, we'll just display an alert with the entered credentials.
        const userType = document.getElementById("user-type").value;
        const message = `Username: ${username}\nPassword: ${password}\nUser Type: ${userType}`;
        alert(message);

        // Optionally, you can reset the form after successful login.
        loginForm.reset();
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();
        const userType = document.getElementById("user-type").value;

        console.log("Username:", username);
        console.log("Password:", password);
        console.log("User Type:", userType);

        // Simulate user authentication (replace with actual authentication logic)
        // For this example, we'll assume 'student' and 'teacher' as valid users
        if (userType === "student" && username === "studentUsername" && password === "studentPassword") {
            // Redirect to student home page (replace 'Student Home.html' with the actual student home page URL)
            window.location.href = "Student Home.html";
        } else if (userType === "teacher" && username === "teacherUsername" && password === "teacherPassword") {
            // Redirect to teacher home page (replace 'teacher-home.html' with the actual teacher home page URL)
            window.location.href = "teacher-home.html";
        } else {
            alert("Invalid username or password.");
        }
    });
});


