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

		elif (not description) or (len(description) > MAX_EQUIP_DESC):
			print("[io] Invalid equip description: empty or over "+MAX_EQUIP_DESC+".")

		elif (not owner) or (len(owner) > MAX_EQUIP_OWNER):
			print("[io] Invalid equipment owner: empty or over "+MAX_EQUIP_OWNER+".")
		else:
			resp = self.pg.insert("equipment", e_name=name, description=description, owner=owner)

			if resp['success']:
				print("[io] New equipment created!")
			else:
				print("[io] Failed to insert new equipment. Primary key conflict?")


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

