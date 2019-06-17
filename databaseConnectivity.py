import tkinter as tk
from tkinter import ttk, messagebox


root=tk.Tk()
root.title("Student Management")

label1=tk.Label(root,text="STUDENT MANAGEMENT SYSTEM")
label1.pack()


namelabel=tk.Label(root,text="Enter Your Name")
namelabel.pack()

nameEntry=tk.Entry(root)
nameEntry.pack()

collegelabel=tk.Label(root,text="Enter Your College")
collegelabel.pack()

collegeEntry=tk.Entry(root)
collegeEntry.pack()

addresslabel=tk.Label(root,text="Enter Your Address")
addresslabel.pack()

addressEntry=tk.Entry(root)
addressEntry.pack()

phonelabel=tk.Label(root,text="Enter Your Phone Number")
phonelabel.pack()

phoneEntry=tk.Entry(root)
phoneEntry.pack()

import sqlite3

connection=sqlite3.connect('stdmanagement.db')

TABLE_NAME="student_table"
STUDENT_NAME="student_name"
STUDENT_COLLEGE="student_college"
STUDENT_ADDRESS="student_address"
STUDENT_PHONE="student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME+ " ( "
                   +STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " +STUDENT_PHONE + " INTEGER);")


def takeinput():
    global nameEntry,collegeEntry,addressEntry,phoneEntry
    global studentid,username,college, address ,phone
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE

    username=nameEntry.get()
    nameEntry.delete(0,tk.END)
    college=collegeEntry.get()
    collegeEntry.delete(0,tk.END)
    address=addressEntry.get()
    addressEntry.delete(0,tk.END)
    phone=phoneEntry.get()
    phoneEntry.delete(0,tk.END)

    connection.execute("INSERT INTO  " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                   STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                  STUDENT_PHONE + " ) VALUES( '"
                   + username +"', '"+ college +"', '"+
                   address +"', "+ str(phone) +" ); ")


    connection.commit()
    messagebox.showinfo("success "," data saved successfully ")

def display():

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")

    for row in cursor:

        print("Student Name is: ", row[0])
        print("student College is: ", row[1])
        print("Student Address is: ",row[2])
        print("Student Phone Number is:",row[3])

    connection.close()


button1= tk.Button(root, text="save",command=lambda:takeinput())
button1.pack()

button2= tk.Button(root, text="Retrieve",command=lambda:display())
button2.pack()

root.mainloop()

