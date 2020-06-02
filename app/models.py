import sqlite3
import os
DATABASE = os.path.join(os.path.dirname(__file__), 'site.db')

def connect(database = DATABASE):
    c = sqlite3.connect(database, check_same_thread=False)
    c.row_factory = sqlite3.Row
    return c


class Product:
    def __init__(self, product_name=None, db=connect()):
        self.product_name = product_name
        self.cursor = db.cursor()

    def return_items(self):
        """
        Returns all the rows from 
        the given table
        """
        cur = self.cursor
        cur.execute(f"SELECT * FROM {self.product_name}")
        products = cur.fetchall()
        return products

    def show_all_items(self):
        cur = self.cursor
        sql = """
        SELECT id,name,price, description,img_url FROM apparels
        UNION
        SELECT id,name,price, description,img_url FROM fashion
        UNION
        SELECT id,name, price, description,img_url FROM bicycles
        UNION 
        SELECT id,name, price, description,img_url FROM jewelry
        ORDER BY name
         """
        cur.execute(sql)
        results = cur.fetchall()
        return results

class User:
    def __init__(self, db=connect()):
        self.cursor = db.cursor()
        self.db = db

    def add(self, fname, lname, email, password):
        sql = f"INSERT INTO User(fname, lname, email, password) VALUES(?,?,?,?)"
        data=(fname, lname, email, password)
        cur = self.cursor
        cur.execute(sql, data)
        self.db.commit()
        

    def verify(self, email ,password):
        sql = f"SELECT email , password FROM User WHERE email='{email}' AND password='{password}'"
        cur = self.cursor
        cur.execute(sql)
        result = cur.fetchall()
        row_count =  len(result)
        print(row_count)
        if row_count == 1 :
            return True
        else:
            return False




class Review:
    def __init__(self):
        pass

    def __repr__(self):
        pass

