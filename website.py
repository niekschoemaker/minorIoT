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

def startThread():
    x = threading.Thread(target=start)
    x.daemon = True
    x.start()
    return x