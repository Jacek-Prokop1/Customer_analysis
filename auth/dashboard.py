from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Users, Clients
from werkzeug.security import generate_password_hash

dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard_panel():
    user_email = session.get("user")
    if not user_email:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    return render_template("dashboard.html", user=user_email)

@dashboard_bp.route("/dashboard/register_user", methods=["POST"])
def register_user():
    user_email = session.get("user")
    if not user_email:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")
    role = request.form.get("role", 0)

    if not email or not password or not confirm_password:
        flash("Wszystkie pola są wymagane.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    if password != confirm_password:
        flash("Hasła się nie zgadzają.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    if Users.query.filter_by(email=email).first():
        flash("Użytkownik z tym emailem już istnieje.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    hashed_password = generate_password_hash(password)
    new_user = Users(email=email, password=hashed_password, role=int(role))
    db.session.add(new_user)
    db.session.commit()

    flash("Rejestracja zakończona sukcesem!", "success")
    return redirect(url_for("dashboard.dashboard_panel"))

@dashboard_bp.route("/dashboard/add_client", methods=["POST"])
def add_client():
    user_email = session.get("user")
    if not user_email:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    email = request.form.get("email", "").strip()
    client_tenure = request.form.get("client_tenure", 0)

    if not first_name or not last_name or not email or not client_tenure:
        flash("Wszystkie pola są wymagane.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    if Clients.query.filter_by(email=email).first():
        flash("Klient z tym emailem już istnieje.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    new_client = Clients(
        first_name=first_name,
        last_name=last_name,
        email=email,
        client_tenure=int(client_tenure)
    )
    db.session.add(new_client)
    db.session.commit()

    flash("Klient został dodany pomyślnie!", "success")
    return redirect(url_for("dashboard.dashboard_panel"))