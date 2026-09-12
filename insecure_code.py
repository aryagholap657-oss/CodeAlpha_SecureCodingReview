import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table for insecure example
cursor.execute("""
CREATE TABLE IF NOT EXISTS insecure_users (
    username TEXT,
    password TEXT
)
""")

# Add demo user if table is empty
cursor.execute("SELECT COUNT(*) FROM insecure_users")
if cursor.fetchone()[0] == 0:
    cursor.execute(
        "INSERT INTO insecure_users (username, password) VALUES (?, ?)",
        ("test", "test")
    )
    conn.commit()

# Insecure: user input is directly combined with SQL query
query = "SELECT * FROM insecure_users WHERE username = '" + username + "' AND password = '" + password + "'"

cursor.execute(query)
result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()