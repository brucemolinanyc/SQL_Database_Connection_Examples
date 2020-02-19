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

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, title, author, isbn):
        sql =("INSERT INTO books(title, author,isbn) VALUES(?,?,?)")
        values = [title, author, isbn]
        self.cursor.execute(sql, values)
        self.con.commit()
        messagebox.showinfo(title="Book Database", message="New book added to database")
    
    def update(self, id, title, author, isbn):
        sql = "UPDATE books SET title = ?, author = ?, isbn = ? WHERE id =?"
        self.cursor.execute(sql, [title,author, isbn, id])
        self.con.commit()
        messagebox.showinfo(title="Book Database", message="Book Updated")
    
    def delete(self, id):
        sql = 'DELETE FROM books WHERE id = ?'
        self.cursor.execute(sql, [id])
        self.con.commit()
        messsagebox.showinfo(title="Book Database", message="Book Deleted")



