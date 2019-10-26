import sqlite3
import time

# According to sqlite docs check_same_thread = False should be safe
conn = sqlite3.connect('data.db', check_same_thread = False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weatherdata ([generated_id] INTEGER PRIMARY KEY, id INT, message_id TEXT, device_id TEXT, temperature TEXT, humidity TEXT, pressure TEXT, rasptimestamp TEXT, timestamp NUMERIC);''')

def insert_data(device_id, nr_id, message_id, temperature, humidity, pressure, rasptimestamp, unixtimestamp):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO weatherdata (id, device_id, message_id, temperature, humidity, pressure, rasptimestamp, timestamp) VALUES(?,?,?,?,?,?,?,?);", (nr_id, device_id, message_id, temperature, humidity, pressure, rasptimestamp, unixtimestamp))
        cur.execute("SELECT * FROM weatherdata WHERE timestamp < ?", (unixtimestamp - 10))
        print(cur.fetchall())
        conn.commit()
    except:
        print("Something went wrong while inserting data")

def check_data():
    try:
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM weatherdata WHERE timestamp < ?", (time.time() - 10))
        print(cur.fetchall())
        return data
    except:
        print("Something went wrong while checking data")

def delete_data(message_id):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM weatherdata WHERE message_id = ?;", message_id)
        conn.commit()
        return
    except:
        print("Something went wrong while deleting data")

def get_data():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM weatherdata;")
        data = cur.fetchall()
        return data
    except:
        print("Something went wrong while fetching data")
