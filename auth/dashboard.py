from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from models import db, Users, Clients, Client_activity
from ML import sales_forecasting

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates"
)

@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard_panel():
    user_email = session.get("user")
    if not user_email:
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    return render_template(
        "dashboard.html",
        user=user_email,
        y_pred=None
    )

@dashboard_bp.route("/dashboard/register-user", methods=["POST"])
def register_user():
    if not session.get("user"):
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")
    role = request.form.get("role", 0)

    if not email or not password or not confirm_password:
        flash("Wszystkie pola są wymagane.", "error")
    elif password != confirm_password:
        flash("Hasła się nie zgadzają.", "error")
    elif Users.query.filter_by(email=email).first():
        flash("Użytkownik z tym emailem już istnieje.", "error")
    else:
        hashed_password = generate_password_hash(password)
        new_user = Users(
            email=email,
            password=hashed_password,
            role=int(role)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Użytkownik został dodany.", "success")

    return redirect(url_for("dashboard.dashboard_panel"))

@dashboard_bp.route("/dashboard/add-client", methods=["POST"])
def add_client():
    if not session.get("user"):
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    first_name = request.form.get("first_name", "").strip()
    last_name = request.form.get("last_name", "").strip()
    email = request.form.get("email", "").strip()
    client_tenure = request.form.get("client_tenure", 0)

    if not first_name or not last_name or not email:
        flash("Wszystkie pola są wymagane.", "error")
    elif Clients.query.filter_by(email=email).first():
        flash("Klient z tym emailem już istnieje.", "error")
    else:
        new_client = Clients(
            first_name=first_name,
            last_name=last_name,
            email=email,
            client_tenure=int(client_tenure)
        )
        db.session.add(new_client)
        db.session.commit()
        flash("Klient został dodany.", "success")

    return redirect(url_for("dashboard.dashboard_panel"))

@dashboard_bp.route("/dashboard/add-activity", methods=["POST"])
def add_client_activity():
    if not session.get("user"):
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    email_customer = request.form.get("email_customer", "").strip()

    client = Clients.query.filter_by(email=email_customer).first()
    if not client:
        flash("Nie ma takiego klienta.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    try:
        numbers_visits = int(request.form.get("numbers_visits", 0))
        numbers_purchases = int(request.form.get("numbers_purchases", 0))
        average_basket_value = float(request.form.get("average_basket_value", 0))
        numbers_purchases_day = int(request.form.get("numbers_purchases_day", 0))
    except ValueError:
        flash("Niepoprawne dane liczbowe.", "error")
        return redirect(url_for("dashboard.dashboard_panel"))

    sales_value = numbers_purchases * average_basket_value
    high_purchase = 1 if numbers_purchases > 0 else 0

    activity = Client_activity.query.filter_by(client_id=client.id).first()
    if not activity:
        activity = Client_activity(client_id=client.id)
        db.session.add(activity)

    activity.numbers_visits = numbers_visits
    activity.numbers_purchases = numbers_purchases
    activity.average_basket_value = average_basket_value
    activity.numbers_purchases_day = numbers_purchases_day
    activity.sales_value = sales_value
    activity.high_purchase = high_purchase

    db.session.commit()
    flash("Aktywność klienta została zapisana.", "success")

    return redirect(url_for("dashboard.dashboard_panel"))

@dashboard_bp.route("/dashboard/ml", methods=["GET"])
def dashboard_ml():
    if not session.get("user"):
        flash("Musisz się zalogować!", "error")
        return redirect(url_for("login.login"))

    client_email = request.args.get("client_email", "").strip()
    if not client_email:
        flash("Podaj email klienta.", "warning")
        return redirect(url_for("dashboard.dashboard_panel"))

    client = Clients.query.filter_by(email=client_email).first()
    if not client:
        flash("Nie znaleziono klienta o takim emailu.", "warning")
        return redirect(url_for("dashboard.dashboard_panel"))

    y_pred, error = sales_forecasting.train_model_regression(client_id=client.id)

    if error:
        flash(error, "warning")
        y_pred = None

    return render_template(
        "dashboard.html",
        user=session.get("user"),
        y_pred=y_pred
    )