from flask import Flask
import os
import pyodbc

app = Flask(__name__)


def get_db_connection():
    conn_str = os.environ.get('CUSTOMCONNSTR_DB_CONNECTION_STRING')
    conn = pyodbc.connect(conn_str)
    return conn

@app.route('/')
def index():
    tasks_html = "<h1>Witaj!Aplikacja wdrożona przez GitHub Actions!</h1><ul>"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Title FROM Tasks")
        rows = cursor.fetchall()
        for row in rows:
            tasks_html += f"<li>{row.Title}</li>"
        conn.close()
    except Exception as e:
        tasks_html += f"<li>Blad polaczenia z baza: {str(e)}</li>"

    tasks_html += "</ul>"
    return tasks_html
