from flask import Flask, redirect, url_for
from auth import login_bp

app = Flask(__name__)
app.secret_key = "tajny_klucz"

app.register_blueprint(login_bp)

@app.route("/")
def index():
    return redirect(url_for("login.login"))

if __name__ == "__main__":
    app.run(debug=True)