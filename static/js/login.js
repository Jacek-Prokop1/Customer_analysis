document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    document.getElementById("emailError").textContent = "";
    document.getElementById("passwordError").textContent = "";
    document.getElementById("formError").textContent = "";

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert("Zalogowano pomyślnie (symulacja)");
        } else {
            if (data.errors.email) {
                document.getElementById("emailError").textContent = data.errors.email;
            }
            if (data.errors.password) {
                document.getElementById("passwordError").textContent = data.errors.password;
            }
            document.getElementById("formError").textContent = "Błąd logowania";
        }
    });
});