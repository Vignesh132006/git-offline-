import os
import shutil
import mysql.connector
import datetime

base_file = "project_base.txt"

# -------------------- MYSQL SETUP --------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="version_system"
)
cursor = db.cursor()
# -----------------------------------------------------

# create base file if not exists
if not os.path.exists(base_file):
    with open(base_file, "w") as f:
        f.write("This is version 1\n")
    print("✅ Base file created")

# create versions folder
if not os.path.exists("versions"):
    os.mkdir("versions")

# count versions
version_count = len(os.listdir("versions")) + 1

# create new version file
new_version = f"versions/project_v{version_count}.txt"
shutil.copy(base_file, new_version)

print(f"✅ Version created: {new_version}")

# -------------------- SAVE INTO MYSQL --------------------
query = """
INSERT INTO version_history (version_number, filename, created_at)
VALUES (%s, %s, %s)
"""
values = (version_count, new_version, datetime.datetime.now())

cursor.execute(query, values)
db.commit()

print("📌 Version info saved in MySQL database!")
