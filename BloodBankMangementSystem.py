from builtins import print
from tkinter import *
import sqlite3
from tkinter import messagebox
import datetime

root = Tk()

'''
conn = sqlite3.connect('blood_bank.db')
conn.execute("""create table donor_details
             (
             donor_name varchar(20),
             donor_age number(2),
             donor_gender varchar(10),
             donor_address varchar(30),
             donor_contact varchar(12)
             )""")
conn.commit()

conn.execute("""create table blood_details
            (
            blood_group varchar(5),
            blood_platelet number(10),
            blood_rbc number(10),
            blood_date varchar(20)
            )""")
conn.commit()

conn.close()
'''

root.title("Dattaji Bhale Blood Bank")
root.geometry("1360x768")
root.configure(background='maroon')
l3 = Label(root, text="Dattaji Bhale Blood Bank", bg='coral1', font="Helvetica 30 bold").place(x=300, y=50, w=800, h=60)

b1 = Button(root, text="Donor Details ", command=lambda: donordetails()).place(x=500, y=200, w=300, h=40)
l1 = Label(root, text="Click to enter the details of the donor", bg='burlywood1', font="Helvetica 10").place(x=80,
                                                                                                             y=200,
                                                                                                             w=300,
                                                                                                             h=40)

l2 = Label(root, text="Click to enter the details of the blood", bg='burlywood1', font="Helvetica 10").place(x=80,
                                                                                                             y=300,
                                                                                                             w=300,
                                                                                                             h=40)
b2 = Button(root, text="Blood Details ", command=lambda: blooddetails()).place(x=500, y=300, w=300, h=40)

l4 = Label(root, text="Click to view information of blood group", bg='burlywood1', font="Helvetica 10").place(x=80,
                                                                                                              y=400,
                                                                                                              w=300,
                                                                                                              h=40)
b3 = Button(root, text="Blood Group Information ", command=lambda: requestblood()).place(x=500, y=400, w=300, h=40)

b4 = Button(root, text="Exit", bg="sky blue", command=lambda: stop(root)).place(x=900, y=500, w=300, h=40)
v = StringVar()


def insertDonor(name, age, gender, address, contactno):
    conn = sqlite3.connect('blood_bank.db')
    query = f"insert into donor_details values('{name}', {age}, '{gender}', '{address}', '{contactno}')"
    conn.execute(query)
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Donor Details Saved..!")


def insertBlood(bg, plt, rbc, dt):
    conn = sqlite3.connect('blood_bank.db')
    query = f"insert into blood_details values('{bg}', {plt}, {rbc}, '{dt}')"
    conn.execute(query)
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Blood Details Saved..!")


def retrieve(bg):
    request = "select * from donors inner join blood using(id) where bloodgroup ='" + bg + "'"


def sel():
    selection = "You selected the option " + v.get()
    print(selection)


def donordetails():
    global v
    root = Toplevel()
    root.title("DONOR DETAILS")
    root.geometry("1024x768")
    root.configure(background='firebrick4')
    l11 = Label(root, text="Name:", bg='slate gray2', font="Helvetica 10").place(x=40, y=40, w=60, h=20)
    l12 = Label(root, text="Age:", bg='slate gray2', font="Helvetica 10").place(x=40, y=80, w=60, h=20)
    l13 = Label(root, text="Gender:", bg='slate gray2', font="Helvetica 10").place(x=40, y=120, w=60, h=20)
    l14 = Label(root, text="Address:", bg='slate gray2', font="Helvetica 10").place(x=40, y=220, w=60, h=20)
    l5 = Label(root, text="Contact:", bg='slate gray2', font="Helvetica 10").place(x=40, y=260, w=60, h=20)
    e1 = Entry(root)
    e1.place(x=120, y=40)
    e2 = Entry(root)
    e2.place(x=120, y=80)
    r1 = Radiobutton(root, text="Male", variable=v, value="Male", command=sel)
    r1.place(x=120, y=120)
    r2 = Radiobutton(root, text="Female", variable=v, value="Female", command=sel)
    r2.place(x=120, y=150)
    r3 = Radiobutton(root, text="Other", variable=v, value="Other", command=sel)
    r3.place(x=120, y=180)
    e3 = Entry(root)
    e4 = Entry(root)
    e4.place(x=120, y=220)
    e5 = Entry(root)
    e5.place(x=120, y=260)

    b12 = Button(root, text="Back", bg="sky blue", command=lambda: stop(root)).place(x=120, y=300)
    b11 = Button(root, text="Submit", bg="sky blue",
                 command=lambda: insertDonor(e1.get(), e2.get(), v.get(), e4.get(), e5.get())).place(x=40, y=300)
    print(v.get())

    root.mainloop()


def blooddetails():
    root = Tk()
    root.title("BLOOD DETAILS")
    root.geometry("1024x768")
    root.configure(background='firebrick4')
    l5 = Label(root, text="Blood Group:", bg='slate gray2', font="Helvetica 10").place(x=40, y=40, w=250, h=20)
    l6 = Label(root, text="Platelet count (in 100 thousands):", bg='slate gray2', font="Helvetica 10").place(x=40, y=80,
                                                                                                             w=250,
                                                                                                             h=20)
    l7 = Label(root, text="RBC count (in millions):", bg='slate gray2', font="Helvetica 10").place(x=40, y=120, w=250,
                                                                                                   h=20)
    l14 = Label(root, text="Date Of Entry count:", bg='slate gray2', font="Helvetica 10").place(x=40, y=160, w=250,
                                                                                                h=20)
    e1 = Entry(root)
    e1.place(x=350, y=40)
    e2 = Entry(root)
    e2.place(x=350, y=80)
    e3 = Entry(root)
    e3.place(x=350, y=120)
    e4 = Entry(root)
    e4.place(x=350, y=160)
    e4.insert(0, datetime.date.today())
    e4.configure(state=DISABLED)

    b12 = Button(root, text="Back", bg="sky blue", command=lambda: stop(root))
    b12.place(x=200, y=200)
    b11 = Button(root, text="Submit", bg="sky blue",
                 command=lambda: insertBlood(e1.get(), e2.get(), e3.get(), datetime.date.today()))
    b11.place(x=50, y=200)

    root.mainloop()


def requestblood():
    root = Tk()
    root.title("BLOOD GROUP DONOR AND COMPATIBLE ACCEPTOR INFORMATION")
    root.geometry("750x500")
    root.configure(background='IndianRed4')
    l9 = Label(root, text="Information of the Blood donor and compatible acceptor", bg='coral1',
               font="Helvetica 20 bold").place(x=250, y=50, w=900, h=60)
    text = Text(root)
    text.insert(INSERT, "List of Blood donors and compatible blood groups:\n\n ")
    text.insert(END, "A+ Matching donor blood group:A+,A-,O+,O-\n")
    text.insert(END, "A- Matching donor blood group:A-,O-\n")
    text.insert(END, "B+ Matching donor blood group:B+,B-,O+,O-\n")
    text.insert(END, "B- Matching donor blood group:B-,O-\n")
    text.insert(END, "AB+ Compatible with all blood groups\n")
    text.insert(END, "AB-Matching donor blood group:AB-,A-,B-,O-\n")
    text.insert(END, "O+ Matching donor blood group:O+,O-\n")
    text.insert(END, "O- Matching donor blood group:O-\n")
    text.pack(expand=1, fill=BOTH)
    text.pack()

    text.tag_add("here", "5.0", "5.0")
    text.tag_add("start", "5.0", "5.0")
    text.tag_config("here", background="white", foreground="blue")
    text.tag_config("start", background="white", foreground="green")
    root.mainloop()


def stop(root):
    root.destroy()


root.mainloop()