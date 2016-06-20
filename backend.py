from flask import *
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


@app.route('/equipment/get', methods=['POST'])
def getEquip():
	
	resp = io.selectAllEquips()

	return jsonify(**resp)

@app.route('/delegation/get', methods=['POST'])
def getDeleg():
	
	resp = io.selectAllDelegs()

	return jsonify(**resp)

@app.route('/equipment/delete', methods=['POST'])
def delEquip():
	if request.json:
		json = request.json
		resp = io.delEquip(json['id'])
		return jsonify(**resp)

@app.route('/delegation/delete', methods=['POST'])
def delDeleg():
	if request.json:
		json = request.json
		resp = io.delDeleg(json['d_name'])
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

@app.route('/facility/create', methods=['POST'])
def newFacility():
	if request.json:
		json = request.json

		if json['address']: 
			add = json['address'] 
		else: address = ""

		if json['capacity']: 
			add = json['capacity'] 
		else: capacity = ""

		resp = io.newFacility( json['f_name'], address, capacity)
		return jsonify(**resp)

@app.route('/language/create', methods=['POST'])
def newLanguage():
	if request.json:
		json = request.json

		resp = io.newLang( json['CPF'], json['language'])

		return jsonify(**resp)

@app.route('/employee/create', methods=['POST'])
def newEmployee():
	if request.json:
		json = request.json

		resp = io.newEmployee( json['CPF'], json['RG'], json['name'], 
			json['work_on'], json['password'])

		return jsonify(**resp)

@app.route('/employee/get', methods=['POST'])
def getEmployee():
	resp = io.selectAllEmployess()

	return jsonify(**resp)

@app.route('/employee/delete', methods=['POST'])
def delEmployee():
	if request.json:
		json = request.json
		
		resp = io.delEmployee(json['CPF'])

		return jsonify(**resp)


@app.route('/')
def index():
	return send_from_directory('views','gui.html')

@app.route('/emp')
def employee():
	return send_from_directory('views','employee.html')

@app.route('/del')
def deleg():
	return send_from_directory('views','delegation.html')

@app.route('/sup')
def supervisor():
	return send_from_directory('views','supervisor.html')

@app.route('/gui.css')
def css():
	return send_from_directory('static','gui.css')


@app.route('/js/<name>')
def js(name):
	fname = '%s' % name
	return send_from_directory('static',fname)


if __name__ == "__main__":
	app.run()
