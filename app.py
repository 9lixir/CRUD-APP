from flask import Flask, render_template, request, redirect, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

def get_db_connection():
    return psycopg2.connect(
        dbname="crud_lab",
        user="postgres",
        password="1207",
        host="localhost",
        port="5432"
    )

# ---------- AUTH ----------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, password FROM users WHERE username=%s",
            (username,)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and check_password_hash(user[1], password):
            session["user_id"] = user[0]
            return redirect("/dashboard")

        return redirect("/login")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- PROTECTED ROUTES ----------

@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items ORDER BY id")
    items = cur.fetchall()
    cur.close()
    conn.close()

    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
def add_item():
    if "user_id" not in session:
        return redirect("/login")

    name = request.form["name"]
    quantity = request.form["quantity"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO items (name, quantity) VALUES (%s, %s)",
        (name, quantity)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update_item(id):
    if "user_id" not in session:
        return redirect("/login")

    name = request.form["name"]
    quantity = request.form["quantity"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET name=%s, quantity=%s WHERE id=%s",
        (name, quantity, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete_item(id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT username FROM users WHERE id=%s",
        (session["user_id"],)
    )
    user = cur.fetchone()
    cur.close()
    conn.close()

    return render_template("dashboard.html", username=user[0])

if __name__ == "__main__":
    app.run(debug=True)
