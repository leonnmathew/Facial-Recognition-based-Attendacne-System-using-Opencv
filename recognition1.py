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

def automatic_attendance():
    root43=Tk()
    root43.title("Attendance using facial recognition")
    root43.geometry("1550x800+0+0")
    bg1 = ImageTk.PhotoImage(file="back2.jpg")
    lb_bg1 = Label(root43, image=bg1)
    lb_bg1.place(x=0, y=0, relwidth=1, relheight=1)

    def convert():
        with open('attendance.csv', 'r') as csv_file:
            conn9 = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
            my_cursor = conn9.cursor()
            my_cursor.execute("TRUNCATE TABLE attendance")
            csv_reader = csv.reader(csv_file)
            now = datetime.now()
            dvname = "attendance" + now.strftime("%d/%m/%y")

            next(csv_reader)

            for line in csv_reader:
                try:
                    my_cursor.execute("insert into attendance values (%s,%s,%s,%s,%s,%s,%s,%s)",
                                      (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))
                    conn9.commit()

                    print(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                except Exception as e:
                    print(e)
        print("Attendance Stored in Database Successfully")
        conn9.close()

    def mark_attendance(name, dep, roll, idiu2, div, d1):
        with open("attendance.csv", "r+", newline="\n") as f:
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((name not in name_list) and (dep not in name_list) and (roll not in name_list) and (
                    idiu2 not in name_list)):
                now = datetime.now()
                # d1=now.strftime("%d/%m/%y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{name},{dep},{roll},{idiu2},{div},{d1},{dtstring},present")

    def face_recog():
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coordinates = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id2, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn7 = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
                cursor7 = conn7.cursor()

                cursor7.execute("select name from student where Id=" + str(id2))
                n = cursor7.fetchone()
                name = "+".join(map(str, n))
                # print(name)

                cursor7.execute("select department from student where Id=" + str(id2))
                d = cursor7.fetchone()
                dep = "+".join(map(str, d))
                # print(dep)

                cursor7.execute("select divison from student where Id=" + str(id2))
                di = cursor7.fetchone()
                div = "+".join(map(str, di))
                # print(dep)

                cursor7.execute("select rollno from student where Id=" + str(id2))
                r = cursor7.fetchone()
                roll = "+".join(map(str, r))
                # print(roll)

                cursor7.execute("select Id from student where Id=" + str(id2))
                idu1 = cursor7.fetchone()
                idiu2 = "+".join(map(str, idu1))

                if confidence > 77:
                    cv2.putText(img, f" ID:{idiu2}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255.255), 2)
                    cv2.putText(img, f"Name:{name}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255.255), 2)
                    cv2.putText(img, f"Department:{dep}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(img, f"RollNo:{roll}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%y")
                    mark_attendance(name, dep, roll, idiu2, div, d1)
                    # dictu={"name":name,"Department":dep, "RollNo":roll}


                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                # cursor7.execute("insert into attendance values (%s,%s,%s)",(name,dep,roll))

                coordinates = [x, y, w, y]

            return coordinates

        def recognize(img, clf, faceCascade):
            coordinates = draw_boundary(img, faceCascade, 1.2, 5, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


    automatic_attendance_button=Button(root43,text="Automatic Attendance using Face Recognition")
    automatic_attendance_button.pack()
    root43.mainloop()

automatic_attendance()