from pg import PostgresLayer

MAX_EQUIP_NAME			= 20
MAX_EQUIP_DESC			= 255
MAX_EQUIP_OWNER			= 20

MAX_DELEG_NAME			= 20
MAX_DELEG_EMAIL			= 20
MAX_DELEG_COUNTRY		= 3
MAX_DELEG_TEL			= 20

class InOutLayer(object):

	def __init__(self, dbname, host, user, password, debug=False):
		self.pg = PostgresLayer(dbname, host, user, password, debug)

	def __del__(self):
		del self.pg

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

		else:
			resp = self.pg.insert("equipment", e_name=name, description=description, owner=owner)

			if resp['success']:
				print("[io] New equipment created!")
			else:
				print("[io] Failed to insert new equipment.")
				resp['msg'] = "Owner doest exist"

		return resp


	def setEquip(self, id, name="", description="", owner=""):

		if (name) and (len(name) > MAX_EQUIP_NAME):
			print("[io] Invalid equip name: empty or over"+MAX_EQUIP_NAME+".")

		elif (description) and (len(description) > MAX_EQUIP_DESC):
			print("[io] Invalid equip description: empty or over "+MAX_EQUIP_DESC+".")

		elif (owner) and (len(owner) > MAX_EQUIP_OWNER):
			print("[io] Invalid equipment owner: empty or over "+MAX_EQUIP_OWNER+".")

		else:
			resp = self.pg.update("equipment", e_id = id, e_name = name, 
				description=description, owner=owner)

			if resp['success']:
				print("[io] Equipment updated!")
			else:
				print("[io] Failed to update equipment. Wrong id?")


	def delEquip(self, id):
		self.pg.delete("equipment", e_id = id)

	def selectEquip(self, id):
		self.pg.select("equipment", e_id = id)


	#####################################

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

	def delDeleg(self, name):
		self.pg.delete("delegation", d_name = name)

	def selectDeleg(self, name):
		self.pg.select("delegation", d_name = name)
