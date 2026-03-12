import sqlite3

DB_FILE = "energy_data.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("SELECT * FROM energy ORDER BY id DESC LIMIT 10")
rows = cursor.fetchall()

print("Last 10 Energy Readings:")
print("ID | Timestamp | Voltage (V) | Current (A) | Power (W)")
for row in rows:
    print(row)

conn.close()