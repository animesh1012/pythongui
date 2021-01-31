from tkinter import *
from tkinter import ttk
from listitem import Booklist
class ListTicket:
    def __init__(self):
        self.book=Booklist()
        self.root=Tk()
        self.root.title('Ticket Chart')
        tv=ttk.Treeview(self.root)
        tv.pack()
        cursor=self.book.showbooking()
        tv.heading('#0',text='ID')
        tv.configure(column=('Name','Gender','Comment'))
        tv.heading('Name',text='Full Name')
        tv.heading('Gender',text='Gender')
        tv.heading('Comment',text='Comment')
        tv.column('#0',anchor='center')
        tv.column('Name',anchor='center')
        tv.column('Gender',anchor='center')
        tv.column('Comment',anchor='center')
        for row in cursor:
            tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
            tv.set('#{}'.format(row['ID']),'Name',row['Name'])
            tv.set('#{}'.format(row['ID']),'Gender',row['Gender'])
            tv.set('#{}'.format(row['ID']),'Comment',row['Comment'])
        #Styling
        style=ttk.Style(self.root)
        style.theme_use('classic')
        self.root.mainloop()
