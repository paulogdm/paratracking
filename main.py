from inout import InOutLayer

DATABASE = "paradb"
HOST = "198.199.79.4"
USER = "pguser"
PASSWORD = ""

def main():
	app = InOutLayer(DATABASE, HOST, USER, PASSWORD, True)
	

if __name__ == "__main__":
	main()