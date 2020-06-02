# Age Calculator
from tkinter import *
from tkinter import ttk
import datetime
from datetime import date
from tkinter import messagebox
root=Tk()
label=ttk.Label(root,text="AGE CALCULATOR")
label.grid(row=0,column=1,pady=3,padx=3)
name=ttk.Label(root,text='Name:')
name.grid(row=1,column=0,pady=3,padx=3)
nameentry=ttk.Entry(root,width=20)
nameentry.grid(row=1,column=1,pady=3,padx=3)
year=ttk.Label(root,text='Year:')
year.grid(row=2,column=0,pady=3,padx=3)
yearentry=ttk.Entry(root,width=20)
yearentry.grid(row=2,column=1,pady=3,padx=3)
month=ttk.Label(root,text='Month:')
month.grid(row=3,column=0,pady=3,padx=3)
monthentry=ttk.Entry(root,width=20)
monthentry.grid(row=3,column=1,pady=3,padx=3)
day=ttk.Label(root,text='Day:')
day.grid(row=4,column=0,pady=3,padx=3)
dayentry=ttk.Entry(root,width=20)
dayentry.grid(row=4,column=1,pady=3,padx=3)
agecal=ttk.Button(root,text="Calculate Age")
agecal.grid(row=5,column=1)
#Disable Mode

#Function
def agecalculator():
    currentdate=datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)
    dob=datetime.date(int(yearentry.get()),int(monthentry.get()),int(dayentry.get()))
    age=round((currentdate-dob).days/365.2425)
    messagebox.showinfo(title='AGE',message="You are {} year old.".format(age))

agecal.config(command=agecalculator)
#Styling
style=ttk.Style()
style.theme_use('clam')
style.configure('TButton',background='red',foreground='blue')
style.map('TButton',background=[('pressed','green'),('disabled','grey')])
style.configure('TLabel',font=('Arial',13))



root.mainloop()
