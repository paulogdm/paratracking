#pg.py
#Postgresql layer

import psycopg2

class PostgresLayer(object):
	def __init__(self, dbname, host, user, password):
		
		try:
			self.conn =  psycopg2.connect("dbname='"+dbname+"' user='"+user+"' host='"+host+"' password='"+password+"'")
			self.cursor = self.conn.cursor()

		except:
			print("Connect to database FAILED!")
			raise ValueError

	def exec(sql):
		self.cursor(sql)

	def fetch():
		return self.cursor.fetchall()
		

