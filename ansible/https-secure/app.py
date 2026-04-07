from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
import datetime

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


# create db automatically
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users (id, username, password) VALUES (1,'admin','admin123')"
    )

    cursor.execute(
        "INSERT OR IGNORE INTO users (id, username, password) VALUES (2,'user','1234')"
    )

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


# SECURE LOGIN
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        return redirect(url_for("home"))
    else:
        return "Invalid login"


# SECURE PAYMENT
@app.route("/pay", methods=["POST"])
def pay():

    courses = request.form.getlist("course")
    total = sum(int(c) for c in courses)

    txn = random.randint(100000,999999)
    time = datetime.datetime.now()

    return redirect(
        url_for(
            "attack",
            status="blocked",
            total=total,
            card="ENCRYPTED",
            txn=txn,
            time=time
        )
    )


@app.route("/attack")
def attack():
    status = request.args.get("status")
    total = request.args.get("total")
    card = request.args.get("card")
    txn = request.args.get("txn")
    time = request.args.get("time")

    return render_template(
        "attack.html",
        status=status,
        total=total,
        card=card,
        txn=txn,
        time=time
    )


@app.route("/about")
def about():
    return """
    <h1>HTTP vs HTTPS Security Demo</h1>

    <h3>HTTP Risks</h3>
    <ul>
    <li>No encryption</li>
    <li>SQL injection possible</li>
    <li>Cart tampering possible</li>
    <li>MITM attack possible</li>
    </ul>

    <h3>HTTPS Protection</h3>
    <ul>
    <li>Encrypted communication</li>
    <li>Secure authentication</li>
    <li>Server-side validation</li>
    <li>Tampering prevention</li>
    </ul>
    """


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)