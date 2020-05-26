import sqlite3
import traceback
import os
DATABASE= "site.db"

def connect(db = DATABASE):
    conn = sqlite3.connect(db)
    return conn

class Database:
    def __init__(self):
        conn= connect()
        self.conn= conn
        self.cursor = conn.cursor()
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
        try:
            db.execute(f"SELECT * FROM {self.product_name}")
            products = db.fetchall()
            return products
        except sqlite3.OperationalError:
            return None


class User(Database):
    def __init__(self):
        self.db = Database().get_cursor()
        self.conn= Database().conn

    def add(self):
        db = self.db
        conn = self.conn
        try:
            sql = "SELECT * FROM Users"
            db.execute(sql)
            print(db.fetchall())
        except Exception as e:
            print(e)

    def exits(email):
        db = self.db
        db.execute(f"SELECT email FROM user WHERE user.email={email}")
        user=db.fetchone()
        return True if user == email else False

    def verify(email, password):
        db = self.db
        db.execute(f"SELECT COUNT(email, password) FROM user WHERE user.email = {email} AND user.password = {password}")
        rows = db.fetchone()
        print(rows)



if __name__=="__main__":
    user = User()
    user.add()

