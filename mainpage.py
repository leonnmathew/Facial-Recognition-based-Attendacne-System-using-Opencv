from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import mysql.connector
import cv2
import os
import numpy as np
from studenttp import student_details1
from recognizer_final import automatic_attendance
from view_attendance import view_attendance



def Mainpage():
    root2 = Toplevel()
    root2.title("Main Window")
    root2.geometry("1550x800+0+0")

    def open_explorer():
        filename = filedialog.askopenfilename(initialdir="dataset",
                                              title="Select a File",
                                              filetypes=(("JPG Files",
                                                          "*.jpg*"),
                                                         ("all files",
                                                          "*.*")), parent=root2)

    bg1 = ImageTk.PhotoImage(file="aSAF.jpg")
    lb_bg1 = Label(root2, image=bg1)
    lb_bg1.place(x=0, y=0, relwidth=1, relheight=1)
    frame1 = Frame(root2, bg="white")
    frame1.place(x=0, y=0, width=2000, height=100)
    intro_label = Label(frame1, text="Facial Recognition Attendance System", font=("times new roman", 45, "bold"),
                        fg="black", bg="white")
    intro_label.place(x=290, y=10)
    img = Image.open("meta-teaching-181210.jpg")
    img=img.resize((240,190),Image.ANTIALIAS)
    student_details_button_img=ImageTk.PhotoImage(img)
    student_details_button_Label=Label(root2,text="Register Students",fg="white", bg="black",font=("times new roman", 23, "bold"))
    student_details_button_Label.place(x=200, y=400)


    img1 = Image.open("woman-hand-writing-attendance-marker-blue-background-professionally-79573891.jpg")
    img1 = img1.resize((240, 190), Image.ANTIALIAS)
    Mark_attendance_button_img = ImageTk.PhotoImage(img1)

    Mark_attendance_button_Label = Label(root2, text="Mark Attendance", fg="white", bg="black",
                                         font=("times new roman", 23, "bold"))
    Mark_attendance_button_Label.place(x=600, y=400)

    img2 = Image.open("student-attendance-software.jpeg")
    img2 = img2.resize((240, 190), Image.ANTIALIAS)
    view_attendance_button_img = ImageTk.PhotoImage(img2)

    view_attendance_button_Label = Label(root2, text="View Attendance", fg="white", bg="black",
                                         font=("times new roman", 23, "bold"))
    view_attendance_button_Label.place(x=1000, y=400)

    img3 = Image.open("dd-e1547642312239.jpg")
    img3 = img3.resize((240, 190), Image.ANTIALIAS)
    view_dataset_button_img = ImageTk.PhotoImage(img3)

    view_dataset_button_Label = Label(root2, text="View Dataset", fg="white", bg="black",
                                         font=("times new roman", 23, "bold"))
    view_dataset_button_Label.place(x=200, y=700)

    img4 = Image.open("about-us.jpg")
    img4 = img4.resize((240, 190), Image.ANTIALIAS)
    About_button_img = ImageTk.PhotoImage(img4)

    About_button_Label = Label(root2, text="About Us", fg="white", bg="black",
                                         font=("times new roman", 23, "bold"))
    About_button_Label.place(x=600, y=700)

    img5 = Image.open("exit_PNG2.png")
    img5 = img5.resize((240, 190), Image.ANTIALIAS)
    exit_button_img = ImageTk.PhotoImage(img5)

    # exit_button_Label = Label(root2, text="Exit", fg="white", bg="black",
    #                                      font=("times new roman", 23, "bold"))
    # exit_button_Label.place(x=1000, y=700)



    student_details_button = Button(root2, border=0, text="students details",command=student_details1,font=("times new roman", 15, "bold"), image=student_details_button_img)  #student details button
    student_details_button.place(x=200, y=200, width=240, height=190)

    mark_attendance_button = Button(root2, border=0, text="Mark Attendance", command=automatic_attendance,font=("times new roman", 15, "bold"),image=Mark_attendance_button_img)        #Mark Attendance button
    mark_attendance_button.place(x=600, y=200, width=240, height=190)

    view_attendance_button = Button(root2, border=0 , text="View Attendance",command=view_attendance,font=("times new roman", 15, "bold"),image=view_attendance_button_img)   #View Attendance button
    view_attendance_button.place(x=1000, y=200, width=240, height=190)

    view_dataset_button = Button(root2, border=0 , text="View Dataset", command=open_explorer,font=("times new roman", 15, "bold"), image=view_dataset_button_img)  #View dataset button
    view_dataset_button.place(x=200, y=500, width=240, height=190)

    About_details_button = Button(root2, border=0 , text="About",font=("times new roman", 15, "bold"), image=About_button_img)   #About details button
    About_details_button.place(x=600, y=500, width=240, height=190)

    exit_button = Button(root2, border=0 , text="Exit", command=root2.destroy ,font=("times new roman", 15, "bold"), image=exit_button_img)    #Exit button
    exit_button.place(x=1000, y=500, width=240, height=190)
    root2.mainloop()



