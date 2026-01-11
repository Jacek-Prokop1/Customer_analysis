from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import Users
from werkzeug.security import check_password_hash

login_bp = Blueprint("login", __name__, template_folder="templates")

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    errors = {}
    email = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email:
            errors["email"] = "Email jest wymagany."
        if not password:
            errors["password"] = "Hasło jest wymagane."

        if email and password:
            user = Users.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                flash("Zalogowano pomyślnie!", "success")
                session["user"] = user.email
                return redirect(url_for("dashboard.dashboard_panel"))
            else:
                errors["form"] = "Nieprawidłowy email lub hasło."

    return render_template("login.html", errors=errors, email=email)