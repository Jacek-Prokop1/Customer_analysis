from app import app, db
from models import Users, Clients, Client_activity
from werkzeug.security import generate_password_hash
from datetime import datetime
import random

with app.app_context():
    # 1️⃣ Utwórz wszystkie tabele w bazie
    db.create_all()
    print("Tabele utworzone.")

    # 2️⃣ Dodaj przykładowego użytkownika
    if not Users.query.filter_by(email="test@example.com").first():
        user = Users(
            email="test@example.com",
            password=generate_password_hash("haslo123"),
            role=0  # 0 = Analist
        )
        db.session.add(user)
        print("Dodano użytkownika test@example.com")

    # 3️⃣ Dodaj przykładowego klienta
    client = Clients.query.filter_by(email="testclient@example.com").first()
    if not client:
        client = Clients(
            first_name="Jan",
            last_name="Kowalski",
            email="testclient@example.com",
            client_tenure=3
        )
        db.session.add(client)
        db.session.commit()  # commit żeby klient miał ID
        print("Dodano klienta testclient@example.com")

    # 4️⃣ Dodaj 10 przykładowych aktywności klienta
    for i in range(10):
        numbers_visits = random.randint(1, 10)
        numbers_purchases = random.randint(0, numbers_visits)
        average_basket_value = round(random.uniform(10, 200), 2)
        numbers_purchases_day = random.randint(1, 30)
        sales_value = numbers_purchases * average_basket_value
        high_purchase = 1 if numbers_purchases > 0 else 0

        activity = Client_activity(
            client_id=client.id,
            numbers_visits=numbers_visits,
            numbers_purchases=numbers_purchases,
            average_basket_value=average_basket_value,
            numbers_purchases_day=numbers_purchases_day,
            sales_value=sales_value,
            high_purchase=high_purchase
        )
        db.session.add(activity)

    db.session.commit()
    print("Dodano 10 przykładowych aktywności klienta.")
    print("Baza danych gotowa do testów ML.")