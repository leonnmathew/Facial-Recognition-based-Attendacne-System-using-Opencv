from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



def student_details1():
    root4 = Toplevel()
    root4.title("Student Details")
    root4.geometry("1550x800+0+0")

    dep_var = tk.StringVar()
    year_var = tk.StringVar()
    name_var = tk.StringVar()
    rollno_var = tk.StringVar()
    div_var = tk.StringVar()
    gender_var = tk.StringVar()
    mobile_var = tk.StringVar()
    email_var = tk.StringVar()
    Id_var = tk.StringVar()

    def fetch():
        conn = mysql.connector.connect(
            host="localhost", user="root", passwd="admin123", database="testdb"
        )

        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            student1_table.delete(*student1_table.get_children())
            for i in data:
                student1_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def save():
        if dep_var.get() == "Select Department" or year_var.get() == "Select" or name_var.get() == "" or rollno_var.get() == "" or div_var.get() == "Select" or gender_var.get() == "Select" or mobile_var.get() == "" or email_var.get() == "" or Id_var.get() == "":
            messagebox.showerror("Error", "Kindly fill all the details to successfuly Register your details",
                                 parent=root4)
        #
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", passwd="admin123", database="testdb"
                )
                #
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (dep_var.get(),
                                   year_var.get(),
                                   name_var.get(),
                                   rollno_var.get(),
                                   div_var.get(),
                                   gender_var.get(),
                                   mobile_var.get(),
                                   email_var.get(),
                                   Id_var.get()))
                conn.commit()
                fetch()
                conn.close()
                messagebox.showinfo("Success", "Details successfully registered", parent=root4)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=root4)

    def focus_cursor(event=""):
        cursor_focus = student1_table.focus()
        content = student1_table.item(cursor_focus)
        data = content["values"]

        dep_var.set(data[0]),
        year_var.set(data[1]),
        name_var.set(data[2]),
        rollno_var.set(data[3]),
        div_var.set(data[4]),
        gender_var.set(data[5]),
        mobile_var.set(data[6]),
        email_var.set(data[7]),
        Id_var.set(data[8])

    def update_details():
        global conn1
        if dep_var.get() == "Select Department" or year_var.get() == "Select" or name_var.get() == "" or rollno_var.get() == "" or div_var.get() == "Select" or gender_var.get() == "Select" or mobile_var.get() == "" or email_var.get() == "" or Id_var.get() == "":
            messagebox.showerror("Error", "Kindly fill all the details to successfuly Register your details", parent=root4)
        else:
            try:
                update_message = messagebox.askyesno("update", "Do you want to update this student's details", parent=root4)
                if update_message > 0:
                    conn1=mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
                    my_cursor=conn1.cursor()
                    my_cursor.execute("update student set department=%s,year=%s,name=%s,rollno=%s,divison=%s,gender=%s,mobile=%s,email=%s where Id=%s",(dep_var.get(),year_var.get(),name_var.get(),rollno_var.get(),div_var.get(),gender_var.get(),mobile_var.get(),email_var.get(),Id_var.get()))
                else:
                    if not update_message:
                        return
                messagebox.showinfo("success","Update done successfully!", parent=root4)
                conn1.commit()
                fetch()
                conn1.close()

            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=root4)

            #         conn = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
            #         my_cursor = conn.cursor()
            #         my_cursor.execute(
            #             "update student set department=%s,year=%s,name=%s,rollno=%s,divison=%s,gender=%s,mobile=%s,"
            #             "email=%s where Id=%s",
            #             (dep_var.get(),
            #              year_var.get(),
            #              name_var.get(),
            #              rollno_var.get(),
            #              div_var.get(),
            #              gender_var.get(),
            #              mobile_var.get(),
            #              email_var.get(),
            #              Id_var.get()))
            #     else:
            #         if not update_message:
            #             return
            #     messagebox.showinfo("success", "Student details updated sucessfully!", parent=root4)
            #     conn.commit()
            #
            #
            # except Exception as es:
            #     messagebox.showerror("error", f"Due to:{str(es)}", parent=root4)

    def delete_details():
        global conn2
        if Id_var.get()=="":
            messagebox.showerror("Error","Student Id must be required", parent=root4)
        else:
            try:
                delete_message=messagebox.askyesno("Delete","Do you want to delete this detail", parent=root4)
                if delete_message>0:
                    conn2=mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
                    my_cursor=conn2.cursor()
                    sql="delete from student where Id=%s"
                    val=(Id_var.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete_message:
                        return

                conn2.commit()
                fetch()
                conn2.close()
                messagebox.showinfo("Delete", "Delete operation done successfully!", parent=root4)
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=root4)

    def reset_details():
        dep_var.set("Select Department")
        year_var.set("Select")
        name_var.set("")
        rollno_var.set("")
        div_var.set("Select")
        gender_var.set("Select")
        mobile_var.set("")
        email_var.set("")
        Id_var.set("")


    def generate_dataset():
        global conn4
        if dep_var.get() == "Select Department" or year_var.get() == "Select" or name_var.get() == "" or rollno_var.get() == "" or div_var.get() == "Select" or gender_var.get() == "Select" or mobile_var.get() == "" or email_var.get() == "" or Id_var.get() == "":
            messagebox.showerror("Error", "Kindly fill all the details to successfuly Register your details", parent=root4)

        else:
            try:
                conn4 = mysql.connector.connect(host="localhost", user="root", passwd="admin123", database="testdb")
                my_cursor = conn4.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                Idi=0
                for x in my_result:
                    Idi+=1
                my_cursor.execute("update student set department=%s,year=%s,name=%s,rollno=%s,divison=%s,gender=%s,mobile=%s,email=%s where Id=%s",(dep_var.get(), year_var.get(), name_var.get(), rollno_var.get(), div_var.get(), gender_var.get(), mobile_var.get(), email_var.get(), Id_var.get()==Idi+1))
                conn4.commit()
                fetch()
                reset_details()
                conn4.close()

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped1=img[y:y+h,x:x+w]
                        return face_cropped1

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read(0)
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(500,500),interpolation=cv2.INTER_AREA)
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_path="dataset/user."+str(Idi)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face", face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("sucess","Dataset Generated",parent=root4)
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=root4)

    def train_images():
        data_directory = ("dataset")
        path = [os.path.join(data_directory, file) for file in os.listdir(data_directory)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # conversion to grayscale
            imageNp = np.array(img, 'uint8')
            idiu = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(idiu)
            cv2.imshow("Training Window", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result", "Training Completed!",parent=root4)




















    bg1 = ImageTk.PhotoImage(file="aSAF.jpg")
    lb_bg1 = Label(root4, image=bg1)
    lb_bg1.place(x=0, y=0, relwidth=1, relheight=1)
    frame1 = Frame(root4, bg="white")
    frame1.place(x=0, y=0, width=2000, height=100)
    intro_label = Label(frame1, text="Student Registration", font=("times new roman", 55, "bold"),
                        fg="black", bg="white")
    intro_label.place(x=490, y=10)

    main_frame = Frame(root4, bg="white")
    main_frame.place(x=4, y=120, width=2000, height=670)
    # --------------------------------left frame-------------------------------------------------------------------------
    left_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
    left_frame.place(x=10, y=10, width=780, height=650)

    first_label = Label(left_frame, text="Students Details", font=("times new roman", 25, "bold"), bg="white",
                        fg="black")
    first_label.place(x=250, y=10)

    info_frame_label = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
    info_frame_label.place(x=5, y=60, width=770, height=350)

    #
    Department_Label = Label(info_frame_label, text="Department:", font=("times new roman", 18, "bold"), bg="white",
                             fg="black")
    Department_Label.grid(row=0, column=0, padx=1, pady=20)

    department_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly",
                                       textvariable=dep_var)
    department_combobox["values"] = ("Select Department", "Bsc-I.T", "Bsc-C.S")
    department_combobox.grid(row=0, column=1, pady=20)
    department_combobox.current(0)
    #
    Year_Label = Label(info_frame_label, text="Year:", font=("times new roman", 18, "bold"), bg="white",
                       fg="black")
    Year_Label.grid(row=0, column=2, padx=1, pady=20)

    Year_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly",
                                 textvariable=year_var)
    Year_combobox["values"] = ("Select", "FY", "SY", "TY")
    Year_combobox.grid(row=0, column=3, pady=20)
    Year_combobox.current(0)
    #
    Name_Label = Label(info_frame_label, text="Name:", font=("times new roman", 18, "bold"), bg="white",
                       fg="black")
    Name_Label.grid(row=1, column=0, padx=1, pady=10)

    Name_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white",
                       textvariable=name_var)
    Name_entry.grid(row=1, column=1, pady=20)

    Rollno_Label = Label(info_frame_label, text="Roll No:", font=("times new roman", 18, "bold"), bg="white",
                         fg="black")
    Rollno_Label.grid(row=1, column=2, pady=20)

    Rollno_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white",
                         textvariable=rollno_var)
    Rollno_entry.grid(row=1, column=3, pady=20)
    # #----------------------------------------row 3-----------------------------------------------------------------
    Divison_Label = Label(info_frame_label, text="Divison:", font=("times new roman", 18, "bold"), bg="white",
                          fg="black")
    Divison_Label.grid(row=2, column=0, pady=20)

    Divison_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly",
                                    textvariable=div_var)
    Divison_combobox["values"] = ("Select", "A", "B")
    Divison_combobox.grid(row=2, column=1, pady=20)
    Divison_combobox.current(0)

    Gender_Label = Label(info_frame_label, text="Gender:", font=("times new roman", 18, "bold"), bg="white",
                         fg="black")
    Gender_Label.grid(row=2, column=2, pady=20)

    Gender_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly",
                                   textvariable=gender_var)
    Gender_combobox["values"] = ("Select", "Male", "Female")
    Gender_combobox.grid(row=2, column=3, pady=20)
    Gender_combobox.current(0)

    #
    # #---------------------------------row 4-----------------------------------------------------------------------
    Mobile_Label = Label(info_frame_label, text="Mobile:", font=("times new roman", 18, "bold"), bg="white",
                         fg="black")
    Mobile_Label.grid(row=3, column=0, pady=20)

    Mobile_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white",
                         textvariable=mobile_var)
    Mobile_entry.grid(row=3, column=1, pady=20)

    email_Label = Label(info_frame_label, text="Email:", font=("times new roman", 18, "bold"), bg="white",
                        fg="black")
    email_Label.grid(row=3, column=2, pady=20)

    email_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white",
                        textvariable=email_var)
    email_entry.grid(row=3, column=3, pady=20)

    Id_Label = Label(info_frame_label, text="ID:", font=("times new roman", 18, "bold"), bg="white",
                     fg="black")
    Id_Label.grid(row=4, column=0, pady=20)
    Id_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white",
                     textvariable=Id_var)
    Id_entry.grid(row=4, column=1, pady=20)

    down_frame_label = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
    down_frame_label.place(x=5, y=420, width=770, height=220)

    save_button = Button(down_frame_label, text="Save", width=20, height=4,
                         font=("times new roman", 12, "bold"), bg="black", fg="white", command=save)
    save_button.grid(row=0, column=0)

    update_button = Button(down_frame_label, text="Update", width=20, height=4, font=("times new roman", 12, "bold"),
                           bg="black", fg="white", command=update_details)
    update_button.grid(row=0, column=1)

    delete_button = Button(down_frame_label, text="Delete", width=20, height=4, font=("times new roman", 12, "bold"),
                           bg="black", fg="white", command=delete_details)
    delete_button.grid(row=0, column=2)

    reset_button = Button(down_frame_label, text="Reset", width=21, height=4, font=("times new roman", 12, "bold"),
                          bg="black", fg="white", command=reset_details)
    reset_button.grid(row=0, column=3)

    down2_frame_label = Frame(down_frame_label, bd=2, relief=RIDGE, bg="white")
    down2_frame_label.place(x=0, y=90, width=760, height=125)

    take_image_button = Button(down2_frame_label, text="Take Image", width=42, height=6,
                               font=("times new roman", 12, "bold"),
                               bg="black", fg="white", command=generate_dataset)
    take_image_button.grid(row=0, column=0)

    update_image_button = Button(down2_frame_label, text="Train Images", width=42, height=6,
                                 font=("times new roman", 12, "bold"),
                                 bg="black", fg="white", command=train_images)
    update_image_button.grid(row=0, column=1)

    # ---------------------------------------- -right frame--------------------------------------------------------------
    right_frame = Frame(main_frame, bd=2, relief=RIDGE, bg="white")
    right_frame.place(x=800, y=10, width=710, height=650)

    # ------------------------------------------Search System------------------------------------------------------------
    search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
    search_frame.place(x=2, y=5, width=700, height=100)

    search_by_label = Label(search_frame, text="Search By:", font=("times new roman", 18, "bold"), bg="white",
                            fg="black")
    search_by_label.grid(row=0, column=0, pady=25)

    searchby_combobox = ttk.Combobox(search_frame, width=10, height=10, font=("times new roman", 18, "bold"),
                                     state="readonly")
    searchby_combobox["values"] = ("Select", "Roll no", "Phone No")
    searchby_combobox.grid(row=0, column=1, pady=25)
    searchby_combobox.current(0)

    search_entry = Entry(search_frame, width=12, font=("times new roman", 18, "bold"), fg="black", bg="white")
    search_entry.grid(row=0, column=2, padx=4, pady=25)
    #
    search_button = Button(search_frame, text="Search", width=13,
                           font=("times new roman", 12, "bold"),
                           bg="black", fg="white")
    search_button.grid(row=0, column=3, padx=4, pady=25)

    show_all_button = Button(search_frame, text="Show All", width=13,
                             font=("times new roman", 12, "bold"),
                             bg="black", fg="white")
    show_all_button.grid(row=0, column=5, padx=4, pady=25)

    search_box_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
    search_box_frame.place(x=2, y=110, width=700, height=528)

    x_scroll = Scrollbar(search_box_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(search_box_frame, orient=VERTICAL)

    student1_table = ttk.Treeview(search_box_frame,
                                  column=(
                                      "Dep", "year", "name", "roll no", "Divison", "Gender", "Mobile", "email", "Id"),
                                  xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

    x_scroll.pack(side=BOTTOM, fill=X)
    y_scroll.pack(side=RIGHT, fill=Y)

    x_scroll.config(command=student1_table.xview)
    y_scroll.config(command=student1_table.yview)

    student1_table.heading("Dep", text="Department")
    student1_table.heading("year", text="Year")
    student1_table.heading("name", text="Name")
    student1_table.heading("roll no", text="Roll No.")
    student1_table.heading("Divison", text="Divison")
    student1_table.heading("Gender", text="Gender")
    student1_table.heading("Mobile", text="Mobile")
    student1_table.heading("email", text="Email")
    student1_table.heading("Id", text="Id")
    student1_table["show"] = "headings"

    student1_table.column("Dep", width=150)
    student1_table.column("year", width=150)
    student1_table.column("name", width=200)
    student1_table.column("roll no", width=150)
    student1_table.column("Divison", width=150)
    student1_table.column("Gender", width=150)
    student1_table.column("Mobile", width=200)
    student1_table.column("email", width=200)
    student1_table.column("Id", width=200)

    student1_table.pack(fill=BOTH, expand=1)
    student1_table.bind("<ButtonRelease>", focus_cursor)
    fetch()

    root4.mainloop()

