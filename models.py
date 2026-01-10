from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    # 0 = Analist, 1 = Admin
    role = db.Column(db.Integer, nullable=False, default=0)

class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    client_tenure = db.Column(db.Integer, nullable=False, default=0)


class Client_activity(db.Model):
    __tablename__ = "client_activity"
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    numbers_visits = db.Column(db.Integer, nullable=False, default=0)
    numbers_purchases = db.Column(db.Integer, nullable=False, default=0)
    average_basket_value = db.Column(db.Float, nullable=False, default=0.0)
    numbers_purchases_day = db.Column(db.Integer, nullable=False, default=0)
    sales_value = db.Column(db.Float, nullable=True)
    high_purchase = db.Column(db.Integer, nullable=False, default=0)

    client = db.relationship('Clients', backref='activities')


