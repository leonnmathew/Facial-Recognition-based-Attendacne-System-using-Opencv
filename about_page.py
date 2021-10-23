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

def about_details():
    root98=Tk()
    root98.title("About")
    root98.geometry("1550x800+0+0")
    bg1 = ImageTk.PhotoImage(file="about us photo.jpg")
    lb_bg1 = Label(root98, image=bg1)
    lb_bg1.place(x=0, y=0, relwidth=1, relheight=1)
    frame1 = Frame(root98, bg="black")
    frame1.place(x=0, y=0, width=2000, height=100)
    intro_label = Label(frame1, text="Developer Details", font=("times new roman", 50, "bold"),
                        fg="white", bg="black")
    intro_label.place(x=490, y=10)

    # img = Image.open("62180437_362654440935369_4543998936130770584_n.jpg")
    # img = img.resize((200, 200), Image.ANTIALIAS)
    # student_details_button_img = ImageTk.PhotoImage(img)
    # lab=Label(root98,image=student_details_button_img, bg="black")
    # lab.place(x=300, y=300)

    # frameu=Frame(root98, bg="black")
    # frameu.place(x=90,y=200 ,width=1100, height=550)
    # text_label=Label(frameu,text="Developer: Leon Mathew",font=("times new roman", 20, "bold"), bg="black", fg="white")
    # text_label.place(x=40,y=20)
    # text_label1 = Label(frameu, text="Languages Used: Python, Mysql", font=("times new roman", 20, "bold"), bg="black",
    #                    fg="white")
    # text_label1.place(x=40, y=80)


    root98.mainloop()

about_details()