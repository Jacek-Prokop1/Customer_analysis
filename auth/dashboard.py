from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Users
from werkzeug.security import generate_password_hash

dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")

@dashboard_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    user_email = session.get("user")
    if not user_email:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        role = request.form.get("role", 0)

        if not email or not password or not confirm_password:
            flash("Wszystkie pola są wymagane.", "error")
            return redirect(url_for("dashboard.dashboard"))

        if password != confirm_password:
            flash("Hasła się nie zgadzają.", "error")
            return redirect(url_for("dashboard.dashboard"))

        if Users.query.filter_by(email=email).first():
            flash("Użytkownik z tym emailem już istnieje.", "error")
            return redirect(url_for("dashboard.dashboard"))

        hashed_password = generate_password_hash(password)
        new_user = Users(email=email, password=hashed_password, role=int(role))
        db.session.add(new_user)
        db.session.commit()

        flash("Rejestracja zakończona sukcesem!", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template("dashboard.html", user=user_email)