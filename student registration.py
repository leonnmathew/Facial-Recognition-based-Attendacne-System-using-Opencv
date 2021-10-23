from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


def student_details1():
    root4 = Toplevel()
    root4.title("Student Details")
    root4.geometry("1550x800+0+0")

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

    first_label=Label(left_frame, text="Students Details",font=("times new roman", 25, "bold"), bg="white", fg="black")
    first_label.place(x=250, y=10)

    info_frame_label=Frame(left_frame, bd=2, relief=RIDGE,  bg="white")
    info_frame_label.place(x=5,y=60, width=770, height=350)

    #
    Department_Label=Label(info_frame_label, text="Department:",font=("times new roman", 18, "bold"), bg="white", fg="black")
    Department_Label.grid(row=0, column=0, padx=1, pady=20)

    department_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly")
    department_combobox["values"] = ("Select Department", "Bsc-I.T", "Bsc-C.S")
    department_combobox.grid(row=0, column=1, pady=20)
    department_combobox.current(0)
#
    Year_Label = Label(info_frame_label, text="Year:", font=("times new roman", 18, "bold"), bg="white",
                             fg="black")
    Year_Label.grid(row=0, column=2, padx=1 , pady=20)

    Year_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly")
    Year_combobox["values"] = ("Select", "FY", "SY", "TY")
    Year_combobox.grid(row=0, column=3 , pady=20)
    Year_combobox.current(0)
#
    Name_Label = Label(info_frame_label, text="Name:", font=("times new roman", 18, "bold"), bg="white",
                             fg="black")
    Name_Label.grid(row=1, column=0, padx=1, pady=10)

    Name_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white")
    Name_entry.grid(row=1, column=1, pady=20)

    Rollno_Label = Label(info_frame_label, text="Roll No:", font=("times new roman", 18, "bold"), bg="white",
                       fg="black")
    Rollno_Label.grid(row=1, column=2, pady=20)

    Rollno_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white")
    Rollno_entry.grid(row=1, column=3, pady=20)
# #----------------------------------------row 3-----------------------------------------------------------------
    Divison_Label = Label(info_frame_label, text="Divison:", font=("times new roman", 18, "bold"), bg="white",
                         fg="black")
    Divison_Label.grid(row=2, column=0, pady=20)

    Divison_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly")
    Divison_combobox["values"] = ("Select", "A", "B")
    Divison_combobox.grid(row=2, column=1 , pady=20)
    Divison_combobox.current(0)

    Gender_Label = Label(info_frame_label, text="Gender:", font=("times new roman", 18, "bold"), bg="white",
                          fg="black")
    Gender_Label.grid(row=2, column=2 , pady=20)

    Gender_combobox = ttk.Combobox(info_frame_label, font=("times new roman", 18, "bold"), state="readonly")
    Gender_combobox["values"] = ("Select", "Male", "Female")
    Gender_combobox.grid(row=2, column=3 , pady=20)
    Gender_combobox.current(0)
#
# #---------------------------------row 4-----------------------------------------------------------------------
    Mobile_Label = Label(info_frame_label, text="Mobile:", font=("times new roman", 18, "bold"), bg="white",
                          fg="black")
    Mobile_Label.grid(row=3, column=0, pady=20)

    Mobile_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white")
    Mobile_entry.grid(row=3, column=1 , pady=20)

    email_Label = Label(info_frame_label, text="Email:", font=("times new roman", 18, "bold"), bg="white",
                         fg="black")
    email_Label.grid(row=3, column=2, pady=20)

    email_entry = Entry(info_frame_label, font=("times new roman", 18, "bold"), fg="black", bg="white")
    email_entry.grid(row=3, column=3, pady=20)

    down_frame_label = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
    down_frame_label.place(x=5, y=420, width=770, height=220)

    save_button=Button(down_frame_label, text="Save", width=20,height=4,font=("times new roman", 12, "bold"), bg="black", fg="white")
    save_button.grid(row=0, column=0)

    update_button = Button(down_frame_label, text="Update", width=20, height=4, font=("times new roman", 12, "bold"),
                         bg="black", fg="white")
    update_button.grid(row=0, column=1)

    delete_button = Button(down_frame_label, text="Delete", width=20, height=4, font=("times new roman", 12, "bold"),
                         bg="black", fg="white")
    delete_button.grid(row=0, column=2)

    reset_button = Button(down_frame_label, text="Reset", width=21, height=4, font=("times new roman", 12, "bold"),
                         bg="black", fg="white")
    reset_button.grid(row=0, column=3)

    down2_frame_label = Frame(down_frame_label, bd=2, relief=RIDGE, bg="white")
    down2_frame_label.place(x=0, y=90, width=760, height=125)


    take_image_button = Button(down2_frame_label, text="Take Image", width=42, height=6, font=("times new roman", 12, "bold"),
                         bg="black", fg="white")
    take_image_button.grid(row=0, column=0)

    update_image_button = Button(down2_frame_label, text="Update Image", width=42, height=6,
                               font=("times new roman", 12, "bold"),
                               bg="black", fg="white")
    update_image_button.grid(row=0, column=1)









    # ---------------------------------------- -right frame--------------------------------------------------------------
    right_frame = Frame(main_frame, bd=2, relief=RIDGE,  bg="white")
    right_frame.place(x=800, y=10, width=710, height=650)

    #------------------------------------------Search System------------------------------------------------------------
    search_frame=Frame(right_frame,bd=2, relief=RIDGE, bg="white")
    search_frame.place(x=2, y=5, width=700, height=100)

    search_by_label=Label(search_frame, text="Search By:", font=("times new roman", 18, "bold"), bg="white", fg="black")
    search_by_label.grid(row=0, column=0, pady=25)

    searchby_combobox = ttk.Combobox(search_frame,width=10,height=10, font=("times new roman", 18, "bold"), state="readonly")
    searchby_combobox["values"] = ("Select", "Roll no", "Phone No")
    searchby_combobox.grid(row=0, column=1, pady=25)
    searchby_combobox.current(0)

    search_entry = Entry(search_frame,width=12 ,font=("times new roman", 18, "bold"), fg="black", bg="white")
    search_entry.grid(row=0, column=2,padx=4 ,pady=25)
    #
    search_button = Button(search_frame, text="Search", width=13,
                               font=("times new roman", 12, "bold"),
                               bg="black", fg="white")
    search_button.grid(row=0, column=3,padx=4 ,pady=25)

    show_all_button = Button(search_frame, text="Show All", width=13,
                           font=("times new roman", 12, "bold"),
                           bg="black", fg="white")
    show_all_button.grid(row=0, column=5,padx=4 ,pady=25)

    search_box_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
    search_box_frame.place(x=2, y=110, width=700, height=528)

    x_scroll = Scrollbar(search_box_frame, orient=HORIZONTAL)
    y_scroll = Scrollbar(search_box_frame, orient=VERTICAL)

    student1_table=ttk.Treeview(search_box_frame, column=("Dep","year","name","roll no","Divison","Gender","Mobile","email"), xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

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
    student1_table["show"]="headings"

    student1_table.column("Dep", width=150)
    student1_table.column("year", width=150)
    student1_table.column("name", width=200)
    student1_table.column("roll no", width=150)
    student1_table.column("Divison", width=150)
    student1_table.column("Gender", width=150)
    student1_table.column("Mobile", width=200)
    student1_table.column("email", width=200)


    student1_table.pack(fill=BOTH, expand=1)








    root4.mainloop()


# student_details1()
