import sqlite3

# According to sqlite docs check_same_thread = False should be safe
conn = sqlite3.connect('data.db', check_same_thread = False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weatherdata ([generated_id] INTEGER PRIMARY KEY, message_id TEXT, device_id TEXT, temperature TEXT, humidity TEXT, pressure TEXT, rasptimestamp TEXT, timestamp NUMERIC);''')

def insert_data(device_id, message_id, temperature, humidity, pressure, rasptimestamp, unixtimestamp):
    cur = conn.cursor()
    cur.execute("INSERT INTO weatherdata (device_id, message_id, temperature, humidity, pressure, rasptimestamp, timestamp) VALUES(?,?,?,?,?,?,?);", (device_id, message_id, temperature, humidity, pressure, rasptimestamp, unixtimestamp))
    cur.execute("select * from weatherdata")
    print(cur.fetchall())
    conn.commit()

def get_data():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM weatherdata")
        data = cur.fetchall()
        return data
    except:
        print("Something went wrong while fetching data")
