from app import AppLayer

DATABASE = "paradb"
HOST = "198.199.79.4"
USER = "pguser"
PASSWORD = "rudineiweb"


def main():
	app = AppLayer(DATABASE, HOST, USER, PASSWORD)



if __name__ == "__main__":
	main()