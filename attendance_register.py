from future.moves.tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from datetime import *


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Register")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Attendance Register", bd=10, relief=GROOVE, font=("impact", 30, "bold"),
                      bg="crimson", fg="white")
        title.pack(side=TOP, fill=X)
        # *************** All Variable *************** #
        self.attendance_date = StringVar()
        self.attendance_time = StringVar()
        self.attendance_day = StringVar()
        self.rollNo1 = StringVar()
        self.rollNo2 = StringVar()
        self.rollNo3 = StringVar()
        self.rollNo4 = StringVar()
        self.rollNo5 = StringVar()
        self.rollNo6 = StringVar()
        self.rollNo7 = StringVar()
        self.rollNo8 = StringVar()
        self.rollNo9 = StringVar()
        self.rollNo10 = StringVar()
        self.rollNo11 = StringVar()

        # *************** Day, Date and Time Frame *************** #
        DDT_Frame = Frame(self.root, bd=7, relief=RIDGE)
        DDT_Frame.place(x=20, y=80, width=1320, height=70)

        # Day
        day = datetime.now()
        self.format_day = day.strftime("%A")
        day_lbl1 = Label(DDT_Frame, text="Day:", font=("times new roman", 16, "bold"))
        day_lbl1.grid(row=0, column=0, padx=60, pady=10, sticky="w")
        day_lbl2 = Label(DDT_Frame, text=self.format_day, font=("times new roman", 20, "bold"), bg="black", fg="white")
        day_lbl2.grid(row=0, column=1, padx=80, pady=10, sticky="w")

        # Date
        date = datetime.now()
        self.format_date = f"{date:%b %d %Y}"
        date_lbl1 = Label(DDT_Frame, text="Date:", font=("times new roman", 16, "bold"))
        date_lbl1.grid(row=0, column=2, padx=30, pady=10, sticky="w")
        date_lbl2 = Label(DDT_Frame, text=self.format_date, font=("times new roman", 20, "bold"), bg="black",
                          fg="white")
        date_lbl2.grid(row=0, column=3, padx=80, pady=10, sticky="w")

        # Time
        time = datetime.now()
        self.format_time = time.strftime("%I:%M:%S")
        time_lbl1 = Label(DDT_Frame, text="Time:", font=("times new roman", 16, "bold"))
        time_lbl1.grid(row=0, column=4, padx=30, pady=10, sticky="w")
        time_lbl2 = Label(DDT_Frame, text=self.format_time, font=("times new roman", 20, "bold"), bg="black",
                          fg="white")
        time_lbl2.grid(row=0, column=5, padx=80, pady=10, sticky="w")

        self.attendance_day.set(self.format_day)
        self.attendance_date.set(self.format_date)
        self.attendance_time.set(self.format_time)

        # *************** Attendance Frame *************** #
        Attendance_Frame = Frame(self.root, bd=7, relief=RIDGE)
        Attendance_Frame.place(x=20, y=150, width=1320, height=420)

        # ******* Roll Number ******* #
        rollNo_lbl = Label(Attendance_Frame, text="Roll Number", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=5)
        rollNo1_lbl = Label(Attendance_Frame, text="1", font=("arial 15")).grid(row=1, column=0, padx=5, pady=2)
        rollNo2_lbl = Label(Attendance_Frame, text="2", font=("arial 15")).grid(row=2, column=0, padx=5, pady=2)
        rollNo3_lbl = Label(Attendance_Frame, text="3", font=("arial 15")).grid(row=3, column=0, padx=5, pady=2)
        rollNo4_lbl = Label(Attendance_Frame, text="4", font=("arial 15")).grid(row=4, column=0, padx=5, pady=2)
        rollNo6_lbl = Label(Attendance_Frame, text="6", font=("arial 15")).grid(row=6, column=0, padx=5, pady=2)
        rollNo5_lbl = Label(Attendance_Frame, text="5", font=("arial 15")).grid(row=5, column=0, padx=5, pady=2)
        rollNo7_lbl = Label(Attendance_Frame, text="7", font=("arial 15")).grid(row=7, column=0, padx=5, pady=2)
        rollNo8_lbl = Label(Attendance_Frame, text="8", font=("arial 15")).grid(row=8, column=0, padx=5, pady=2)
        rollNo9_lbl = Label(Attendance_Frame, text="9", font=("arial 15")).grid(row=9, column=0, padx=5, pady=2)
        rollNo10_lbl = Label(Attendance_Frame, text="10", font=("arial 15")).grid(row=10, column=0, padx=5, pady=2)
        rollNo11_lbl = Label(Attendance_Frame, text="11", font=("arial 15")).grid(row=11, column=0, padx=5, pady=2)

        name_lbl = Label(Attendance_Frame, text="Student Name", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=5)
        name1_lbl = Label(Attendance_Frame, text="Akshita Bhadoria", font=("arial 15")).grid(row=1, column=1, padx=5,
                                                                                             pady=2, sticky="w")
        name2_lbl = Label(Attendance_Frame, text="Ankita Sharma", font=("arial 15")).grid(row=2, column=1, padx=5,
                                                                                          pady=2, sticky="w")
        name3_lbl = Label(Attendance_Frame, text="Kanta Sharma", font=("arial 15")).grid(row=3, column=1, padx=5,
                                                                                         pady=2, sticky="w")
        name4_lbl = Label(Attendance_Frame, text="Gourav Nama", font=("arial 15")).grid(row=4, column=1, padx=5, pady=2,
                                                                                        sticky="w")
        name5_lbl = Label(Attendance_Frame, text="Manish Sharma", font=("arial 15")).grid(row=5, column=1, padx=5,
                                                                                          pady=2, sticky="w")
        name6_lbl = Label(Attendance_Frame, text="Manish Jangir", font=("arial 15")).grid(row=6, column=1, padx=5,
                                                                                          pady=2, sticky="w")
        name7_lbl = Label(Attendance_Frame, text="Mansvi Gautam", font=("arial 15")).grid(row=7, column=1, padx=5,
                                                                                          pady=2, sticky="w")
        name8_lbl = Label(Attendance_Frame, text="Pooja Sharma", font=("arial 15")).grid(row=8, column=1, padx=5,
                                                                                         pady=2, sticky="w")
        name9_lbl = Label(Attendance_Frame, text="Sakshi Tamrkar", font=("arial 15")).grid(row=9, column=1, padx=5,
                                                                                           pady=2, sticky="w")
        name10_lbl = Label(Attendance_Frame, text="Sunil Jangir", font=("arial 15")).grid(row=10, column=1, padx=5,
                                                                                          pady=2, sticky="w")
        name11_lbl = Label(Attendance_Frame, text="Surbhi Ajmera", font=("arial 15")).grid(row=11, column=1, padx=5,
                                                                                           pady=2, sticky="w")

        stdId_lbl = Label(Attendance_Frame, text="Student ID", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                          column=2,
                                                                                                          padx=5)
        stdId1_lbl = Label(Attendance_Frame, text="19/MCA/IV/01", font=("arial 15")).grid(row=1, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId2_lbl = Label(Attendance_Frame, text="19/MCA/IV/02", font=("arial 15")).grid(row=2, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId3_lbl = Label(Attendance_Frame, text="19/MCA/IV/03", font=("arial 15")).grid(row=3, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId4_lbl = Label(Attendance_Frame, text="19/MCA/IV/04", font=("arial 15")).grid(row=4, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId5_lbl = Label(Attendance_Frame, text="19/MCA/IV/05", font=("arial 15")).grid(row=5, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId6_lbl = Label(Attendance_Frame, text="19/MCA/IV/06", font=("arial 15")).grid(row=6, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId7_lbl = Label(Attendance_Frame, text="19/MCA/IV/07", font=("arial 15")).grid(row=7, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId8_lbl = Label(Attendance_Frame, text="19/MCA/IV/08", font=("arial 15")).grid(row=8, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId9_lbl = Label(Attendance_Frame, text="19/MCA/IV/09", font=("arial 15")).grid(row=9, column=2, padx=5,
                                                                                          pady=2, sticky="w")
        stdId10_lbl = Label(Attendance_Frame, text="19/MCA/IV/10", font=("arial 15")).grid(row=10, column=2, padx=5,
                                                                                           pady=2, sticky="w")
        stdId11_lbl = Label(Attendance_Frame, text="19/MCA/IV/11", font=("arial 15")).grid(row=11, column=2, padx=5,
                                                                                           pady=2, sticky="w")

        email_lbl = Label(Attendance_Frame, text="Email Address", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                             column=3,
                                                                                                             padx=5)
        email1_lbl = Label(Attendance_Frame, text="Akshita1089@gmail.com", font=("arial 15")).grid(row=1, column=3,
                                                                                                   padx=5, pady=2,
                                                                                                   sticky="w")
        email2_lbl = Label(Attendance_Frame, text="ankitasharma302000@gmail.com", font=("arial 15")).grid(row=2,
                                                                                                          column=3,
                                                                                                          padx=5,
                                                                                                          pady=2,
                                                                                                          sticky="w")
        email3_lbl = Label(Attendance_Frame, text="Kantasharma1119@gmail.com", font=("arial 15")).grid(row=3, column=3,
                                                                                                       padx=5, pady=2,
                                                                                                       sticky="w")
        email4_lbl = Label(Attendance_Frame, text="gouravnama1101@gmail.com", font=("arial 15")).grid(row=4, column=3,
                                                                                                      padx=5, pady=2,
                                                                                                      sticky="w")
        email5_lbl = Label(Attendance_Frame, text="manish12.mca@gmail.com", font=("arial 15")).grid(row=5, column=3,
                                                                                                    padx=5, pady=2,
                                                                                                    sticky="w")
        email6_lbl = Label(Attendance_Frame, text="manishjangir770@gmail.com", font=("arial 15")).grid(row=6, column=3,
                                                                                                       padx=5, pady=2,
                                                                                                       sticky="w")
        email7_lbl = Label(Attendance_Frame, text="Maghagautam2222@gmail.com", font=("arial 15")).grid(row=7, column=3,
                                                                                                       padx=5, pady=2,
                                                                                                       sticky="w")
        email8_lbl = Label(Attendance_Frame, text="heenasharma1119@gmail.com", font=("arial 15")).grid(row=8, column=3,
                                                                                                       padx=5, pady=2,
                                                                                                       sticky="w")
        email9_lbl = Label(Attendance_Frame, text="Sakshitamrkar1224@gmail.com", font=("arial 15")).grid(row=9,
                                                                                                         column=3,
                                                                                                         padx=5, pady=2,
                                                                                                         sticky="w")
        email10_lbl = Label(Attendance_Frame, text="Suniljangir341514@gmail.com", font=("arial 15")).grid(row=10,
                                                                                                          column=3,
                                                                                                          padx=5,
                                                                                                          pady=2,
                                                                                                          sticky="w")
        email11_lbl = Label(Attendance_Frame, text="ajmerasurbhi0229@gmail.com", font=("arial 15")).grid(row=11,
                                                                                                         column=3,
                                                                                                         padx=5, pady=2,
                                                                                                         sticky="w")

        contact_lbl = Label(Attendance_Frame, text="Contact", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                         column=4,
                                                                                                         padx=5)
        contact1_lbl = Label(Attendance_Frame, text="+91961013XXXX", font=("arial 15")).grid(row=1, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact2_lbl = Label(Attendance_Frame, text="+91982857XXXX", font=("arial 15")).grid(row=2, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact3_lbl = Label(Attendance_Frame, text="+91978396XXXX", font=("arial 15")).grid(row=3, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact4_lbl = Label(Attendance_Frame, text="+91902355XXXX", font=("arial 15")).grid(row=4, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact5_lbl = Label(Attendance_Frame, text="+91856286XXXX", font=("arial 15")).grid(row=5, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact6_lbl = Label(Attendance_Frame, text="+91856286XXXX", font=("arial 15")).grid(row=6, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact7_lbl = Label(Attendance_Frame, text="+91979977XXXX", font=("arial 15")).grid(row=7, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact8_lbl = Label(Attendance_Frame, text="+91724060XXXX", font=("arial 15")).grid(row=8, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact9_lbl = Label(Attendance_Frame, text="+91808508XXXX", font=("arial 15")).grid(row=9, column=4, padx=5,
                                                                                             pady=2, sticky="w")
        contact10_lbl = Label(Attendance_Frame, text="+91967234XXXX", font=("arial 15")).grid(row=10, column=4, padx=5,
                                                                                              pady=2, sticky="w")
        contact11_lbl = Label(Attendance_Frame, text="+91637841XXXX", font=("arial 15")).grid(row=11, column=4, padx=5,
                                                                                              pady=2, sticky="w")

        attendance_lbl = Label(Attendance_Frame, text="Attendance", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                               column=5,
                                                                                                               padx=150)
        attendance1_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo1, font=("arial 15 bold"),
                                         state="readonly")
        attendance1_combo['values'] = ("Present", "Absent", "Leave")
        attendance1_combo.grid(row=1, column=5, padx=8, pady=2)
        attendance2_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo2, font=("arial 15 bold"),
                                         state="readonly")
        attendance2_combo['values'] = ("Present", "Absent", "Leave")
        attendance2_combo.grid(row=2, column=5, padx=8, pady=2)
        attendance3_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo3, font=("arial 15 bold"),
                                         state="readonly")
        attendance3_combo['values'] = ("Present", "Absent", "Leave")
        attendance3_combo.grid(row=3, column=5, padx=8, pady=2)
        attendance4_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo4, font=("arial 15 bold"),
                                         state="readonly")
        attendance4_combo['values'] = ("Present", "Absent", "Leave")
        attendance4_combo.grid(row=4, column=5, padx=8, pady=2)
        attendance5_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo5, font=("arial 15 bold"),
                                         state="readonly")
        attendance5_combo['values'] = ("Present", "Absent", "Leave")
        attendance5_combo.grid(row=5, column=5, padx=8, pady=2)
        attendance6_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo6, font=("arial 15 bold"),
                                         state="readonly")
        attendance6_combo['values'] = ("Present", "Absent", "Leave")
        attendance6_combo.grid(row=6, column=5, padx=8, pady=2)
        attendance7_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo7, font=("arial 15 bold"),
                                         state="readonly")
        attendance7_combo['values'] = ("Present", "Absent", "Leave")
        attendance7_combo.grid(row=7, column=5, padx=8, pady=2)
        attendance8_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo8, font=("arial 15 bold"),
                                         state="readonly")
        attendance8_combo['values'] = ("Present", "Absent", "Leave")
        attendance8_combo.grid(row=8, column=5, padx=8, pady=2)
        attendance9_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo9, font=("arial 15 bold"),
                                         state="readonly")
        attendance9_combo['values'] = ("Present", "Absent", "Leave")
        attendance9_combo.grid(row=9, column=5, padx=8, pady=2)
        attendance10_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo10, font=("arial 15 bold"),
                                          state="readonly")
        attendance10_combo['values'] = ("Present", "Absent", "Leave")
        attendance10_combo.grid(row=10, column=5, padx=8, pady=2)
        attendance11_combo = ttk.Combobox(Attendance_Frame, textvariable=self.rollNo11, font=("arial 15 bold"),
                                          state="readonly")
        attendance11_combo['values'] = ("Present", "Absent", "Leave")
        attendance11_combo.grid(row=11, column=5, padx=8, pady=2)

        # *************** Buttons Frame *************** #
        Button_Frame = Frame(self.root, bd=7, relief=RIDGE)
        Button_Frame.place(x=290, y=570, width=710, height=100)

        # Buttons
        add_button = Button(Button_Frame, text="Add", command=self.add, font=("times new roman", 13, "bold"),
                            relief=GROOVE, bd=5, width=20, height=3, bg="#BFC9CA", fg="black")
        add_button.grid(row=0, column=0, padx=8, pady=8)
        clear_button = Button(Button_Frame, command=self.clear, text="Clear", font=("times new roman", 13, "bold"),
                              relief=GROOVE, bd=5, width=20, height=3, bg="#BFC9CA", fg="black")
        clear_button.grid(row=0, column=1, padx=8, pady=8)
        exit_button = Button(Button_Frame, command=self.exit, text="Exit", font=("times new roman", 13, "bold"),
                             relief=GROOVE, bd=5, width=20, height=3, bg="#BFC9CA", fg="black")
        exit_button.grid(row=0, column=2, padx=8, pady=8)

    def add(self):
        if self.rollNo1.get() == "" or self.rollNo2.get() == "" or self.rollNo3.get() == "" or self.rollNo4.get() == "" or self.rollNo5.get() == "" or self.rollNo6.get() == "" or self.rollNo7.get() == "" or self.rollNo8.get() == "" or self.rollNo9.get() == "" or self.rollNo10.get() == "" or self.rollNo11.get() == "":
            messagebox.showerror("Error!", "All fields are required !")
        else:
            con = pymysql.connect(host="localhost", user="root", password="uokcsi2012", database="attendance")
            cur = con.cursor()
            cur.execute("insert into attendance_register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.attendance_day.get(),
                         self.attendance_date.get(),
                         self.attendance_time.get(),
                         self.rollNo1.get(),
                         self.rollNo2.get(),
                         self.rollNo3.get(),
                         self.rollNo4.get(),
                         self.rollNo5.get(),
                         self.rollNo6.get(),
                         self.rollNo7.get(),
                         self.rollNo8.get(),
                         self.rollNo9.get(),
                         self.rollNo10.get(),
                         self.rollNo11.get()
                         ))
            con.commit()
            con.close()
            messagebox.showinfo("Success!", "Record has been inserted !")

    def clear(self):
        self.rollNo1 = StringVar().set("")
        self.rollNo2 = StringVar().set("")
        self.rollNo3 = StringVar().set("")
        self.rollNo4 = StringVar().set("")
        self.rollNo5 = StringVar().set("")
        self.rollNo6 = StringVar().set("")
        self.rollNo7 = StringVar().set("")
        self.rollNo8 = StringVar().set("")
        self.rollNo9 = StringVar().set("")
        self.rollNo10 = StringVar().set("")
        self.rollNo11 = StringVar().set("")

    def exit(self):
        ask = messagebox.askyesno("Exit", "Are you sure?")
        if ask > 0:
            self.root.destroy()


root = Tk()
obj = Attendance(root)
root.mainloop()
