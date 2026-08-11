"""
Professional Xbox Contract System (starter template)

Features:
- Flask web app
- SQLite storage
- Typed signature
- Drawn signature (base64 canvas)
- Submission timestamps
- PDF generation
- Admin dashboard
- Payhip Order ID field
- Email placeholders

Install:
pip install flask reportlab

Run:
python app.py
"""
from flask import Flask, render_template, request, redirect
import sqlite3, datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("contracts.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS contracts(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      order_id TEXT,
      full_name TEXT,
      email TEXT,
      phone TEXT,
      gamertag TEXT,
      typed_signature TEXT,
      drawn_signature TEXT,
      submitted_at TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET","POST"])
def contract():
    if request.method == "POST":
        conn = sqlite3.connect("contracts.db")
        conn.execute(
            "INSERT INTO contracts(order_id,full_name,email,phone,gamertag,typed_signature,drawn_signature,submitted_at) VALUES (?,?,?,?,?,?,?,?)",
            (
                request.form.get("order_id"),
                request.form.get("full_name"),
                request.form.get("email"),
                request.form.get("phone"),
                request.form.get("gamertag"),
                request.form.get("typed_signature"),
                request.form.get("signature_data"),
                datetime.datetime.utcnow().isoformat()
            )
        )
        conn.commit()
        conn.close()
        return redirect("/admin")
    return render_template("contract.html")

@app.route("/admin")
def admin():
    conn = sqlite3.connect("contracts.db")
    rows = conn.execute("SELECT * FROM contracts ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("admin.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
