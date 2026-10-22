from flask import Flask
import os
import psycopg2
import time

app = Flask(__name__)

@app.route('/health')
def health():
    # Пытаемся подключиться к БД, которую поднимет compose
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        return "DATABASE_URL not set", 500
    try:
        conn = psycopg2.connect(db_url)
        conn.close()
        return "OK: Connected to database", 200
    except Exception as e:
        return f"DB connection failed: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
