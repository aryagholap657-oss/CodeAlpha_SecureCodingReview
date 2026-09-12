import sqlite3
import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password before using it
password_hash = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Parameterized query prevents SQL injection
query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password_hash))

result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()