import sqlite3
import time
import math

# According to sqlite docs check_same_thread = False should be safe
conn = sqlite3.connect('data.db', check_same_thread = False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weatherdata ([generated_id] INTEGER PRIMARY KEY, id INT, device_id TEXT, temperature NUMERIC, humidity NUMERIC, pressure NUMERIC, rasptimestamp TEXT, timestamp INTEGER);''')

def insert_data(device_id, nr_id, temperature, humidity, pressure, rasptimestamp, unixtimestamp):
    cur = conn.cursor()
    cur.execute("INSERT INTO weatherdata (id, device_id, temperature, humidity, pressure, rasptimestamp, timestamp) VALUES(?,?,?,?,?,?,?);", (nr_id, device_id, temperature, humidity, pressure, rasptimestamp, math.floor(unixtimestamp)))
    conn.commit()

def check_data():
    cur = conn.cursor()
    # Do timestamp minus 15 to make sure it has timed out and not just precision error
    cur.execute("SELECT id, temperature, humidity, pressure, rasptimestamp FROM weatherdata WHERE `timestamp` < %d;" % int(time.time() - 15.0))
    data = cur.fetchall()
    if len(data) > 0:
        print(data)
        return data
    else:
        return None

def delete_data(message_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM weatherdata WHERE id = %d;" % int(message_id))
    conn.commit()
    return

def get_data():
    cur = conn.cursor()
    cur.execute("SELECT * FROM weatherdata;")
    data = cur.fetchall()
    return data

def update_timestamp(id, timestamp):
    cur = conn.cursor()
    cur.execute("UPDATE weatherdata SET timestamp = %s WHERE id = %s" % (str(timestamp), str(id)))
