#pg.py
#Postgresql layer

import psycopg2

class PostgresLayer(object):

	# Constructor
	# > Args: 	dbname (required) => name of database created BEFORE
	# 			host (required) => IP (Default port 5432) // localhost if youre
	# 				running postgres on this machine
	# 			user (required) => Your pg user // check your permission
	# 			password (required) => String
	# 			DEBUG_MODE (optional) => True if you want explicit query prints
	# 				
	def __init__(self, dbname, host, user, password, DEBUG_MODE = False):
		
		try:
			self.conn =  psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
			self.cursor = self.conn.cursor()

		except:
			print("Connect to database FAILED!")
			raise ValueError

		self.DEBUG_MODE = DEBUG_MODE
		
		self.insert_req_args = {}	# required fields to insert
		self.insert_ret_args = {}	# fields to return if needed by gui/app
		self.upsert_opt_args = {}	# optional fields to insert/update
		self.update_req_args = {}	# if one update must be performed >> keys for where

		self.init_dict()

		def __del__(self):
			self.conn.close()

	def init_dict(self):

		self.insert_req_args['delegation'] = ['d_name', 'country']
		self.insert_ret_args['delegation'] = []
		self.upsert_opt_args['delegation'] = ['email', 'tel']
		self.update_req_args['delegation'] = ['d_name']

		self.insert_req_args['equipment'] = ['e_name', 'description', 'owner']
		self.insert_ret_args['equipment'] = ['e_id']
		self.upsert_opt_args['equipment'] = []
		self.update_req_args['equipment'] = ['e_id']

		self.insert_req_args['facility'] = ['f_name']
		self.insert_ret_args['facility'] = []
		self.upsert_opt_args['facility'] = ['adress', 'capacity']
		self.update_req_args['facility'] = ['f_name']

		self.insert_req_args['stock'] = ['f_name', 'e_id']
		self.insert_ret_args['stock'] = []
		self.upsert_opt_args['stock'] = []
		self.update_req_args['stock'] = ['f_name', 'e_id']

		self.insert_req_args['employee'] = ['CPF', 'RG', 'civil_name', 'work_on', 'password']
		self.insert_ret_args['employee'] = []
		self.upsert_opt_args['employee'] = ['is_active']
		self.update_req_args['employee'] = ['CPF']

		self.insert_req_args['employee_fluent'] = ['CPF', 'language']
		self.insert_ret_args['employee_fluent'] = []
		self.upsert_opt_args['employee_fluent'] = []
		self.update_req_args['employee'] = ['CPF', 'language']

		self.insert_req_args['supervisor'] = ['CPF']
		self.insert_ret_args['supervisor'] = []
		self.upsert_opt_args['supervisor'] = ['level']
		self.update_req_args['supervisor'] = ['CPF']

		self.insert_req_args['supervisor_of'] = ['CPF_sup', 'CPF_emp']
		self.insert_ret_args['supervisor_of'] = []
		self.upsert_opt_args['supervisor_of'] = []
		self.update_req_args['supervisor_of'] = ['CPF_sup', 'CPF_emp']
		
		self.insert_req_args['local_of_equip'] = ['e_id', 'local']
		self.insert_ret_args['local_of_equip'] = ['status']
		self.upsert_opt_args['local_of_equip'] = []
		self.update_req_args['local_of_equip'] = ['e_id']
		
		self.insert_req_args['request'] = ['e_id', 'local_in', 'local_out', 'date_in', 'date_out']
		self.insert_ret_args['request'] = ['r_id']
		self.upsert_opt_args['request'] = []
		self.update_req_args['request'] = ['r_id']

		self.insert_req_args['service'] = ['r_id', 'employee', 'description']
		self.insert_ret_args['service'] = ['s_id']
		self.upsert_opt_args['service'] = []
		self.update_req_args['service'] = ['s_id']


	#################################################
	#				AUX FUNCTIONS					#
	#################################################
	
	# String functions
	# Description: Prepare strings for postgre fields 

	def singleQuote(self, str):
		return str.replace("'", "''")

	# Postgre explicit functions
	# Description: 	Functions to execute querys and get
	# 				responses from postgre 
	
	# Execute query. If fails, do rollback, if success, 
	# 	commit changes.
	# > Args: 	sql (required) => query to execute
	# < Return:	Dictionary with "sucess" flag and/or 
	# 			"err" flag
	def exec(self, sql):
		try:
			self.cursor.execute(sql)

		except Exception as err:
			self.cursor.execute("ROLLBACK;")
			
			resp = {'success': False}
			resp['err'] = err.pgcode
		else:
			self.cursor.execute("COMMIT;")
			resp = {'success': True}

		return resp
		
	# Fetch one result. Useful for simple selects based o Pkey
	# > Args: 	none
	# < Return:	row
	def fetchone(self):
		return self.cursor.fetchone()

	# Fetch all results. Useful for complex querys
	# > Args: 	none
	# < Return:	set of rows
	def fetchall(self):
		return self.cursor.fetchall()
		

	#################################################
	#				GENERIC DB FUNCTIONS			#
	#################################################
	
	def insert(self, table_target,**kwargs):

		insert_req_args = self.insert_req_args[table_target]
		insert_ret_args = self.insert_ret_args[table_target]
		upsert_opt_args = self.upsert_opt_args[table_target]

		if not table_target or not insert_req_args:
			return {'success': False, 'err': 'Table doesnt exist'}

		pgquery = "INSERT INTO "+table_target+ " ("
		values = " ("

		for field in insert_req_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + ","
				values += "'" + kwargs[field] + "',"
			else:
				return {'success' : False, 'err': 'Missing input'}

		for field in upsert_opt_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + ","
				values += "'" + str(kwargs[field]) + "',"

		pgquery = pgquery[:-1] + ") "
		values = values[:-1] + ") "

		pgquery = pgquery + " VALUES " + values + ";"

		if self.DEBUG_MODE:
			print(pgquery)

		resp = self.exec(pgquery);
	
		if self.DEBUG_MODE:
			print(resp)

		return resp

	def update(self, table_target, **kwargs):

		insert_req_args = self.insert_req_args[table_target]
		insert_ret_args = self.insert_ret_args[table_target]
		upsert_opt_args = self.upsert_opt_args[table_target]
		update_req_args = self.update_req_args[table_target]

		if not table_target or not upsert_opt_args:
			return {'success': False, 'err': 'Table doesnt exist'}
		
		pgquery = "UPDATE "+table_target+ " SET "
		
		for field in insert_req_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "',"

		for field in upsert_opt_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "',"

		pgquery = pgquery[:-1] + " WHERE "

		for field in update_req_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "' and "
			else: return {'success' : False, 'err': 'Missing input'}

		pgquery = pgquery[:-4] + ";"

		if self.DEBUG_MODE:
			print(pgquery)

		return self.exec(pgquery);

	def delete(self, table_target, **kwargs):

		update_req_args = self.update_req_args[table_target]

		if not table_target or not update_req_args:
			return {'success': False, 'err': 'Table doesnt exist'}
		
		pgquery = "DELETE FROM " + table_target + " WHERE "

		for field in update_req_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "' and "
			else: return {'success' : False, 'err': 'Missing input'}

		pgquery = pgquery[:-4] + ";"

		if self.DEBUG_MODE:
			print(pgquery)

		return self.exec(pgquery);


	#################################################
	#				SPECIFIC DB FUNCTIONS			#
	#################################################

	def selectAllEquips(self):
		pgquery = "SELECT * FROM equipment ORDER BY e_id asc;"

		if self.DEBUG_MODE:
			print(pgquery)
		
		self.cursor.execute(pgquery)

		columns = ('id', 'name', 'description', 'owner')
		results = []

		for row in self.fetchall():
			results.append(dict(zip(columns, row)))

		return results

	def selectAllDelegs(self):
		pgquery = "SELECT * FROM delegation ORDER BY d_name asc;"

		if self.DEBUG_MODE:
			print(pgquery)
		
		self.cursor.execute(pgquery)
		
		columns = ('name', 'country', 'email', 'tel')
		results = []

		for row in self.fetchall():
			results.append(dict(zip(columns, row)))

		return results

	def selectAllEmployees(self):
		pgquery =  "SELECT employee.*, supervisor.level FROM employee "
		pgquery += "LEFT OUTER JOIN supervisor on employee.CPF = supervisor.CPF "
		pgquery += "ORDER BY employee.CPF asc;"

		if self.DEBUG_MODE:
			print(pgquery)
		
		self.cursor.execute(pgquery)
		
		columns = ('CPF', 'RG', 'name', 'work_on', 'password', 'is_active', 'level')
		results = []

		for row in self.fetchall():
			results.append(dict(zip(columns, row)))

		return results

