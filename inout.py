from pg import PostgresLayer

#DEFINE				= LENGHTS
MAX_EQUIP_NAME		= 20
MAX_EQUIP_DESC		= 255
MAX_EQUIP_OWNER		= 20

MAX_DELEG_NAME		= 20
MAX_DELEG_EMAIL		= 20
MAX_DELEG_COUNTRY	= 3
MAX_DELEG_TEL		= 20

MAX_FAC_NAME		= 20
MAX_FAC_ADDR		= 50

MAX_CPF 			= 10
MAX_EMP_NAME 		= 20
MAX_RG 				= 10
MAX_PASS 			= 50

MAX_LANG 			= 20


class InOutLayer(object):
	
	# Constructor
	# > Args: 	dbname (required) => name of database created BEFORE
	# 			host (required) => IP (Default port 5432) // localhost if youre
	# 				running postgres on this machine
	# 			user (required) => Your pg user // check your permission
	# 			password (required) => String
	# 			DEBUG_MODE (optional) => True if you want explicit query prints
	# 				
	def __init__(self, dbname, host, user, password, debug=False):
		self.pg = PostgresLayer(dbname, host, user, password, debug)

	def __del__(self):
		del self.pg

	# New Equip
	# > Args: 	name (required) => Equip name
	# 			description (required) => Equip descrip
	# 			owner (required) => Delegation name
	# 			DEBUG_MODE (optional) => True if you want explicit query prints
	# 				
	def newEquip(self, name, description, owner):
		if (not name) or (len(name) > MAX_EQUIP_NAME):
			print("[io] Invalid equip name: empty or over"+MAX_EQUIP_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (not description) or (len(description) > MAX_EQUIP_DESC):
			print("[io] Invalid equip description: empty or over "+MAX_EQUIP_DESC+".")
			resp = {'success' : False, 'msg': 'Description lenght invalid'}

		elif (not owner) or (len(owner) > MAX_EQUIP_OWNER):
			print("[io] Invalid equipment owner: empty or over "+MAX_EQUIP_OWNER+".")
			resp = {'success' : False, 'msg': 'Owner lenght invalid'}

		else: #remember the kwargs?
			resp = self.pg.insert("equipment", e_name=name, description=description, owner=owner)

			if resp['success']:
				print("[io] New equipment created!")
			else:
				print("[io] Failed to insert new equipment.")
				resp['msg'] = "Owner doesnt exist"

		return resp

	# update equip
	# > Args: 	id (required) => key of equip
	# 			name => optional arg
	# 			description => optional arg
	# 			owner => optional arg
	# 				
	def setEquip(self, id, name="", description="", owner=""):

		if (name) and (len(name) > MAX_EQUIP_NAME):
			print("[io] Invalid equip name: empty or over"+MAX_EQUIP_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (description) and (len(description) > MAX_EQUIP_DESC):
			print("[io] Invalid equip description: empty or over "+MAX_EQUIP_DESC+".")
			resp = {'success' : False, 'msg': 'Description lenght invalid'}

		elif (owner) and (len(owner) > MAX_EQUIP_OWNER):
			print("[io] Invalid equipment owner: empty or over "+MAX_EQUIP_OWNER+".")
			resp = {'success' : False, 'msg': 'Owner lenght invalid'}

		else:
			resp = self.pg.update("equipment", e_id = id, e_name = name, 
				description=description, owner=owner)

			if resp['success']:
				print("[io] Equipment updated!")
			else:
				print("[io] Failed to update equipment. Wrong id?")
				resp['msg'] = "Failed."
		return resp

	# Delete Equipment
	# > Args: 	id (required) => id of equip
	def delEquip(self, id):

		resp = self.pg.delete("equipment", e_id = id)

		if resp['success']:
			print("[io] Equipment deleted!")
		else:
			print("[io] Failed to delete equipment. Wrong id?")

		return resp;

	# Select ONE Equipment
	# > Args: 	id (required) => id of equip
	def selectEquip(self, id):
		return self.pg.select("equipment", e_id = id)

	# Select ALL Equipments
	def selectAllEquips(self):
		resp = {'success': True}
		resp['list'] = self.pg.selectAllEquips()
		return resp

	#####################################
	# 		DELEGATION FUNCTIONS		#
	#####################################
	
	# New Delegation
	# > Args: 	name (required) => name of delegation
	# 			country (required) => country of delegation
	# 			email (opt) => email of delegation
	def newDeleg(self, name, country, email="", tel=""):

		#REQUIRED
		if (not name) or (len(name) > MAX_DELEG_NAME):
			print("[io] Invalid delegation name: empty or over"+MAX_DELEG_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (not country) or (len(country) > MAX_DELEG_COUNTRY):
			print("[io] Invalid delegation country: empty or over "+MAX_DELEG_COUNTRY+".")
			resp = {'success' : False, 'msg': 'Country lenght invalid'}

		#OPT
		elif (email) and (len(email) > MAX_DELEG_EMAIL):
			print("[io] Invalid delegation email: empty or over "+MAX_DELEG_EMAIL+".")
			resp = {'success' : False, 'msg': 'Email lenght invalid'}
			
		elif (tel) and (len(tel) > MAX_DELEG_TEL):
			print("[io] Invalid delegation tel: empty or over "+MAX_DELEG_TEL+".")
			resp = {'success' : False, 'msg': 'Telephone lenght invalid'}

		else:
			resp = self.pg.insert("delegation", d_name=name, country=country, email=email, tel=tel)

			if resp['success']:
				print("[io] New delegation created!")
			else:
				print("[io] Failed to insert new delegation.")
				resp['msg'] = "Name is taken"

		return resp

	# New Delegation
	# > Args: 	name (required) => name of delegation
	# 			country (opt) => country of delegation
	# 			email (opt) => email of delegation
	# 			tel (opt) => tel of delegation
	def setDeleg(self, name, country="", email="", tel=""):
		if (name) and (len(name) > MAX_DELEG_NAME):
			print("[io] Invalid delegation name: empty or over"+MAX_DELEG_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (country) and (len(country) > MAX_DELEG_COUNTRY):
			print("[io] Invalid delegation country: empty or over "+MAX_DELEG_COUNTRY+".")
			resp = {'success' : False, 'msg': 'Country lenght invalid'}

		elif (email) and (len(email) > MAX_DELEG_EMAIL):
			print("[io] Invalid delegation email: empty or over "+MAX_DELEG_EMAIL+".")
			resp = {'success' : False, 'msg': 'Email lenght invalid'}
			
		elif (tel) and (len(tel) > MAX_DELEG_TEL):
			print("[io] Invalid delegation tel: empty or over "+MAX_DELEG_TEL+".")
			resp = {'success' : False, 'msg': 'Telephone lenght invalid'}

		else:
			resp = self.pg.update("delegation", d_name=name, country=country, email=email, tel=tel)

			if resp['success']:
				print("[io] Delegation updated!")
			else:
				print("[io] Failed to update delegation.")
				resp['msg'] = "Name is taken."

		return resp

	# Delete Delegation
	# > Args: 	name (required) => name of delegation
	def delDeleg(self, name):
		resp = self.pg.delete("delegation", d_name = name)

		if resp['success']:
			print("[io] Equipment deleted!")
		else:
			print("[io] Failed to delete equipment. Wrong name?")

		return resp;

	# Select ONE Delegation
	# > Args: 	name (required) => name of delegation
	def selectDeleg(self, name):
		self.pg.select("delegation", d_name = name)
	
	# Select ALL Delegation
	def selectAllDelegs(self):
		resp = {'success': True}
		resp['list'] = self.pg.selectAllDelegs()
		return resp

	
	#############################
	# 	FACILITY FUNCTIONS 		#
	#############################
	
	# New Facility
	# > Args: 	name (required) => name of facility
	# 			address (opt) => address
	# 			capacity (opt) => capacity
	def newFacility(self, name, address="", capacity=""):
		if (not name) or (len(name) > MAX_FAC_NAME):
			print("[io] Invalid facility name: empty or over"+MAX_FAC_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (address) and (len(address) > MAX_FAC_ADDR):
			print("[io] Invalid facility address: empty or over "+MAX_FAC_ADDR+".")
			resp = {'success' : False, 'msg': 'Address lenght invalid'}

		else:
			resp = self.pg.insert("facility", f_name=name, address=address, capacity=capacity)

			if resp['success']:
				print("[io] New facility created!")
			else:
				print("[io] Failed to insert new facility.")
				resp['msg'] = "Name taken."

		return resp


	# New Facility
	# > Args: 	name (required) => name of facility
	# 			address (opt) => address
	# 			capacity (opt) => capacity
	def setFacility(self, name, address="", capacity=""):
		if (not name) or (len(name) > MAX_FAC_NAME):
			print("[io] Invalid facility name: empty or over"+MAX_FAC_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (address) and (len(address) > MAX_FAC_ADDR):
			print("[io] Invalid facility address: empty or over "+MAX_FAC_ADDR+".")
			resp = {'success' : False, 'msg': 'Address lenght invalid'}

		else:
			resp = self.pg.update("facility", f_name=name, address=address, capacity=capacity)

			if resp['success']:
				print("[io] Facility updated!")
			else:
				print("[io] Failed to insert new facility.")
				resp['msg'] = "Name taken."

		return resp


	# All Facilities
	def selectAllFacilities(self):
		resp = {'success': True}
		resp['list'] = self.pg.selectAllFacilities()
		return resp


	# Delete Facility
	# > Args: 	name (required) => name of facility
	def delFacility(self, name):

		resp = self.pg.delete("facility", f_name = name.strip())

		if resp['success']:
			print("[io] Facility deleted!")
		else:
			print("[io] Failed to delete facility. FK")
			resp['msg'] = "You can't delete the facility if it holds equipment"

		return resp;

	###################
	###################
	###################


	# Get employees that translate one language
	# > Args: 	language (required) => language
	def getTranslator(self, language):

		if (language) and (len(language) > MAX_LANG):
			print("[io] Invalid language: empty or over "+MAX_LANG+".")
			resp = {'success' : False, 'msg': 'Language lenght invalid'}

		else:
			if language:
				language = language.upper()
			else: language = ""

			resp = {'success': True}
			resp['list'] = self.pg.searchTranslator(language)

			if resp['success']:
				print("[io] Translator returned!")

			else:
				print("[io] Failed to search for translator.")
				resp['msg'] = "Search failed..."

		return resp


	# New Employee Fluent in
	# > Args: 	CPF (required) => CPF of employee
	# 			language (required) => new language
	def newLang(self, CPF, language):
		
		#REQUIRED
		if (not CPF) or (len(CPF) > MAX_CPF):
			print("[io] Invalid CPF: empty or over"+MAX_CPF+".")
			resp = {'success' : False, 'msg': 'CPF lenght invalid'}

		elif (not language) or (len(language) > MAX_LANG):
			print("[io] Invalid language: empty or over "+MAX_LANG+".")
			resp = {'success' : False, 'msg': 'Language lenght invalid'}


		else:
			
			language = language.upper()

			resp = self.pg.insert("employee_fluent", CPF=CPF, language=language)

			if resp['success']:
				print("[io] New language created!")
			else:
				print("[io] Failed to insert new language.")
				resp['msg'] = "Relation already exist"

		return resp

	###################
	###################
	###################
	

	# Get All Employees
	def selectAllEmployess(self):
		resp = {'success': True}
		resp['list'] = self.pg.selectAllEmployees()
		return resp


	# New Employee
	# > Args: 	CPF (required)
	# 			RG (required)
	# 			name (required)
	# 			work_on (required) => facility name to work
	# 			password (required)
	def newEmployee(self, CPF, RG, name, work_on, password):
		
		#REQUIRED
		if (not CPF) or (len(CPF) > MAX_CPF):
			print("[io] Invalid CPF: empty or over"+MAX_CPF+".")
			resp = {'success' : False, 'msg': 'CPF lenght invalid'}

		elif (not RG) or (len(RG) > MAX_CPF):
			print("[io] Invalid RG: empty or over "+MAX_CPF+".")
			resp = {'success' : False, 'msg': 'RG lenght invalid'}

		elif (not name) or (len(name) > MAX_EMP_NAME):
			print("[io] Invalid Name: empty or over "+MAX_EMP_NAME+".")
			resp = {'success' : False, 'msg': 'Name lenght invalid'}

		elif (not work_on) or (len(work_on) > MAX_FAC_NAME):
			print("[io] Invalid facility: empty or over "+MAX_FAC_NAME+".")
			resp = {'success' : False, 'msg': 'Facility name lenght invalid'}

		elif (not password) or (len(password) > MAX_PASS):
			print("[io] Invalid password: empty or over "+MAX_PASS+".")
			resp = {'success' : False, 'msg': 'Password lenght invalid'}


		else:
			resp = self.pg.insert("employee", CPF=CPF, RG=RG, 
				civil_name=name, work_on=work_on, password=password)

			if resp['success']:
				print("[io] Employee hired!")

			else:
				print("[io] Failed to hire employee.")
				resp['msg'] = "Employee already exist"

		return resp

	# Delete Employee
	# > Args: 	CPF (required)
	def delEmployee(self, CPF):

		resp = self.pg.delete("employee", CPF = CPF)

		if resp['success']:
			print("[io] Employee deleted!")
		else:
			print("[io] Failed to delete employee. Wrong CPF?")
			resp['msg'] = "Wrong CPF: '"+CPF+"'"

		return resp;


	# New Request
	# > Args: 	id (required) => id of equipment
	# 			local_in (required) => name of facility
	# 			local_out (required) => name of facility
	# 			date_in (required) => date
	# 			date_out (required) => date
	def newRequest(self, id, local_in, local_out, date_in, date_out):
		
		resp = self.pg.insert("request", e_id = id, local_in = local_in, 
			local_out = local_out, date_in = date_in, date_out = date_out)

		if resp['success']:
			print("[io] New request created!")
		else:
			print("[io] Failed to insert request.")
			resp['msg'] = "Facility Origin name and/or destination invalid."

		return resp
