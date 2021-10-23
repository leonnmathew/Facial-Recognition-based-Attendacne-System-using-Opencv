from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from mainpage import Mainpage
import mysql.connector
import cv2
import os
import numpy as np
from studenttp import student_details1
from recognizer_final import automatic_attendance
from view_attendance import view_attendance


root = Tk()
root.title("GUI")
root.geometry("1550x800+0+0")
bg = ImageTk.PhotoImage(file="Login page image.jpg")
lb_bg = Label(root, image=bg)
lb_bg.place(x=0, y=0, relwidth=1, relheight=1)
lba = Label(root, text="LOGIN SYSTEM", font=("times new roman", 45, "bold"), fg="white", bg="black")
lba.place(x=500, y=100)


def login():
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error", "Kindly Fill all the details to login")

    elif username_entry.get() == "admin" and password_entry.get() == "admin":
        messagebox.showinfo("Sucess", "Your Login Was Successful")
        Mainpage()


    else:
        conn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM register WHERE username=%s AND password=%s",
                          (username_entry.get(), password_entry.get()))

        row = my_cursor.fetchone()
        if row==None:
            messagebox.showerror("error", "Invalid credentials")
        else:
            messagebox.showinfo("Sucess", "Your Login Was Successful")
            Mainpage()



lg_frame = Frame(root, bg="black")
lg_frame.place(x=510, y=200, width=440, height=450)

lb1 = Label(lg_frame, text="Credentials", font=("Times new roman", 30, "bold"), fg="white", bg="black")
lb1.place(x=110, y=20)

# lable for username and password
username_label = Label(lg_frame, text="Username", font=("Times new roman", 25, "bold"), fg="white", bg="black")
username_label.place(x=20, y=110)

username_entry = Entry(lg_frame, font=("Times new roman", 25, "bold"))
username_entry.place(x=20, y=150, width=400)

password_label = Label(lg_frame, text="Password", font=("Times new roman", 25, "bold"), fg="white", bg="black")
password_label.place(x=20, y=198)

password_entry = Entry(lg_frame, font=("Times new roman", 25, "bold"), show="*")
password_entry.place(x=20, y=250, width=400)

login_button = Button(lg_frame, command=login, text="Login", font=("Times new roman", 20, "bold"), bd=3, relief=RIDGE,
                      fg="white", bg="red")
login_button.place(x=20, y=310, width=140, height=40)

# register_page_label = Button(lg_frame, command=registerpage.register, text="New Registration",
#                              font=("Times new roman", 15, "bold"), borderwidth=0, fg="white", bg="black",
#                              activebackground="black")
# register_page_label.place(x=5, y=380, width=170)

# forgot_password_label = Button(lg_frame, text="Forgot Password", font=("Times new roman", 15, "bold"), borderwidth=0,
#                                fg="white", bg="black", activebackground="black")
# forgot_password_label.place(x=180, y=380, width=170)

root.mainloop()
