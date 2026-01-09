from . import login_bp
from models import db, Users
from flask import render_template, request, redirect, url_for, flash, session

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
            user = Users.query.filter_by(email=email).first()
            if user and user.password == password:
                flash("Zalogowano pomyślnie!", "success")
                session["user"] = user.email
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