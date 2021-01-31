#Ticket Reservation Layout
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from listitem import Booklist
from listreservation import ListTicket
#import tkinter
Book=Booklist()
#Main Code
root=Tk()
root.configure(background='#e1d8b2')
root.title('Ticket Reservation')
ttk.Label(root,text='Full Name:').grid(row=0,column=0,pady=10,padx=10)
nameentry=ttk.Entry(root,width=24,font=('Arial',15))
nameentry.grid(row=0,column=1,columnspan=2)
initvariable=StringVar()
initvariable.set('Male')
ttk.Label(root,text='Gender:').grid(row=1,column=0,padx=10)
ttk.Radiobutton(root,text='Male',variable=initvariable,value='Male').grid(row=1,column=1)
ttk.Radiobutton(root,text='Female',variable=initvariable,value='Female').grid(row=1,column=2)
ttk.Label(root,text='Comment:').grid(row=2,column=0,padx=10)
text=Text(root,height=15,width=33)
text.grid(row=2,column=1,columnspan=2)
Bsubmit=ttk.Button(root,text='Submit')
Bsubmit.grid(row=3,column=3,padx=10)
#List Button
Lbutton=ttk.Button(root,text='List Reservation')
Lbutton.grid(row=3,column=2)
#Booklist class function
def Submitclick():
    Book.Add(nameentry.get(),initvariable.get(),text.get(1.0,'end'))
    nameentry.delete(0,'end')
    text.delete(1.0,'end')
    messagebox.showinfo(title='Booking Portal',message='Your Response has been Recorded !!')
Bsubmit.config(command=Submitclick)
#Tree View class function
def Lbuttonclick():
    list=ListTicket()
Lbutton.config(command=Lbuttonclick)
#Style
style=ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background='#e1d8b2',font=('Arial',11))
style.configure('TButton',background='#e1d8b2',font=('Arial',11))
style.configure('TRadiobutton',background='#e1d8b2',font=('Arial',11))


root.mainloop()
