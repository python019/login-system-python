import sqlite3
import hashlib

base = sqlite3.connect('data.db')

cursor = base.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "subux", hashlib.sha256("subux123".encode()).hexdigest()
username2, password2 = "subui", hashlib.sha256("subui123".encode()).hexdigest()

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username1, password1))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username2, password2))

base.commit()