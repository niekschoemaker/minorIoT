from flask import Flask
import database

app = Flask(__name__)

@app.route("/")
def hello():
    data = database.get_data()
    print(data)
    return str(data)