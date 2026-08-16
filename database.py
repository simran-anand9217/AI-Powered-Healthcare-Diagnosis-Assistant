import sqlite3
from datetime import datetime

DB_NAME = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            age INTEGER,
            gender TEXT,
            primary_disease TEXT,
            probability REAL,
            risk_level TEXT,
            specialist TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_prediction(age, gender, disease, probability, risk_level, specialist):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO predictions (timestamp, age, gender, primary_disease, probability, risk_level, specialist)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), age, gender, disease, probability, risk_level, specialist))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp, age, gender, primary_disease, probability, risk_level, specialist FROM predictions ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows