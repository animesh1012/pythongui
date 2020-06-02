# List of participants classs
import sqlite3
class Booklist:

    def __init__(self):
        self.db=sqlite3.connect('ticketchart.db')
        self.db.row_factory=sqlite3.Row
        self.db.execute("create table if not exists Ticket(ID integer primary key autoincrement,Name text,Gender text,Comment text)")
        self.db.commit()
    def Add(self,Name,Gender,Comment):
        self.db.row_factory=sqlite3.Row
        self.db.execute("insert into Ticket(Name,Gender,Comment) values(?,?,?)",(Name,Gender,Comment))
        self.db.commit()
    def showbooking(self):
        return(self.db.execute("select * from Ticket"))
