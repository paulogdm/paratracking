from flask import Flask
from inout import InOutLayer

DATABASE = "paradb"
HOST = "198.199.79.4"
USER = "pguser"
PASSWORD = ""

app = Flask(__name__)

@app.route('/')

@app.route("/")
def index():
	return "Hello World!"

if __name__ == "__main__":
	app.run()
