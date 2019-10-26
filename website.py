from flask import Flask
import database
import threading

app = Flask(__name__)

@app.route("/")
def hello():
    data = database.get_data()
    print(data)
    return str(data)

def start():
    app.run(host="0.0.0.0")

# Create a new thread to run the listener since the listener blocks the thread
x = threading.Thread(target=start)
x.start()