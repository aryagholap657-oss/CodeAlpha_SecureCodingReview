import sqlite3
import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password
password_hash = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table for secure example
cursor.execute("""
CREATE TABLE IF NOT EXISTS secure_users (
    username TEXT,
    password TEXT
)
""")

# Add demo user with hashed password if table is empty
cursor.execute("SELECT COUNT(*) FROM secure_users")
if cursor.fetchone()[0] == 0:
    cursor.execute(
        "INSERT INTO secure_users (username, password) VALUES (?, ?)",
        ("test", hashlib.sha256("test".encode()).hexdigest())
    )
    conn.commit()

# Secure: parameterized query prevents SQL injection
query = "SELECT * FROM secure_users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password_hash))
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()