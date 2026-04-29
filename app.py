from flask import Flask, jsonify, request, render_template
import psycopg2
import os
import api_caller

API_KEY = "sk-JgGoX7z7SYHhIaxAYc7gkg"
BASE_URL = "https://kurim.ithope.eu/chat/completions"

ollama = api_caller.ollama_api(BASE_URL, API_KEY)

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    return conn

@app.route("/ping")
def ping():
    return "pong"

@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "author": "jan_janicek"
    })

@app.route("/save")
def save():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, msg TEXT);")
    cur.execute("INSERT INTO test (msg) VALUES ('ahoj z databaze');")

    conn.commit()
    cur.close()
    conn.close()

    return "ulozeno"

@app.route("/ai", methods=["POST"])
def ai():
    try:
        data = request.json
        question = data.get("question", "")

        if not question:
            return {"error": "Chybí otázka"}

        answer = ollama.query(question)

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
