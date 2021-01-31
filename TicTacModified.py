# Tic Tac Toy Game
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
root=Tk()
ActivePlayer=1
p1=[]
p2=[]
winner=-1
root.title('TicTacToyGame:Player 1')
#Function
def Buclick(id):
    global ActivePlayer
    global p1
    global p2
    if ActivePlayer==1:
        SetLayout(id,'X')
        p1.append(id)
        root.title('TicTacToyGame:Player 2')
        ActivePlayer=2
        print('P1:{}'.format(p1))
    if ActivePlayer==2:
        Autoplay()
    if winner==-1:
        Checkwinner()

def SetLayout(id,symbol):
    if id==1:
        button1.config(text=symbol)
        button1.state(['disabled'])
    if id==2:
        button2.config(text=symbol)
        button2.state(['disabled'])
    if id==3:
        button3.config(text=symbol)
        button3.state(['disabled'])
    if id==4:
        button4.config(text=symbol)
        button4.state(['disabled'])
    if id==5:
        button5.config(text=symbol)
        button5.state(['disabled'])
    if id==6:
        button6.config(text=symbol)
        button6.state(['disabled'])
    if id==7:
        button7.config(text=symbol)
        button7.state(['disabled'])
    if id==8:
        button8.config(text=symbol)
        button8.state(['disabled'])
    if id==9:
        button9.config(text=symbol)
        button9.state(['disabled'])

def Checkwinner():
    #Row 1,2,3
    global winner
    if (1 in p1)and(2 in p1)and(3 in p1):
        winner=1
    if (1 in p2)and(2 in p2)and(3 in p2):
        winner=2
    #Row 4,5,6
    if (4 in p1)and(5 in p1)and(6 in p1):
        winner=1
    if (4 in p2)and(5 in p2)and(6 in p2):
        winner=2
    #Row 7,8,9
    if (7 in p1)and(8 in p1)and(9 in p1):
        winner=1
    if (7 in p2)and(8 in p2)and(9 in p2):
        winner=2
    #Row 1,4,7
    if (1 in p1)and(4 in p1)and(7 in p1):
        winner=1
    if (1 in p2)and(4 in p2)and(7 in p2):
        winner=2
    #Row 2,5,8
    if (2 in p1)and(5 in p1)and(8 in p1):
        winner=1
    if (2 in p2)and(5 in p2)and(8 in p2):
        winner=2
    #Row 3,6,9
    if (3 in p1)and(6 in p1)and(9 in p1):
        winner=1
    if (3 in p2)and(6 in p2)and(9 in p2):
        winner=2
    #Button 1,5,9
    if (1 in p1)and(5 in p1)and(9 in p1):
        winner=1
    if (1 in p2)and(5 in p2)and(9 in p2):
        winner=2
    #Button 3,5,7
    if (3 in p1)and(5 in p1)and(7 in p1):
        winner=1
    if (3 in p2)and(5 in p2)and(7 in p2):
        winner=2
    #Winning message
    if winner==1:
        messagebox.showinfo(title="Congrats",message="Player 1: Win")
        k=1
    elif winner==2:
        messagebox.showinfo(title='Congrats',message='Player 2: Win')
        k=1

def Autoplay():
    global p1
    global p2
    global ActivePlayer
    emptycell=[]
    for cell in range(9):
        if not((cell+1 in p1)or(cell+1 in p2)):
            emptycell.append(cell+1)
    randomindex=randint(0,len(emptycell)-1)

#Win
    if (1 in p2)and(2 in p2)and(3 in emptycell):
        SetLayout(3,'O')
        p2.append(3)
        try:
            emptycell.remove(3)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (2 in p2)and(3 in p2)and(1 in emptycell):
        SetLayout(1,'O')
        p2.append(1)
        try:
            emptycell.remove(1)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p2)and(3 in p2)and(2 in emptycell):
        SetLayout(2,'O')
        p2.append(2)
        try:
            emptycell.remove(2)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))


    elif (4 in p2)and(5 in p2)and(6 in emptycell):
        SetLayout(6,'O')
        p2.append(6)
        try:
            emptycell.remove(6)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (4 in p2)and(6 in p2)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (5 in p2)and(6 in p2)and(4 in emptycell):
        SetLayout(4,'O')
        p2.append(4)
        try:
            emptycell.remove(4)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (7 in p2)and(8 in p2)and(9 in emptycell):
        SetLayout(9,'O')
        p2.append(9)
        try:
            emptycell.remove(9)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (7 in p2)and(9 in p2)and(8 in emptycell):
        SetLayout(8,'O')
        p2.append(8)
        try:
            emptycell.remove(8)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (9 in p2)and(8 in p2)and(7 in emptycell):
        SetLayout(7,'O')
        p2.append(7)
        try:
            emptycell.remove(7)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p2)and(4 in p2)and(7 in emptycell):
        SetLayout(7,'O')
        p2.append(7)
        try:
            emptycell.remove(7)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p2)and(7 in p2)and(4 in emptycell):
        SetLayout(4,'O')
        p2.append(4)
        try:
            emptycell.remove(4)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (4 in p2)and(7 in p2)and(1 in emptycell):
        SetLayout(1,'O')
        p2.append(1)
        try:
            emptycell.remove(1)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (2 in p2)and(5 in p2)and(8 in emptycell):
        SetLayout(8,'O')
        p2.append(8)
        try:
            emptycell.remove(8)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (5 in p2)and(8 in p2)and(2 in emptycell):
        SetLayout(2,'O')
        p2.append(2)
        try:
            emptycell.remove(2)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (8 in p2)and(2 in p2)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (3 in p2)and(6 in p2)and(9 in emptycell):
        SetLayout(9,'O')
        p2.append(9)
        try:
            emptycell.remove(9)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (6 in p2)and(9 in p2)and(3 in emptycell):
        SetLayout(3,'O')
        p2.append(3)
        try:
            emptycell.remove(3)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (9 in p2)and(3 in p2)and(6 in emptycell):
        SetLayout(6,'O')
        p2.append(6)
        try:
            emptycell.remove(6)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (3 in p2)and(5 in p2)and(7 in emptycell):
        SetLayout(7,'O')
        p2.append(7)
        try:
            emptycell.remove(7)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (5 in p2)and(7 in p2)and(3 in emptycell):
        SetLayout(3,'O')
        p2.append(3)
        try:
            emptycell.remove(3)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (7 in p2)and(3 in p2)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p2)and(5 in p2)and(9 in emptycell):
        SetLayout(9,'O')
        p2.append(9)
        try:
            emptycell.remove(9)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p2)and(9 in p2)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (9 in p2)and(5 in p2)and(1 in emptycell):
        SetLayout(1,'O')
        p2.append(1)
        try:
            emptycell.remove(1)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

#Defend
    elif (1 in p1)and(2 in p1)and(3 in emptycell):
        SetLayout(3,'O')
        p2.append(3)
        try:
            emptycell.remove(3)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p1)and(3 in p1)and(2 in emptycell):
        SetLayout(2,'O')
        p2.append(2)
        try:
            emptycell.remove(2)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (2 in p1)and(3 in p1)and(1 in emptycell):
        SetLayout(1,'O')
        p2.append(1)
        try:
            emptycell.remove(1)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (4 in p1)and(5 in p1)and(6 in emptycell):
        SetLayout(6,'O')
        p2.append(6)
        try:
            emptycell.remove(6)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (6 in p1)and(5 in p1)and(4 in emptycell):
        SetLayout(4,'O')
        p2.append(4)
        try:
            emptycell.remove(4)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (4 in p1)and(6 in p1)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (7 in p1)and(8 in p1)and(9 in emptycell):
        SetLayout(9,'O')
        p2.append(9)
        try:
            emptycell.remove(9)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (9 in p1)and(7 in p1)and(8 in emptycell):
        SetLayout(8,'O')
        p2.append(8)
        try:
            emptycell.remove(8)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (8 in p1)and(9 in p1)and(7 in emptycell):
        SetLayout(7,'O')
        p2.append(7)
        try:
            emptycell.remove(7)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p1)and(4 in p1)and(7 in emptycell):
        SetLayout(7,'O')
        p2.append(7)
        try:
            emptycell.remove(7)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (4 in p1)and(7 in p1)and(1 in emptycell):
        SetLayout(1,'O')
        p2.append(1)
        try:
            emptycell.remove(1)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p1)and(7 in p1)and(4 in emptycell):
        SetLayout(4,'O')
        p2.append(4)
        try:
            emptycell.remove(4)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (2 in p1)and(5 in p1)and(8 in emptycell):
        SetLayout(8,'O')
        p2.append(8)
        try:
            emptycell.remove(8)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (5 in p1)and(8 in p1)and(2 in emptycell):
        SetLayout(2,'O')
        p2.append(2)
        try:
            emptycell.remove(2)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (2 in p1)and(8 in p1)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (3 in p1)and(6 in p1)and(9 in emptycell):
        SetLayout(9,'O')
        p2.append(9)
        try:
            emptycell.remove(9)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (3 in p1)and(9 in p1)and(6 in emptycell):
        SetLayout(6,'O')
        p2.append(6)
        try:
            emptycell.remove(6)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (6 in p1)and(9 in p1)and(3 in emptycell):
        SetLayout(3,'O')
        p2.append(3)
        try:
            emptycell.remove(3)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (3 in p1)and(5 in p1)and(7 in emptycell):
        SetLayout(7,'O')
        p2.append(7)
        try:
            emptycell.remove(7)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (3 in p1)and(7 in p1)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (7 in p1)and(5 in p1)and(3 in emptycell):
        SetLayout(3,'O')
        p2.append(3)
        try:
            emptycell.remove(3)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p1)and(5 in p1)and(9 in emptycell):
        SetLayout(9,'O')
        p2.append(9)
        try:
            emptycell.remove(9)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (9 in p1)and(5 in p1)and(1 in emptycell):
        SetLayout(1,'O')
        p2.append(1)
        try:
            emptycell.remove(1)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

    elif (1 in p1)and(9 in p1)and(5 in emptycell):
        SetLayout(5,'O')
        p2.append(5)
        try:
            emptycell.remove(5)
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))


    else:
        SetLayout(emptycell[randomindex],'O')
        p2.append(emptycell[randomindex])
        try:
            emptycell.remove(emptycell[randomindex])
        except ValueError:
            pass
        root.title('TicTacToyGame:Player 1')
        ActivePlayer=1
        print('P2:{}'.format(p2))

button1=ttk.Button(root)
button1.grid(row=0,column=0,ipadx=40,ipady=40,sticky='snew')
button1.config(command=lambda:Buclick(1))
button2=ttk.Button(root)
button2.grid(row=0,column=1,ipadx=40,ipady=40,sticky='snew')
button2.config(command=lambda:Buclick(2))
button3=ttk.Button(root)
button3.grid(row=0,column=2,ipadx=40,ipady=40,sticky='snew')
button3.config(command=lambda:Buclick(3))
button4=ttk.Button(root)
button4.grid(row=1,column=0,ipadx=40,ipady=40,sticky='snew')
button4.config(command=lambda:Buclick(4))
button5=ttk.Button(root)
button5.grid(row=1,column=1,ipadx=40,ipady=40,sticky='snew')
button5.config(command=lambda:Buclick(5))
button6=ttk.Button(root)
button6.grid(row=1,column=2,ipadx=40,ipady=40,sticky='snew')
button6.config(command=lambda:Buclick(6))
button7=ttk.Button(root)
button7.grid(row=2,column=0,ipadx=40,ipady=40,sticky='snew')
button7.config(command=lambda:Buclick(7))
button8=ttk.Button(root)
button8.grid(row=2,column=1,ipadx=40,ipady=40,sticky='snew')
button8.config(command=lambda:Buclick(8))
button9=ttk.Button(root)
button9.grid(row=2,column=2,ipadx=40,ipady=40,sticky='snew')
button9.config(command=lambda:Buclick(9))
#Styling
style=ttk.Style()
style.theme_use('classic')

root.mainloop()
