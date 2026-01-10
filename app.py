from flask import Flask, redirect, url_for
from models import db, Users
from auth.login import login_bp
from auth.dashboard import dashboard_bp
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "tajny_klucz"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)

with app.app_context():
    db.create_all()
    if not Users.query.filter_by(email="test@example.com").first():
        user = Users(email="test@example.com", password=generate_password_hash("haslo123"), role=0)
        db.session.add(user)
        db.session.commit()

@app.route("/")
def index():
    return redirect(url_for("login.login"))

if __name__ == "__main__":
    app.run(debug=True)