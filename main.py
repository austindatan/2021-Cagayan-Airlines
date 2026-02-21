import tkinter as tk
from datetime import datetime
from tkinter import RIGHT, messagebox, NO, YES, NW, ttk
from tkinter.ttk import Treeview
import mysql.connector
from PIL import Image, ImageTk

mydb = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="austinreverie",
    database="cagayan_airlines")
db = mydb.cursor(buffered=True)

root = tk.Tk()
root.title("CAGAYAN AIRLINES")
root.geometry("400x500")
root.resizable(False, False)
current_time = datetime.now()
mainwindowbg = tk.PhotoImage(file="assets/mainwindowbg.png")

global username
global to_destination
global class_info
global flight_type

canvas = tk.Canvas(root)
canvas.create_image(0,0,image=mainwindowbg, anchor=NW)
canvas.pack(fill="both", expand=True)

frame2 = tk.LabelFrame (canvas)
frame2.place(x=3,y=20)
frame2.configure(bg="#f6f6f6")

my_message = tk.Message (frame2, text ="Welcome to Cagayan Airlines",font=("Helvetica", 18), justify=RIGHT)
my_message.configure(bg="#f6f6f6")
label_time = tk.Label(frame2, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 8), justify=tk.CENTER)
label_time.configure(bg="#f6f6f6")
my_message.pack(pady=0, padx=5)
label_time.pack(pady=0)

my_message2 = tk.Label(root, text="Log In or Sign Up", font=("Helvetica", 10),bg="#f6f6f6").place(x=160,y=150)

button_insert = tk.Button(text="LOG IN", height=1, width=10, font=('verdana',14), bg="#ffbaf0", fg='black', command = lambda:[login_window()]).place(x=145,y=180)

button_insert2 = tk.Button(text="SIGN UP", height=1, width=10, font=('verdana',14), bg="#ffbaf0", fg='black', command = lambda:[signup_window()]).place(x=145, y=230)

global signup_bg
def signup_window():
    root.destroy()
    top = tk.Tk()
    top.resizable(False, False)
    top.title("CAGAYAN AIRLINES")
    top.geometry("420x800")

    signup_bg = Image.open("assets/signup2.png")
    signup_resize = signup_bg.resize((420, 900))
    signup_convert = ImageTk.PhotoImage(signup_resize)
    signup_button = tk.Button(image=signup_convert, borderwidth=0, highlightthickness=0)
    signup_button.image = signup_convert
    signup_button.place(x=0,y=0,relwidth=1,relheight=1)

    frame1 = tk.LabelFrame(top)
    frame1.grid(pady=20)
    frame1.configure(bg="#83c9ea")

    my_message = tk.Message(frame1, text="Welcome to Cagayan Airlines", font=("Helvetica", 18), justify=RIGHT)
    my_message.configure(bg="#83c9ea")
    label_time = tk.Label(frame1, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 10), justify=tk.CENTER)
    label_time.configure(bg="#83c9ea")
    my_message.grid(pady=5, padx=5)
    label_time.grid(pady=5)

    label_real_name = tk.Label(text="Name: ", font=('verdana', 12))
    label_real_name.config(bg="#83c9ea")
    entry_real_name = tk.Entry(font=('verdana', 12))
    entry_real_name.configure(bg="#83c9ea")
    label_real_name.grid(row=1, column=0)
    entry_real_name.grid(row=1, column=1, pady=20, padx=20)

    label_birthdate = tk.Label(text="Birthdate: ", font=('verdana', 12))
    label_birthdate.configure(bg="#83c9ea")
    entry_birthdate = tk.Entry(font=('verdana', 12))
    entry_birthdate.configure(bg="#83c9ea")
    label_birthdate.grid(row=2, column=0)
    entry_birthdate.grid(row=2, column=1, pady=20, padx=20)

    label_gender = tk.Label(text="Gender: ", font=('verdana', 12))
    label_gender.configure(bg="#83c9ea")
    label_gender.grid(row=3, column=0, pady=20, padx=20)
    vars = tk.StringVar()
    gender_malecheck = tk.Checkbutton (top, text="Male", font=('verdana', 12), padx=5, variable=vars, onvalue='Male', offvalue = 0,bg="#83c9ea").place(x=185, y=320)
    gender_female = tk.Checkbutton (top, text="Female", font=('verdana', 12), padx=20, variable=vars, onvalue='Female', offvalue = 0,bg="#83c9ea").place(x=255, y=320)

    label_username = tk.Label(text="Username: ", font=('verdana', 12))
    label_username.configure(bg="#83c9ea")
    entry_username = tk.Entry(font=('verdana', 12))
    entry_username.configure(bg="#83c9ea")
    label_username.grid(row=4, column=0)
    entry_username.grid(row=4, column=1, pady=20, padx=20)

    label_password = tk.Label(text="Password: ", font=('verdana', 12))
    label_password.configure(bg="#83c9ea")
    entry_password = tk.Entry(font=('verdana', 12), show="*")
    entry_password.configure(bg="#83c9ea")
    label_password.grid(row=5, column=0)
    entry_password.grid(row=5, column=1, pady=20, padx=20)

    button_insert = tk.Button(text="Insert", font=('verdana', 14), bg="#83c9ea", command=lambda: [newuser()])
    button_insert.grid(row=7, column=0, columnspan=2, pady=20, padx=20)

    def newuser():
        global username
        realname = entry_real_name.get()
        birthdate = entry_birthdate.get()
        gender = vars.get()
        username = entry_username.get()
        password = entry_password.get()

        if (realname == "" or birthdate == "" or gender == "" or username == "" or password == ""):
            messagebox.showwarning('WARNING', 'Insert Information, All Fields are Required')

        db.execute(f"SELECT * from signup_info WHERE username='{username}'")
        if db.fetchall():
            messagebox.showwarning('WARNING', 'User Already Exists!')

        else:
            insert_query = "INSERT INTO signup_info (`real_name`, `birthdate`, `gender`, `username`, `password`) VALUES (%s,%s,%s,%s,%s)"
            vals = (realname, birthdate, gender, username, password)
            db.execute(insert_query, vals)
            mydb.commit()
            messagebox.showwarning('SUCCESFUL', 'Account Added, Please Exit the System and Restart it.')

def login_window():
    root.destroy()
    top2 = tk.Tk()
    top2.resizable(False, False)
    top2.geometry("425x500")
    top2.title("CAGAYAN AIRLINES")

    signup_bg = Image.open('assets/login.png')
    signup_resize = signup_bg.resize((425, 500))
    signup_convert = ImageTk.PhotoImage(signup_resize)
    signup_button = tk.Button(image=signup_convert, borderwidth=0, highlightthickness=0)
    signup_button.image = signup_convert
    signup_button.place(x=0, y=0, relwidth=1, relheight=1)

    frame2 = tk.LabelFrame(top2)
    frame2.grid(pady=20)
    frame2.configure(bg="#54b5e8")

    my_message = tk.Message(frame2, text="Welcome to Cagayan Airlines", font=("Helvetica", 18), justify=RIGHT, fg="white")
    my_message.configure(bg="#54b5e8")
    label_time = tk.Label(frame2, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 10), justify=tk.CENTER, fg="white")
    label_time.configure(bg="#54b5e8")
    my_message.grid(pady=5, padx=5)
    label_time.grid(pady=5)

    label_player_name = tk.Label(text="User Name: ", font=('verdana', 12),fg="white")
    label_player_name.configure(bg="#54b5e8")
    entry_player_name = tk.Entry(font=('verdana', 12),fg="white")
    entry_player_name.configure(bg="#54b5e8")
    label_player_name.grid(row=1, column=0)
    entry_player_name.grid(row=1, column=1, pady=20, padx=20)

    label_email = tk.Label(text="Password: ", font=('verdana', 12),fg="white")
    label_email.configure(bg="#54b5e8")
    entry_email = tk.Entry(font=('verdana', 12), show="*",fg="white")
    entry_email.configure(bg="#54b5e8")
    label_email.grid(row=3, column=0)
    entry_email.grid(row=3, column=1, pady=20, padx=20)

    def login_window2():
        global username
        username = entry_player_name.get()
        email = entry_email.get()
        select_query = 'SELECT * FROM `signup_info` WHERE `username` = %s and password = %s'
        vals = (username, email,)
        db.execute(select_query, vals)
        user = db.fetchone()
        if user is not None:
            messagebox.showwarning('Logged In Succesfully','Logged In Succesfully, Please wait as we prepare your Adventures!')

            top2.destroy()
            homewindow = tk.Tk()
            homewindow.resizable(False, False)
            homewindow.geometry("500x642")
            homewindow.title("CAGAYAN AIRLINES")

            signup_bg = Image.open('assets/home.png')
            signup_resize = signup_bg.resize((500, 642))
            signup_convert = ImageTk.PhotoImage(signup_resize)
            signup_button = tk.Button(image=signup_convert, borderwidth=0, highlightthickness=0)
            signup_button.image = signup_convert
            signup_button.place(x=0, y=0, relwidth=1, relheight=1)

            frame2 = tk.LabelFrame(homewindow)
            frame2.grid(pady=20)
            frame2.configure(bg="#b8d7da")

            my_message = tk.Message(frame2, text="Welcome to Cagayan Airlines", font=("Helvetica", 18), justify=RIGHT)
            my_message.configure(bg="#b8d7da")
            label_time = tk.Label(frame2, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 10),justify=tk.CENTER)
            label_time.configure(bg="#b8d7da")
            my_message.grid(pady=1, padx=5)
            label_time.grid(pady=1)

            def flight_window():
                homewindow.destroy()
                flightlist = tk.Tk()
                flightlist.resizable(False,False)
                flightlist.geometry("640x560")
                flightlist.title("CAGAYAN AIRLINES")

                signup_bg = Image.open('assets/flights2.png')
                signup_resize = signup_bg.resize((1150, 560))
                signup_convert = ImageTk.PhotoImage(signup_resize)
                signup_button = tk.Button(image=signup_convert, borderwidth=0, highlightthickness=0)
                signup_button.image = signup_convert
                signup_button.place(x=0, y=0, relwidth=1, relheight=1)

                frame2 = tk.LabelFrame(flightlist)
                frame2.grid(pady=20)
                frame2.configure(bg="#83c9ea")

                my_message = tk.Message(frame2, text="Welcome to Cagayan Airlines", font=("Helvetica", 18),justify=RIGHT)
                my_message.configure(bg="#83c9ea")
                label_time = tk.Label(frame2, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 10),justify=tk.CENTER)
                label_time.configure(bg="#83c9ea")
                my_message.grid(pady=5, padx=5)
                label_time.grid(pady=5)

                fromcagayan = tk.Message(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea")
                fromcagayan.grid(pady=1, padx=5)

                destination = tk.Label(text="Destination: ", font=('verdana', 12))
                destination.configure(bg="#83c9ea")
                destination.grid(row=4, column=0, pady=20, padx=20)
                destination_string = tk.StringVar()
                paris = tk.Checkbutton(flightlist, text="Paris, France", font=('verdana', 12), padx=5,
                                       variable=destination_string, onvalue='Paris, France', offvalue=0,bg="#83c9ea").place(x=215,y=240)
                new_delhi = tk.Checkbutton(flightlist, text="New Delhi, India", font=('verdana', 12), padx=20,
                                           variable=destination_string, onvalue='New Delhi, India', offvalue=0,bg="#83c9ea").place(x=365, y=240)
                kyoto = tk.Checkbutton(flightlist, text="Kyoto, Japan", font=('verdana', 12), padx=20,
                                       variable=destination_string, onvalue='Kyoto, Japan', offvalue=0,bg="#83c9ea").place(x=200,y=285)
                manila = tk.Checkbutton(flightlist, text="Manila, Philippines", font=('verdana', 12), padx=20,
                                        variable=destination_string, onvalue='Manila, Philippines', offvalue=0,bg="#83c9ea").place(x=365, y=285)

                flight_types = tk.Label(text="Flight Type: ", font=('verdana', 12))
                flight_types.configure(bg="#83c9ea")
                flight_types.place(x=25, y=330)
                flight_types_string = tk.StringVar()
                one_way = tk.Checkbutton(flightlist, text="One Way", font=('verdana', 12), padx=5,
                                         variable=flight_types_string, onvalue='One Way', offvalue=0,bg="#83c9ea").place(x=215, y=330)
                round_trip = tk.Checkbutton(flightlist, text="Round Trip", font=('verdana', 12), padx=20,
                                            variable=flight_types_string, onvalue='Round Trip', offvalue=0,bg="#83c9ea").place(x=365, y=330)

                class_type = tk.Label(text="Class Info: ", font=('verdana', 12))
                class_type.configure(bg="#83c9ea")
                class_type.place(x=25, y=380)
                class_types_string = tk.StringVar()
                first_class = tk.Checkbutton(flightlist, text="First Class", font=('verdana', 12), padx=5,
                                         variable=class_types_string, onvalue='First Class', offvalue=0,bg="#83c9ea").place(x=215,y=380)
                business_class = tk.Checkbutton(flightlist, text="Business Class", font=('verdana', 12), padx=20,
                                            variable=class_types_string, onvalue='Business Class', offvalue=0,bg="#83c9ea").place(x=365,y=380)
                premium_economy = tk.Checkbutton(flightlist, text="Premium", font=('verdana', 12), padx=5,
                                             variable=class_types_string, onvalue='Premium Economy', offvalue=0,bg="#83c9ea").place(x=215, y=425)
                premium_economy2 = tk.Label(text="Economy",font=("Helvetica", 12),bg="#83c9ea").place(x=242, y=450)
                economy = tk.Checkbutton(flightlist, text="Economy", font=('verdana', 12), padx=20,
                                                variable=class_types_string, onvalue='Economy',offvalue=0,bg="#83c9ea").place(x=365, y=425)

                button_insert = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea",fg='black',command=lambda: [flight_update()])
                button_insert.place(x=330, y=490)

                def flight_update():
                    global username
                    global to_destination
                    global flight_type
                    global class_info
                    flight_type = flight_types_string.get()
                    to_destination = destination_string.get()
                    class_info = class_types_string.get()

                    if (flight_type == "" or to_destination == "" or class_info ==""):
                        messagebox.showwarning('WARNING', 'Insert Information, All Fields are Required')
                    else:
                        button_insert.destroy()
                        flightlist.geometry("1150x560")
                        messagebox.showinfo('SUCCESFUL', 'Complete the next form to continue.')

                        if (flight_type == "One Way" and to_destination == "Paris, France" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Paris, France" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Paris, France" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Paris, France" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Paris, France" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Paris, France" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Paris, France" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Paris, France" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Paris, France", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "New Delhi, India" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "New Delhi, India" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "New Delhi, India" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "New Delhi, India" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "New Delhi, India" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "New Delhi, India" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "New Delhi, India" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "New Delhi, India" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to New Delhi, India", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Kyoto, Japan" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Kyoto, Japan" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Kyoto, Japan" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Kyoto, Japan" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Kyoto, Japan" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Kyoto, Japan" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Kyoto, Japan" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Kyoto, Japan" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Kyoto, Japan", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Manila, Philippines" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Manila, Philippines" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Manila, Philippines" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "Round Trip" and to_destination == "Manila, Philippines" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing Round Trip Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Manila, Philippines" and class_info =="Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Manila, Philippines" and class_info =="Premium Economy"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Premium Economy Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Manila, Philippines" and class_info =="Business Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: Business Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        elif (flight_type == "One Way" and to_destination == "Manila, Philippines" and class_info =="First Class"):
                            fromcagayan = tk.Label(text="From: Cagayan Airlines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=165)
                            fromdestination = tk.Label(text="Showing One Way Flights to Manila, Philippines", font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=185)
                            fromclass = tk.Label(text="Class Type: First Class Flights",font=("Helvetica", 10),bg="#83c9ea").place(x=620, y=205)

                            airline_string = tk.StringVar()
                            airline_header = tk.Label(text="Airline:", font=("Helvetica", 11),bg="#83c9ea").place(x=675, y=240)
                            departure_header = tk.Label(text="Departure Time:", font=("Helvetica", 11),bg="#83c9ea").place(x=850, y=240)
                            cost_header = tk.Label(text="Prices:", font=("Helvetica", 11),bg="#83c9ea").place(x=1060, y=240)

                            qatar_airways = tk.Checkbutton(flightlist, text="Qatar Airways", font=('verdana', 12), padx=5,
                                                         variable=airline_string, onvalue='Qatar Airways',offvalue=0,bg="#83c9ea").place(x=620, y=270)
                            qatar_departure = tk.Label(text="2023-04-14 23:00:00",font=('verdana', 12),bg="#83c9ea").place(x=815, y=270)
                            qatar_cost = tk.Label(text="45,801.51",font=('verdana', 12),bg="#83c9ea").place(x=1040, y=270)

                            emirates_airways = tk.Checkbutton(flightlist, text="Emirates", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Emirates', offvalue=0,bg="#83c9ea").place(x=620, y=320)
                            emirates_departure = tk.Label(text="2023-04-18 12:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=320)
                            emirates_cost = tk.Label(text="49,245.99", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=320)

                            air_france_airways = tk.Checkbutton(flightlist, text="Air France", font=('verdana', 12),padx=5,
                                                           variable=airline_string, onvalue='Air France',offvalue=0,bg="#83c9ea").place(x=620, y=370)
                            air_france_departure = tk.Label(text="2023-04-14 21:00:00", font=('verdana', 12),bg="#83c9ea").place(x=815,y=370)
                            air_france_cost = tk.Label(text="42,981.00", font=('verdana', 12),bg="#83c9ea").place(x=1040, y=370)

                            flight_button = tk.Button(text="Submit", font=('verdana', 14) ,bg="#83c9ea", fg='black', command=lambda: [header_change(), flight_processes()])
                            flight_button.place(x=815, y=400)

                        def header_change():
                            global airline
                            global departure
                            global flight_cost
                            airline = airline_string.get()

                            if (airline == "Qatar Airways"):
                                departure = ('2023-04-14 23:00:00')
                                flight_cost = ('45,801.51')
                            elif (airline == "Emirates"):
                                departure = ('2023-04-18 12:00:00')
                                flight_cost = ('49,245.99')
                            elif (airline == "Air France"):
                                departure = ('2023-04-14 21:00:00')
                                flight_cost = ('42,981.00')

                        def flight_processes():
                            global username
                            global to_destination
                            global flight_type
                            global class_info
                            global airline
                            global departure
                            global flight_cost

                            if (airline == ""):
                                messagebox.showwarning('WARNING', 'Insert Information, All Fields are Required')
                            else:
                                flight_button.destroy()
                                insert_query = "INSERT INTO flight_info (`username`,`destination`, `flight_type`,`class_info`,`airline`,`departure`,`flight_cost`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                                vals = (username, to_destination,flight_type , class_info, airline, departure, flight_cost)
                                db.execute(insert_query, vals)
                                mydb.commit()
                                messagebox.showinfo('SUCCESFUL', 'Reservation Complete.')

                                flightlist.destroy()
                                paywindow = tk.Tk()
                                paywindow.resizable(False, False)
                                paywindow.geometry("500x500")
                                paywindow.title("CAGAYAN AIRLINES")

                                signup_bg = Image.open('assets/paywindow.png')
                                signup_resize = signup_bg.resize((500, 500))
                                signup_convert = ImageTk.PhotoImage(signup_resize)
                                signup_button = tk.Button(image=signup_convert, borderwidth=0, highlightthickness=0)
                                signup_button.image = signup_convert
                                signup_button.place(x=0, y=0, relwidth=1, relheight=1)

                                select_query = 'SELECT real_name, gender FROM `signup_info` WHERE username'
                                db.execute(select_query)

                                frame2 = tk.LabelFrame(paywindow)
                                frame2.grid(pady=20)
                                frame2.configure(bg="#b8d7da")

                                my_message = tk.Message(frame2, text="Welcome to Cagayan Airlines", font=("Helvetica", 18), justify=RIGHT,bg="#b8d7da")
                                label_time = tk.Label(frame2, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 10), justify=tk.CENTER,bg="#b8d7da")
                                my_message.grid(pady=5, padx=5)
                                label_time.grid(pady=5)

                                reciept = tk.Label(text="PARTIAL RECIEPT", font=('verdana', 12),bg="#b8d7da").place(x=40, y=180)

                                reciept = tk.Label(text="Present this Reciept to the ", font=('verdana', 10), bg="#b8d7da").place(x=250, y=180)
                                reciept = tk.Label(text="Front Desk Cashier when ",font=('verdana', 10), bg="#b8d7da").place(x=250, y=205)
                                reciept = tk.Label(text="paying for your flights.",font=('verdana', 10), bg="#b8d7da").place(x=250, y=230)

                                username_label = tk.Label(text="Username", font=('verdana', 10),bg="#b8d7da").place(x=40, y=205)
                                username_reciept = tk.Label(text=username, font=('verdana', 12),bg="#b8d7da").place(x=40, y=225)

                                from_label = tk.Label(text="Origin:", font=('verdana', 10),bg="#b8d7da").place(x=40,y=260)
                                from_reciept = tk.Label(text="Cagayan Airlines", font=('verdana', 12),bg="#b8d7da").place(x=40,y=285)

                                destination_label = tk.Label(text="Destination:", font=('verdana', 10),bg="#b8d7da").place(x=250, y=260)
                                destination_reciept = tk.Label(text=to_destination, font=('verdana', 12),bg="#b8d7da").place(x=250, y=285)

                                air_label = tk.Label(text="Airline:", font=('verdana', 10),bg="#b8d7da").place(x=40, y=320)
                                air_reciept = tk.Label(text=airline, font=('verdana', 12),bg="#b8d7da").place(x=40,y=345)

                                type_label = tk.Label(text="Flight Type:", font=('verdana', 10),bg="#b8d7da").place(x=250,y=320)
                                type_reciept = tk.Label(text=flight_type, font=('verdana', 12),bg="#b8d7da").place(x=250,y=345)

                                departure_label = tk.Label(text="Departure:", font=('verdana', 10),bg="#b8d7da").place(x=40, y=380)
                                air_reciept = tk.Label(text=departure, font=('verdana', 12),bg="#b8d7da").place(x=40, y=405)

                                header_label = tk.Label(text="Flight Price:", font=('verdana', 10),bg="#b8d7da").place(x=250, y=380)
                                type_reciept = tk.Label(text=flight_cost, font=('verdana', 12),bg="#b8d7da").place(x=250, y=405)

            def flight_cancel():
                homewindow.destroy()
                flightcancel = tk.Tk()
                flightcancel.resizable(False, False)
                flightcancel.geometry("880x600")
                flightcancel.title("CAGAYAN AIRLINES")

                signup_bg = Image.open('assets/cancel.png')
                signup_resize = signup_bg.resize((880, 600))
                signup_convert = ImageTk.PhotoImage(signup_resize)
                signup_button = tk.Button(image=signup_convert, borderwidth=0, highlightthickness=0)
                signup_button.image = signup_convert
                signup_button.place(x=0, y=0, relwidth=1, relheight=1)

                frame2 = tk.LabelFrame(flightcancel)
                frame2.place(x=1,y=20)
                frame2.configure(bg="#83c9ea")

                my_message = tk.Message(frame2, text="Welcome to Cagayan Airlines", font=("Helvetica", 18),justify=RIGHT,bg="#83c9ea")
                label_time = tk.Label(frame2, text=f"{current_time:%A, %B %d, %Y}", font=("Helvetica", 10),justify=tk.CENTER,bg="#83c9ea")
                my_message.grid(pady=5, padx=5)
                label_time.grid(pady=5)

                def search_info():
                    user_search = user_entry.get()
                    select_query = 'SELECT * FROM `flight_info` WHERE `username` = %s'
                    vals = (user_search,)
                    db.execute(select_query, vals)
                    user = db.fetchone()

                    if user is None or (user_search == ""):
                        messagebox.showwarning('INVALID','User does not Exist!')

                    if user is not None:
                        def update(rows):
                            flight.delete(*flight.get_children())
                            for i in rows:
                                flight.insert('', 'end', values=i)

                        user_search = user_entry.get()
                        query = F"SELECT flight_id, username, destination, flight_type, class_info, airline, departure, flight_cost from flight_info WHERE username LIKE '%"+user_search+"%'"
                        db.execute(query)
                        rows = db.fetchall()
                        update(rows)

                        search_button.destroy()
                        search_label.destroy()
                        search_entry.destroy()
                        password_entry.destroy()
                        password_label.destroy()

                        def delete_flight():
                            flight_idS = flight_id.get()
                            if tk.messagebox.askyesno("Confirm to Cancel Flight?", "Are you sure you want to cancel your flight?"):
                                query = f"DELETE FROM flight_info WHERE flight_id ='{flight_idS}'"
                                db.execute(query)
                                mydb.commit()
                                user_search = user_entry.get()
                                query = F"SELECT flight_id, username, destination, flight_type, class_info, airline, departure, flight_cost from flight_info WHERE username LIKE '%" + user_search + "%'"
                                db.execute(query)
                                rows = db.fetchall()
                                update(rows)
                                message_flight_id.configure(state="normal", bg="#83c9ea")
                                message_username.configure(state="normal", bg="#83c9ea")
                                message_destination.configure(state="normal", bg="#83c9ea")
                                message_flight_type.configure(state="normal", bg="#83c9ea")
                                message_class_type.configure(state="normal", bg="#83c9ea")
                                message_airline.configure(state="normal", bg="#83c9ea")
                                message_departure.configure(state="normal", bg="#83c9ea")
                                message_flight_cost.configure(state="normal", bg="#83c9ea")
                                tk.messagebox.showinfo('Succesful!', 'Flight was Cancelled')

                                message_flight_id.delete(0, tk.END)
                                message_username.delete(0, tk.END)
                                message_destination.delete(0, tk.END)
                                message_flight_type.delete(0, tk.END)
                                message_class_type.delete(0, tk.END)
                                message_airline.delete(0, tk.END)
                                message_departure.delete(0, tk.END)
                                message_flight_cost.delete(0, tk.END)
                            else:
                                return True

                        cancel_flight_button = tk.Button(text="Cancel Flight", command=delete_flight)
                        cancel_flight_button.place(x=700, y=555)

                def getrows():
                    message_flight_id.delete(0, tk.END)
                    message_username.delete(0, tk.END)
                    message_destination.delete(0, tk.END)
                    message_flight_type.delete(0, tk.END)
                    message_class_type.delete(0, tk.END)
                    message_airline.delete(0, tk.END)
                    message_departure.delete(0, tk.END)
                    message_flight_cost.delete(0, tk.END)

                    selected_row = flight.focus()
                    values = flight.item(selected_row, 'values')

                    message_flight_id.insert(0, values[0])
                    message_username.insert(0, values[1])
                    message_destination.insert(0, values[2])
                    message_flight_type.insert(0, values[3])
                    message_class_type.insert(0, values[4])
                    message_airline.insert(0, values[5])
                    message_departure.insert(0, values[6])
                    message_flight_cost.insert(0, values[7])
                    message_flight_id.configure(state="readonly", readonlybackground="#83c9ea")
                    message_username.configure(state="readonly", readonlybackground="#83c9ea")
                    message_destination.configure(state="readonly", readonlybackground="#83c9ea")
                    message_flight_type.configure(state="readonly", readonlybackground="#83c9ea")
                    message_class_type.configure(state="readonly", readonlybackground="#83c9ea")
                    message_airline.configure(state="readonly", readonlybackground="#83c9ea")
                    message_departure.configure(state="readonly", readonlybackground="#83c9ea")
                    message_flight_cost.configure(state="readonly", readonlybackground="#83c9ea")

                def clicker(e):
                    getrows()

                flight_wrapper = tk.LabelFrame(flightcancel, text="Flight List")
                flight_wrapper.place(x=25, y=200)
                flight_wrapper.configure(bg="#83c9ea")

                flight = Treeview(flight_wrapper, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="6")
                flight.grid()
                flight.bind("<Double-1>", clicker)
                flight.heading(1, text="Flight ID")
                flight.column(1, minwidth=0, width=100, stretch=NO)
                flight.heading(2, text="Username")
                flight.column(2, minwidth=0, width=100, stretch=NO)
                flight.heading(3, text="Destination")
                flight.column(3, minwidth=0, width=100, stretch=NO)
                flight.heading(4, text="Flight Type")
                flight.column(4, minwidth=0, width=100, stretch=NO)
                flight.heading(5, text="Class Info")
                flight.column(5, minwidth=0, width=100, stretch=NO)
                flight.heading(6, text="Airline")
                flight.column(6, minwidth=0, width=100, stretch=NO)
                flight.heading(7, text="Departure")
                flight.column(7, minwidth=0, width=130, stretch=YES)
                flight.heading(8, text="Flight Cost")
                flight.column(8, minwidth=0, width=100, stretch=NO)

                search_label = tk.Label(text="Cancel Your Flights Here", font=('verdana', 12), bg="#83c9ea")
                search_label.place(x=30, y=170)

                search_label = tk.Label(text="Please Verify Your Username",font=('verdana', 12),bg="#83c9ea")
                search_label.place (x=30, y=375)
                user_entry = tk.StringVar()
                search_entry = tk.Entry(textvariable=user_entry,bg="#83c9ea")
                search_entry.place (x=320, y =375)

                password_label = tk.Label(text="Password", font=('verdana', 12),bg="#83c9ea")
                password_label.place(x=450, y=375)
                password_entry = tk.Entry(bg="#83c9ea", show="*")
                password_entry.place(x=540, y=375)

                search_button = tk.Button (text="Verify Account",command=search_info,bg="#83c9ea",fg='black')
                search_button.place (x=700, y=372)

                # flight information
                flight_id = tk.StringVar()
                show_flight_id = tk.Label(text="Flight ID:", font=('verdana', 10), bg="#83c9ea").place(x=40, y=400)
                message_flight_id = tk.Entry(textvariable=flight_id, font=('verdana', 12),bg="#83c9ea")
                message_flight_id.place(x=40, y=425)

                flight_username = tk.StringVar()
                show_username = tk.Label(text="Username:", font=('verdana', 10),bg="#83c9ea").place(x=250, y=400)
                message_username = tk.Entry(textvariable=flight_username, font=('verdana', 12),bg="#83c9ea")
                message_username.place(x=250, y=425)

                flight_destination = tk.StringVar()
                show_destination = tk.Label(text="Destination:", font=('verdana', 10),bg="#83c9ea").place(x=40, y=460)
                message_destination = tk.Entry(textvariable=flight_destination, font=('verdana', 12),bg="#83c9ea")
                message_destination.place(x=40, y=485)

                flight_type = tk.StringVar()
                show_flight_type = tk.Label(text="Flight Type", font=('verdana', 10),bg="#83c9ea").place(x=250, y=460)
                message_flight_type = tk.Entry(textvariable=flight_type, font=('verdana', 12),bg="#83c9ea")
                message_flight_type.place(x=250, y=485)

                class_type = tk.StringVar()
                show_class_type = tk.Label(text="Class Info", font=('verdana', 10),bg="#83c9ea").place(x=460, y=460)
                message_class_type = tk.Entry(textvariable=class_type, font=('verdana', 12),bg="#83c9ea")
                message_class_type.place(x=460, y=485)

                airline_type = tk.StringVar()
                show_airline = tk.Label(text="Airline", font=('verdana', 10),bg="#83c9ea").place(x=40, y=520)
                message_airline = tk.Entry(textvariable=airline_type, font=('verdana', 12),bg="#83c9ea")
                message_airline.place(x=40, y=555)

                flight_departure = tk.StringVar()
                show_departure = tk.Label(text="Departure:", font=('verdana', 10),bg="#83c9ea").place(x=250, y=520)
                message_departure = tk.Entry(textvariable=flight_departure, font=('verdana', 12),bg="#83c9ea")
                message_departure.place(x=250, y=555)

                flight_flight_cost = tk.StringVar()
                show_flight_cost = tk.Label(text="Flight Cost:", font=('verdana', 10),bg="#83c9ea").place(x=460, y=520)
                message_flight_cost = tk.Entry(textvariable=flight_flight_cost, font=('verdana', 12),bg="#83c9ea")
                message_flight_cost.place(x=460, y=555)

            flight_icon = Image.open('assets/air.png')
            flight_resize = flight_icon.resize((60, 60))
            flight_convert = ImageTk.PhotoImage(flight_resize)
            flight_button = tk.Button(image=flight_convert, borderwidth=0, highlightthickness=0, command=flight_window,bg="#b8d7da")
            flight_button.image = flight_convert
            flight_button.place(x=45,y=160)
            flight_labelT = tk.Label(text="Flight", font=('Helvetica', 9))
            flight_labelT.place(x=55, y=224)
            flight_labelT.configure(bg="#b8d7da")
            flight_labelR = tk.Label(text="Reservations", font=('Helvetica', 9))
            flight_labelR.place(x=35, y=240)
            flight_labelR.configure(bg="#b8d7da")

            flight_icon = Image.open('assets/air.png')
            flight_resize = flight_icon.resize((60, 60))
            flight_convert = ImageTk.PhotoImage(flight_resize)
            flight_button = tk.Button(image=flight_convert, borderwidth=0, highlightthickness=0, command=flight_cancel,bg="#b8d7da")
            flight_button.image = flight_convert
            flight_button.place(x=150,y=160)
            flight_cancel2 = tk.Label(text="Cancel", font=('Helvetica', 9))
            flight_cancel2.place(x=156, y=224)
            flight_cancel2.configure(bg="#b8d7da")
            flight_s = tk.Label(text="Flights", font=('Helvetica', 9))
            flight_s.place(x=157, y=240)
            flight_s.configure(bg="#b8d7da")

            frame3 = tk.LabelFrame(homewindow)
            frame3.place(x=0,y=273)
            frame3.configure(bg="#b8d7da")
            my_message1 = tk.Message(frame3, text="Introducing Deluxe SELECTIONS", font=("Helvetica", 17),justify=RIGHT)
            my_message1.configure(bg="#b8d7da")
            my_message1.grid(pady=0, padx=1)

            india_icon = Image.open('assets/india.png')
            india_resize = india_icon.resize((325, 96))
            india_convert = ImageTk.PhotoImage(india_resize)
            india_button = tk.Button(image=india_convert, borderwidth=0, highlightthickness=0, command=flight_window)
            india_button.place (x=177, y=273)
            india_button.image = india_convert

        else:
            messagebox.showwarning('Error', 'ERROR, Enter a Valid Username & Password!')

    button_insert = tk.Button(text="LOG IN", height=1, width=10, font=('verdana', 14), fg='white',command=lambda:[login_window2()],bg="#54b5e8")
    button_insert.place(x=250, y=300)

root.mainloop()

