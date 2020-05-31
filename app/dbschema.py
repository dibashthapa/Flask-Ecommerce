import csv
import sqlite3
import os
import random
import hashlib

DATABASE_NAME ="site.db"
def connect(database=DATABASE_NAME):
    """Return a database connection, by default to
    the configured DATABASE_NAME
    Ensure that the connection is configured to return Row objects
    rather than tuples from queries"""

    c = sqlite3.connect(database)
    c.row_factory = sqlite3.Row

    return c

def create_tables(db):
    """Create and initialise the database tables
    This will have the effect of overwriting any existing
    data."""

    sql = """
    
    DROP TABLE IF EXISTS jewelry;
    CREATE TABLE jewelry (
            id integer unique primary key autoincrement,
            name text,
            description text,
            image_url text,
            category text,
            inventory integer,
            unit_cost number
            );
    """

    db.executescript(sql)
    db.commit()

def sample_data(db):
    """Generate some sample data for testing the web
    application. Erases any existing data in the
    database
    Returns the list of users and the list of positions
    that are inserted into the database"""


    cursor = db.cursor()
    cursor.execute("DELETE FROM jewelry")

    # read sample product data from apparel.csv
    jewelry = {}
    id = 0
    first = True  # flag
    sql = "INSERT INTO jewelry (id, name, description, image_url, category, inventory, unit_cost) VALUES (?, ?, ?, ?, ?, ?, ?)"
    with open(os.path.join(os.path.dirname(__file__), 'jewelry.csv')) as fd:
        reader = csv.DictReader(fd)
        for row in reader:
            if row['Title'] is not '':
                if first:
                    inv = 0  # inventory of first item (Ocean Blue Shirt) is zero
                    first = False
                else:
                    inv = int(random.random()*100)
                cost = int(random.random()*200) + 0.95
                description = "<p>" + row['Body (HTML)'] + "</p>"
                data = (id, row['Title'], description, row['Image Src'], row['Tags'], inv, cost)
                cursor.execute(sql, data)
                jewelry[row['Title']] = {'id': id, 'name': row['Title'], 'description': description, 'category': row['Tags'], 'inventory': inv, 'unit_cost': cost}
                id += 1

    db.commit()

    return jewelry

if __name__=="__main__":
    db = connect(DATABASE_NAME)
    create_tables(db)
    sample_data(db)
