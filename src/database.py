import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('finance.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')

    conn.commit()

    conn.close()

    print ("Database initialized")

def getDBConnection():
    conn = sqlite3.connect('finance.db')
    conn.row_factory = sqlite3()
    return conn

if __name__ == '__main__':
        init_db()