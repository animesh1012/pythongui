from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import speedtest
st = speedtest.Speedtest()
root=Tk()
root.title('SPEED TEST')
root.geometry('420x250+250+150')
root.config(background='#31112c')
label=ttk.Label(root,text='SPEED TEST')
label.grid(row=0,column=1,sticky='snew',padx=3,pady=5)
test=ttk.Button(root,text='TEST SPEED')
test.grid(row=1,column=0,columnspan=2,padx=3,pady=3)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
# Functioning

def spt():
    servernames =[]
    st.get_servers(servernames)
    messagebox.showinfo(title='SPEED TEST',message='Download Speed : {} MBPS\nUpload Speed : {} MBPS\nPing : {}'.format(st.download()/(1024*1024),st.upload()/(1024*1024),st.results.ping))

test.config(command=spt)


# Style
style=ttk.Style()
style.theme_use('clam')
style.configure('TLabel',background='#31112c',foreground='#f4f4f4',font=('Arial',30))
style.configure('TButton',background='#ffc93c',font=('Arial',20))
style.map('TButton',background=[('pressed','#ec0101')])

root.mainloop()
