import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weatherdata ([generated_id] INTEGER PRIMARY KEY, device_id TEXT, temperature TEXT, humidity TEXT, pressure TEXT, rasptimestamp TEXT);''')

def insert_data(device_id, temperature, humidity, pressure, rasptimestamp):
    cur = conn.cursor()
    cur.execute("INSERT INTO weatherdata (device_id, temperature, humidity, pressure, rasptimestamp) VALUES(?,?,?,?,?);", (device_id, temperature, humidity, pressure, rasptimestamp))
    cur.execute("select * from weatherdata")
    print(cur.fetchall())
    conn.commit()
