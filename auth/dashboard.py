from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Users, Clients, Client_activity
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

@dashboard_bp.route("/dashboard/add_client_activity", methods=["POST"])
def add_client_activity():
    email_customer = request.form.get("email_customer", "").strip()
    numbers_visits = request.form.get("numbers_visits", "").strip()
    numbers_purchases = request.form.get("numbers_purchases", "").strip()
    average_basket_value = request.form.get("average_basket_value", "").strip()
    numbers_purchases_day = request.form.get("numbers_purchases_day", "").strip()

    if not email_customer or not numbers_visits or not numbers_purchases or not average_basket_value or not numbers_purchases_day:
        flash("Wszystkie pola są wymagane.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    try:
        numbers_visits = int(numbers_visits)
        numbers_purchases = int(numbers_purchases)
        average_basket_value = float(average_basket_value)
        numbers_purchases_day = int(numbers_purchases_day)
    except ValueError:
        flash("Niepoprawne dane liczbowe.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    client = Clients.query.filter_by(email=email_customer).first()
    if not client:
        flash("Nie ma takiego klienta.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    client_activity = Client_activity.query.filter_by(client_id=client.id).first()
    sales_value = numbers_purchases * average_basket_value
    high_purchase = 1 if numbers_purchases > 0 else 0

    if client_activity:
        client_activity.numbers_visits = numbers_visits
        client_activity.numbers_purchases = numbers_purchases
        client_activity.average_basket_value = average_basket_value
        client_activity.numbers_purchases_day = numbers_purchases_day
        client_activity.sales_value = sales_value
        client_activity.high_purchase = high_purchase
    else:
        client_activity = Client_activity(
            client_id=client.id,
            numbers_visits=numbers_visits,
            numbers_purchases=numbers_purchases,
            average_basket_value=average_basket_value,
            numbers_purchases_day=numbers_purchases_day,
            sales_value=sales_value,
            high_purchase=high_purchase
        )
        db.session.add(client_activity)

    db.session.commit()
    flash("Aktywność klienta została zapisana pomyślnie!", "success")
    return redirect(url_for("dashboard.dashboard_panel"))

@dashboard_bp.route("/dashboard/ml", methods=["GET"])
def dashboard_ml():
    user_email = session.get("user")
    if not user_email:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    ml_stats = {
        "accuracy": 0.92,
        "precision": 0.88,
        "recall": 0.91,
        "f1_score": 0.895
    }
    stats_text = "\n".join(
        [f"{key}: {value}" for key, value in ml_stats.items()]
    )

    return render_template(
        "dashboard.html",
        user=user_email,
        show_ml=True,
        stats_text=stats_text
    )

