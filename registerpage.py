from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox






def register():
    global root2
    global fname_label
    global fname_entry
    global lname_label
    global lname_entry
    global contact_label
    global contact_entry
    global email_label
    global email_entry
    global securityQ_label
    global combo_security
    global securityA_label
    global securityA_entry
    global password_label
    global password_entry
    global confpassword_label
    global confpassword_entry
    global checkbtn1
    global s
#-------------------------------------------------------------------

    def success_register():
        if fname_entry.get()=="" or lname_entry.get()=="" or contact_entry.get()=="" or email_entry.get()=="" or combo_security.get()=="Select" or securityA_entry.get()=="" or password_entry.get()=="" or confpassword_entry.get()=="":
            messagebox.showerror("Error", "Kindly fill all the details")

        elif password_entry.get()!= confpassword_entry.get():
            messagebox.showerror("Error", "password doesn't match")

        elif s.get()==0:
            messagebox.showerror("Error", "Please accept the terms and conditions")

        else:
            messagebox.showinfo("Success", "Your Registration was successful")




    root2 = Toplevel()
    root2.geometry("1550x800+0+0")
    root2.title("Registeration Page")

    bg = ImageTk.PhotoImage(file="students-in-classroom.jpg")
    lb_bg = Label(root2, image=bg)
    lb_bg.place(x=0, y=0, relwidth=1.1, relheight=1)
    lba = Label(root2, text="Student Registration", font=("times new roman", 45, "bold"), fg="white", bg="black")
    lba.place(x=500, y=90)

    rg_frame = Frame(root2, bg="black")
    rg_frame.place(x=350, y=200, width=800, height=500)
    # ----------------------------row 1--------------------------------------------------------------------------------------
    fname_label = Label(rg_frame, text="First Name", font=("times new roman", 20, "bold"), fg="white", bg="black")
    fname_label.place(x=30, y=60)

    fname_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    fname_entry.place(x=30, y=95, width=280)

    lname_label = Label(rg_frame, text="Last Name", font=("times new roman", 20, "bold"), fg="white", bg="black")
    lname_label.place(x=450, y=60)

    lname_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    lname_entry.place(x=450, y=95, width=280)
    # ---------------------------------Row 2 --------------------------------------------------------------------------------
    contact_label = Label(rg_frame, text="Contact No.", font=("times new roman", 20, "bold"), fg="white", bg="black")
    contact_label.place(x=30, y=150)

    contact_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    contact_entry.place(x=30, y=190, width=280)

    email_label = Label(rg_frame, text="Email", font=("times new roman", 20, "bold"), fg="white", bg="black")
    email_label.place(x=450, y=150)

    email_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    email_entry.place(x=450, y=190, width=280)
    # ---------------------------------Row 3 --------------------------------------------------------------------------------
    securityQ_label = Label(rg_frame, text="Select security Question", font=("times new roman", 20, "bold"), fg="white",
                      bg="black")
    securityQ_label.place(x=30, y=230)

    # rg_entry6 = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="white")
    # rg_entry6.place(x=30, y=270, width=280)

    combo_security = ttk.Combobox(rg_frame, font=("times new roman", 20, "bold"), state="readonly")
    combo_security["values"] = ("Select", "Your Birth Place", "Your First Friend", "Your Pet Name")
    combo_security.place(x=30, y=270, width=280)
    combo_security.current(0)

    securityA_label = Label(rg_frame, text="Security Answer", font=("times new roman", 20, "bold"), fg="white", bg="black")
    securityA_label.place(x=450, y=230)

    securityA_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    securityA_entry.place(x=450, y=270, width=280)

    # ---------------------------------Row 4 --------------------------------------------------------------------------------

    password_label = Label(rg_frame, text="Enter Password", font=("times new roman", 20, "bold"), fg="white",
                      bg="black")
    password_label.place(x=30, y=320)

    password_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    password_entry.place(x=30, y=350, width=280)

    confpassword_label = Label(rg_frame, text="Confirm Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
    confpassword_label.place(x=450, y=320)

    confpassword_entry = Entry(rg_frame, font=("times new roman", 20, "bold"), fg="black")
    confpassword_entry.place(x=450, y=350, width=280)

    s=IntVar()

    checkbtn1 = Checkbutton(rg_frame, text="I agree to the terms & conditions", font=("times new roman", 13, "bold"),
                            onvalue=1, offvalue=0, variable=s)
    checkbtn1.place(x=30, y=390)

    register_button = Button(rg_frame, text="Register", cursor="hand2", borderwidth=0,
                             font=("times new roman", 20, "bold"), fg="black", bg="white", activebackground="black", command=success_register)
    register_button.place(x=30, y=430, width=150)

    login_button = Button(rg_frame, text="Login", cursor="hand2", borderwidth=0,
                          font=("times new roman", 20, "bold"), fg="black", bg="white", activebackground="black")
    login_button.place(x=420, y=430, width=150)

    root2.mainloop()

