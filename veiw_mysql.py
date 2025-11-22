import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pinky@143",
    database="version_system"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM version_history")

for row in cursor.fetchall():
    print(row)
