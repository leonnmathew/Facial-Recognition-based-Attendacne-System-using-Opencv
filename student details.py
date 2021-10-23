from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


def student_details():
    root3 = Tk()
    root3.title("Student Details")
    root3.geometry("1550x800+0+0")

    bg1 = ImageTk.PhotoImage(file="aSAF.jpg")
    lb_bg1 = Label(root3, image=bg1)
    lb_bg1.place(x=0, y=0, relwidth=1, relheight=1)
    frame1 = Frame(root3, bg="white")
    frame1.place(x=0, y=0, width=2000, height=100)
    intro_label = Label(frame1, text="Student Details", font=("times new roman", 55, "bold"),
                        fg="black", bg="white")
    intro_label.place(x=500, y=10)

    main_frame = Frame(root3, bg="white")
    main_frame.place(x=4, y=120, width=2000, height=670)
    #--------------------------------left frame-------------------------------------------------------------------------
    left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, font=("times new roman", 12, "bold"),
                            bg="white")
    left_frame.place(x=10, y=10, width=780, height=650)

    label_info = Label(left_frame, text="Student Details", font=("times new roman", 25, "bold"), bg="white")
    label_info.grid(row=0, column=1, padx=5, pady=5, sticky=W)
#-------------------row 1--------------------------------------------------------------------------------------------
    department_info=Label(left_frame, text="Department:", font=("times new roman", 18, "bold"), bg="white")
    department_info.grid(row=1, column=0)

    department_info_combobox= ttk.Combobox(left_frame, font=("times new roman", 18, "bold"), state="readonly")
    department_info_combobox["values"] = ("Select Department", "Bsc-I.T", "Bsc-C.S")
    department_info_combobox.grid(row=1, column=1, padx=3, pady=3, sticky=W)
    department_info_combobox.current(0)
    #
    year_info = Label(left_frame, text="Year:", font=("times new roman", 18, "bold"), bg="white")
    year_info.grid(row=1, column=2, padx=3, pady=3, sticky=W)

    year_info_combobox = ttk.Combobox(left_frame, font=("times new roman", 18, "bold"), state="readonly")
    year_info_combobox["values"] = ("Select Year", "FY", "SY", "TY")
    year_info_combobox.grid(row=1, column=3, padx=3, pady=3, sticky=W)
    year_info_combobox.current(0)
#---------------------------------row2-----------------------------------------------------------------------------
    name_info = Label(left_frame, text="Name:", font=("times new roman", 18, "bold"), bg="white")
    name_info.grid(row=2, column=0, padx=3, pady=3, sticky=W)

    name_info_entry = Entry(left_frame, font=("times new roman", 18, "bold"), fg="black", bg="white")
    name_info_entry.grid(row=2, column=1, padx=3, pady=3, sticky=W)

    class_Divison_info = Label(left_frame, text="Division:", font=("times new roman", 18, "bold"), bg="white")
    class_Divison_info.grid(row=2, column=2, padx=3, pady=3, sticky=W)

    Divison_info_combobox = ttk.Combobox(left_frame, font=("times new roman", 18, "bold"), state="readonly")
    Divison_info_combobox["values"] = ("Select", "A", "B")
    Divison_info_combobox.grid(row=2, column=3, padx=3, pady=3, sticky=W)
    Divison_info_combobox.current(0)
#---------------------------------row3-------------------------------------------------------------------------------
    class_rollno_info = Label(left_frame, text="Roll No:", font=("times new roman", 17, "bold"), bg="white")
    class_rollno_info.grid(row=3, column=0, padx=5, pady=15, sticky=W)

    class_rollno_entry = Entry(left_frame, font=("times new roman", 17, "bold"), bg="white")
    class_rollno_entry.grid(row=3, column=1, padx=2, pady=15, sticky=W)

    DOB_info = Label(left_frame, text="DOB:", font=("times new roman", 17, "bold"), bg="white")
    DOB_info.grid(row=3, column=2, padx=5, pady=15, sticky=W)

    DOB_entry = Entry(left_frame, font=("times new roman", 17, "bold"), bg="white")
    DOB_entry.grid(row=3, column=3, padx=5, pady=15, sticky=W)
#---------------------------row 4--------------------------------------------------------------------------------
    # Mobileno_info = Label(left_frame, text="Mobile No:", font=("times new roman", 20, "bold"), bg="white")
    # Mobileno_info.place(x=10, y=480)
    #
    # Mobileno_entry = Entry(left_frame, font=("times new roman", 20, "bold"), bg="white")
    # Mobileno_entry.place(x=150, y=480, width=280)
    #
    # email_info = Label(left_frame, text="Email ID:", font=("times new roman", 20, "bold"), bg="white")
    # email_info.place(x=10, y=540)
    #
    # email_entry = Entry(left_frame, font=("times new roman", 20, "bold"), bg="white")
    # email_entry.place(x=150, y=540, width=280)
#---------------------------------------row 5----------------------------------------------------------------
    # Gender_info = Label(left_frame, text="Gender:", font=("times new roman", 20, "bold"), bg="white")
    # Gender_info.place(x=10, y=590)
    #
    # Gender_info_combobox = ttk.Combobox(left_frame, font=("times new roman", 20, "bold"), state="readonly")
    # Gender_info_combobox["values"] = ("Select", "Male", "Female")
    # Gender_info_combobox.place(x=150, y=590, width=200)
    # Gender_info_combobox.current(0)










    # right frame
    right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,
                             font=("times new roman", 12, "bold"),
                             bg="white")
    right_frame.place(x=800, y=10, width=710, height=650)

    root3.mainloop()


student_details()
