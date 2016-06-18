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
		
		self.key_args = {} # we could change that to WHERE_REQUIRED_ARGS
		self.req_args = {} # we could change that to INSERT_REQUIRED_ARGS
		self.opt_args = {} # we could change that to CAN_BE_NULL_OR_DEFAULT_ARGS

		self.init_dict()

		def __del__(self):
			self.conn.close()

	def init_dict(self):
		
		self.key_args['delegation'] = ['d_name']
		self.req_args['delegation'] = ['country', 'd_name']
		self.opt_args['delegation'] = ['email', 'tel']

		self.key_args['equipment'] = ['e_id']
		self.req_args['equipment'] = ['e_name', 'description', 'owner']
		self.opt_args['equipment'] = []

		self.key_args['facility'] = ['f_name']
		self.req_args['facility'] = ['f_name']
		self.opt_args['facility'] = ['address', 'capacity']

		self.key_args['stock'] = ['f_name', 'e_id']
		self.req_args['stock'] = ['e_id']
		self.opt_args['stock'] = []

		self.key_args['employee'] = ['CPF']
		self.req_args['employee'] = ['CPF', 'RG', 'civil_name', 'work_on', 'password']
		self.opt_args['employee'] = ['is_active']

		self.key_args['employee_fluent'] = ['CPF', 'language']
		self.req_args['employee_fluent'] = ['CPF', 'language']
		self.opt_args['employee_fluent'] = []
		
		self.key_args['supervisor'] = ['CPF']
		self.req_args['stock'] = ['CPF']
		self.opt_args['stock'] = ['level']

		self.key_args['supervisor_of'] = ['CPF_sup', 'CPF_emp']
		self.req_args['supervisor_of'] = ['CPF_sup', 'CPF_emp']
		self.opt_args['supervisor_of'] = []
		
		self.key_args['local_of_equip'] = ['e_id']
		self.req_args['local_of_equip'] = ['e_id', 'local']
		self.opt_args['local_of_equip'] = ['status']
		
		self.key_args['request'] = ['r_id']
		self.req_args['request'] = ['e_id', 'local_in', 'local_out', 'date_in', 'date_out']
		self.opt_args['request'] = []

		self.key_args['service'] = ['s_id']
		self.req_args['local_of_equip'] = ['r_id', 'employee', 'description']
		self.opt_args['local_of_equip'] = []


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

		key_args = self.key_args[table_target]
		req_args = self.req_args[table_target]
		opt_args = self.opt_args[table_target]

		if not table_target or not key_args:
			return {'success': False, 'err': 'Table doesnt exist'}

		pgquery = "INSERT INTO "+table_target+ " ("
		values = " ("

		for field in req_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + ","
				values += "'" + kwargs[field] + "',"
			else:
				return {'success' : False, 'err': 'Missing input'}

		for field in opt_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + ","
				values += "'" + str(kwargs[field]) + "',"

		for field in key_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + ","
				values += "'" + str(kwargs[field]) + "',"
		

		pgquery = pgquery[:-1] + ") "
		values = values[:-1] + ");"

		pgquery = pgquery + " VALUES " + values

		if self.DEBUG_MODE:
			print(pgquery)

		return self.exec(pgquery);

	def update(self, table_target,**kwargs):

		key_args = self.key_args[table_target]
		req_args = self.req_args[table_target]
		opt_args = self.opt_args[table_target]

		if not table_target or not key_args:
			return {'success': False, 'err': 'Table doesnt exist'}
		
		pgquery = "UPDATE "+table_target+ " SET "
		
		for field in req_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "',"

		for field in opt_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "',"

		pgquery = pgquery[:-1] + " WHERE "

		for field in key_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "' and "

		pgquery = pgquery[:-4] + ";"

		if self.DEBUG_MODE:
			print(pgquery)

		return self.exec(pgquery);

	def delete(self, **kwargs):

		key_args = self.key_args[table_target]
		
		if not table_target or not key_args:
			return {'success': False, 'err': 'Table doesnt exist'}
		
		pgquery = "DELETE FROM "+table_target+" WHERE "

		for field in key_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "' and "

		pgquery = pgquery[:-4] + ";"

		if self.DEBUG_MODE:
			print(pgquery)

		return self.exec(pgquery);

	def select(self, **kwargs):

		key_args = self.key_args[table_target]
		
		if not table_target or not key_args:
			return {'success': False, 'err': 'Table doesnt exist'}
		
		pgquery = "SELECT * FROM "+table_target+" WHERE "

		for field in key_args:
			if field in kwargs and kwargs[field]:
				pgquery += field + " = '" + str(kwargs[field]) + "' and "

		pgquery = pgquery[:-4] + ";"

		if self.DEBUG_MODE:
			print(pgquery)

		return self.exec(pgquery);

	#################################################
	#				SPECIFIC DB FUNCTIONS			#
	#################################################


