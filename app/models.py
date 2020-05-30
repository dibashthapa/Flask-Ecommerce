import sqlite3

DATABASE= "site.db"

class Database:
    def __init__(self):
        db= DATABASE
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row

    def get_cursor(self):
        return self.cursor

class Product(Database):
    def __init__(self, product_name):
        self.product_name = product_name
        self.db = Database().get_cursor()

    def return_items(self):
        """
        Returns all the rows from 
        the given table
        """
        db = self.db
        db.execute(f"SELECT * FROM {self.product_name}")
        products = db.fetchall()
        return products

class User(Database):
    def __init__(self):
        self.db= Database.get_cursor()

    def add_user(self,name , email, password):
        """
        Add new User with name, 
        email and pasword
        """
        db  = self.db
        db.execute(f"INSERT INTO ")



    