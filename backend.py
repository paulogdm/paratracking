from flask import Flask, jsonify, render_template, request, redirect, url_for, abort, session
from inout import InOutLayer

DATABASE = "paradb"
HOST = "198.199.79.4"
USER = "pguser"
PASSWORD = ""

io = InOutLayer(DATABASE, HOST, USER, PASSWORD, True) 

app = Flask(__name__)



@app.route('/equipment/create', methods=['POST'])
def newEquip():
	if request.json:
		json = request.json
		resp = io.newEquip( json['e_name'], json['description'], json['owner'])
		return jsonify(**resp)


@app.route('/delegation/create', methods=['POST'])
def newDeleg():
	if request.json:
		json = request.json
		
		if json['email']:
			email = json['email']
		else: email = ""
		
		if json['tel']: 
			tel = json['tel'] 
		else: tel = ""

		resp = io.newDeleg( json['d_name'], json['country'], email, tel)

		return jsonify(**resp)

@app.route('/')
def index():
	return render_template('gui.html')

if __name__ == "__main__":
	app.run()
