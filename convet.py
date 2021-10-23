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

def convert():
    filename = datetime.now().strftime('Attendance-%Y-%m-%d.csv')
    with open(filename, 'r') as csv_file:
        conn9 = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
        my_cursor = conn9.cursor()
        my_cursor.execute("TRUNCATE TABLE attendance")
        csv_reader = csv.reader(csv_file)
        now=datetime.now()
        dvname="attendance"+now.strftime("%d/%m/%y")

        next(csv_reader)

        for line in csv_reader:
            try:
                my_cursor.execute("insert into attendance values (%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))
                conn9.commit()

                # print(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
            except Exception as e:
                print(e)
    print("Attendance Stored in Database Successfully")
    conn9.close()




convert()




