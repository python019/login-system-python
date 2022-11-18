import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9998))

server.listen()

def login(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("Password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()


    base = sqlite3.connect("data.db")
    cursor = base.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    if cursor.fetchall():
        c.send("Login successful!".encode())
    else:
        c.send("Login failed!".encode())

while True:
    client, addr = server.accept()
    threading.Thread(target=login, args=(client, )).start()