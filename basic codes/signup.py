import tkinter as tk
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

# Create the Tkinter window and run the application
cd_signup_window = Tk()
cd_signup_window.geometry('1366x768')
cd_signup_window.title('Registration')
cd_signup_window.iconbitmap('')


# set the window state to maximized
# cd_signup_window.state('zoomed')

# Functionality
def name_enter(event):
    if name_entry.get() == 'Name':
        name_entry.delete(0, END)


def username_enter(event):
    if username_entry.get() == 'Username':
        username_entry.delete(0, END)


def answer_enter(event):
    if answer_entry.get() == 'Security Answer':
        answer_entry.delete(0, END)


def password_enter(event):
    if password_entry.get() == 'Password':
        password_entry.delete(0, END)


# def hide(event):
#     cd_open_eye.config(file='closeye.png')
#     password_entry.config(show='*')
#     cd_eye_btn.config(command=show)


# def show():
#     cd_open_eye.config(file='openeye.png')
#     password_entry.config(show='')
#     cd_eye_btn.config(command=hide)


# Heading Label
cd_head_lbl = Label(cd_signup_window, text='REGISTRATION', font=('Times New Roman', 30, 'bold'), bg='white',
                    fg='firebrick1')
cd_head_lbl.place(x=190, y=105)

# Name input TextField
name_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
name_entry.place(x=127, y=180)
name_entry.insert(0, 'Name')
name_entry.bind('<FocusIn>', name_enter)

# Name line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=215)

# Username input TextField
username_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
username_entry.place(x=127, y=250)
username_entry.insert(0, 'Username')
username_entry.bind('<FocusIn>', username_enter)

# Username line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=285)

# list of options in dropdown-menu
cd_options = ["What is your mother's name?", "What is your nick name?", "Who is your first childhood friend?",
              "What is your first school name?"]

# Label
cd_sec_ques_lbl = Label(cd_signup_window, text='Security Question', font=('Times New Roman', 20, 'bold'), bg='white',
                        fg='firebrick1')
cd_sec_ques_lbl.place(x=127, y=315)

# create a combobox
selected_option = tk.StringVar()
cd_combobox = ttk.Combobox(cd_signup_window, textvariable=selected_option, values=cd_options, width=29,
                           font=('Times New Roman', 20, 'bold'), state="readonly")
cd_combobox.current(0)
cd_combobox.place(x=127, y=357)

# create a style and set the foreground color
cd_style = ttk.Style()
cd_style.map('TCombobox', fieldforeground=[('readonly', 'red')])

# Answer input TextField
answer_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
answer_entry.place(x=127, y=410)
answer_entry.insert(0, 'Security Answer')
answer_entry.bind('<FocusIn>', answer_enter)

# Answer line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=445)

# Password input TextField
password_entry = Entry(cd_signup_window, width=25, font=('Times New Roman', 20, 'bold'), bd=0, fg='firebrick1')
password_entry.place(x=127, y=485)
password_entry.insert(0, 'Password')
password_entry.bind('<FocusIn>', password_enter)

# Password line for TextField
Frame(cd_signup_window, width=430, height=2, bg='firebrick1').place(x=127, y=520)

# Button
cd_login_btn = Button(cd_signup_window, text='SIGNUP', font=('Open Sans', 17, 'bold'), fg='white', bg='firebrick1',
                      activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=30, height=1)
cd_login_btn.place(x=127, y=550)

cd_signup_window.mainloop()
