from flask import render_template, request, redirect, url_for, flash, session
from . import login_bp

USERS = {"test@example.com": "haslo123"}

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    errors = {}
    email = ""

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        if not email:
            errors["email"] = "Email jest wymagany."
        if not password:
            errors["password"] = "Hasło jest wymagane."

        if email and password:
            if USERS.get(email) == password:
                flash("Zalogowano pomyślnie!", "success")
                session["user"] = email
                return redirect(url_for("login.dashboard"))
            else:
                errors["form"] = "Nieprawidłowy email lub hasło."

    return render_template("login.html", errors=errors, email=email)

@login_bp.route("/dashboard")
def dashboard():
    user = session.get("user")

    if not user:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    return f"Witaj w panelu użytkownika, {user}!"