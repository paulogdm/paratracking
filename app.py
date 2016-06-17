from pg import PostgresLayer

class AppLayer(object):
	def __init__(self, dbname, host, user, password):
		self.pg = PostgresLayer(dbname, host, user, password)

