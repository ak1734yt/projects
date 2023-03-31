"""
Created on Thu Feb 17 23:26:59 2022

@author: ak_1734_yt
"""


import csv
import pandas as pd
from tkinter import *
from tkinter import  messagebox 

root = Tk()
root.geometry('420x420')
root.title(' Contact Address Book')
root.resizable(0,0)
root.configure(background="light blue")

df1=pd.DataFrame()
df1=pd.read_csv("contactlist.csv")
l1=df1.values.tolist()
contactlist=l1

Name = StringVar()
Number = StringVar()
Address = StringVar()
PIN = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, xscrollcommand=scroll.set, height=7 ,width=45)
scroll.config (command=select.xview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


def Selected():
    return int(select.curselection()[0])
def AddContact():
    contactlist.append([Name.get(), Number.get() ,Address.get(),PIN.get()])
    N=Name.get()
    No=Number.get() 
    A=Address.get()
    P=PIN.get()
    
    if N =="":
         messagebox.showwarning("error","please enter your name")
    elif No =="":
         messagebox.showwarning("error","please enter your Number")
    elif A =="":
         messagebox.showwarning("error","please enter your Address ")
    elif P=="":
         messagebox.showwarning("error","please enter your Pin code")
    else:
        Label(root,text="Contact added ", font='algerian 12 italic', fg="green").place(x=150,y=300)
    RESET()     
    Select_set()
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(),Address.get(),PIN.get()]
    Label(root,text="Contact edited ", font='algerian 12 italic', fg="green").place(x=150,y=300)
    RESET()  
    Select_set()
def DELETE():
    del contactlist[Selected()]
    Label(root,text="Contact Deleted ", font='algerian 12 italic', fg="green").place(x=150,y=300)
    Select_set()
def VIEW():
    NAME, PHONE , ADDRESS ,PINCODE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Address.set(ADDRESS)
    PIN.set(PINCODE)
def EXIT():
    root.destroy()
def RESET():
    Name.set('')
    Number.set('')
    Address.set('')
    PIN.set('')
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,address,pincode in contactlist :
        select.insert (END, name )
Select_set()

Label(root, text = 'NAME',font=' algerian  12 italic',  ).place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 130, y=20)
Label(root, text = 'PHONE NO.',font='algerian   12 italic').place(x= 30, y=50)
Entry(root, textvariable = Number).place(x= 130, y=50)
Label(root, text = 'ADDRESS',font='algerian   12 italic').place(x= 30, y=80)
Entry(root, textvariable = Address).place(x= 130, y=80)
Label(root, text = 'PINCODE',font='algerian    12 italic').place(x= 30, y=110)
Entry(root, textvariable = PIN).place(x= 130, y=110)

Button(root,text="ADD ",font='algerian    12 italic', bg='green', command = AddContact).place(x= 285, y=45)
Button(root,text="EDIT",font='algerian    12 italic', command = EDIT).place(x= 10, y=160)
Button(root,text="DELETE",font='algerian    12 italic', command = DELETE).place(x= 285, y=80)
Button(root,text="VIEW",font='algerian    12 italic',  command = VIEW).place(x= 65, y=160)
Button(root,text="EXIT",font='algerian    12 italic', bg='red' ,command = EXIT).place(x= 370, y=280)
Button(root,text="CLEAR",font='algerian    12 italic',  command = RESET).place(x= 285, y=115)

root.mainloop()
print(contactlist)
df=pd.DataFrame(contactlist)
df.to_csv("contactlist.csv",index=False)