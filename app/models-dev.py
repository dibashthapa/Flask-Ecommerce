import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'site.db')

def connect(database = DATABASE):
	conn = sqlite3.connect(database)
	conn.row_factory = sqlite3.Row

	return conn


class Products:
	def __init__(self):
		self.db = connect()

	def show_all_tables(self):
		db = self.db
		cur = db.cursor()
		sql = """
		SELECT id,name,price FROM apparels
		UNION
		SELECT id,name,price FROM fashion
		UNION
		SELECT id,name, price FROM bicycles
		UNION 
		SELECT id,name, price FROM jewelry
		ORDER BY name
		 """
		cur.execute(sql)
		results = cur.fetchall()
		return results


if __name__=="__main__":
	grocery = Products()
	rows = grocery.show_all_tables()
	print([dict(p) for p in rows])


