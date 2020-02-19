from postgres_config import dbConfig
import psycopg2 as pyo 

con = pyo.connect(**dbConfig)

cursor = con.cursor()

class Bookdb:
    def __init__(self):
        self.con = pyo.connect(**dbConfig)
        self.cursor = con.cursor()
        print("You have connected to the database!")
        print(con)

    def __delete__(self):
        self.con.close()