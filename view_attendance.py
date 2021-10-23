import csv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
import os.path
from os import path


def view_attendance():
    root56 = Toplevel()
    root56.title('View Attendance of Students')
    root56.geometry("1550x800+0+0")
    bg1 = ImageTk.PhotoImage(file="back2.jpg")
    lb_bg1 = Label(root56, image=bg1)
    lb_bg1.place(x=0, y=0, relwidth=1, relheight=1)
    def fetch():
        conn = mysql.connector.connect(
            host="localhost", user="root", passwd="admin123", database="testdb"
        )

        my_cursor = conn.cursor()
        my_cursor.execute("select * from attendance")
        data = my_cursor.fetchall()

        if len(data) != 0:
            student1_table.delete(*student1_table.get_children())
            for i in data:
                student1_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    search_box_frame = Frame(root56, bd=2, relief=RIDGE, bg="white")
    search_box_frame.place(x=55, y=160, width=1400, height=528)

    x_scroll = Scrollbar(search_box_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(search_box_frame, orient=VERTICAL)

    student1_table = ttk.Treeview(search_box_frame,
                                  column=(
                                      "Name", "Department", "roll", "Id", "Div", "Date", "Time", "Status"),
                                  xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)

    x_scroll.config(command=student1_table.xview)
    y_scroll.config(command=student1_table.yview)

    student1_table.heading("Name", text="Name")
    student1_table.heading("Department", text="roll")
    student1_table.heading("roll", text="roll")
    student1_table.heading("Id", text="Id")
    student1_table.heading("Div", text="Div")
    student1_table.heading("Date", text="Date")
    student1_table.heading("Time", text="Time")
    student1_table.heading("Status", text="Status")
    student1_table["show"] = "headings"

    student1_table.column("Name", width=150)
    student1_table.column("Department", width=150)
    student1_table.column("roll", width=200)
    student1_table.column("Id", width=150)
    student1_table.column("Div", width=150)
    student1_table.column("Date", width=150)
    student1_table.column("Time", width=200)
    student1_table.column("Status", width=200)


    student1_table.pack(fill=BOTH, expand=1)
    # student1_table.bind("<ButtonRelease>", focus_cursor)
    fetch()
    root56.mainloop()

