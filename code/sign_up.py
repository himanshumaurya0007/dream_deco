from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk


# -------------------------------------------------- MySQL DB Functions --------------------------------------------------
def clear_entities():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)


# -------------------------------------------------- MySQL DB Connection --------------------------------------------------
def connect_to_mysql_db():
    if name_entry.get() == '' or email_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '' or confirm_password_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    elif password_entry.get() != confirm_password_entry.get():
        messagebox.showerror('Error', 'Password and Confirm Password Mismatched!')
    else:
        try:
            # con = pymysql.connect(host='localhost', user='root', password='2711', database='sem4_py_mini_project')
            con = pymysql.connect(host='localhost', user='root', password='Sanchit@2004')
            my_cursor = con.cursor()
        except():
            messagebox.showerror('Error', 'Database connectivity issue!\nPlease, try again')
            return
        try:
            # sql_query_to_create_db = 'CREATE DATABASE sem4_py_mini_project'
            # my_cursor.execute(sql_query_to_create_db)
            sql_query_to_select_created_db = 'USE sem4_py_mini_project'
            my_cursor.execute(sql_query_to_select_created_db)
            # sql_query_to_create_table = 'CREATE TABLE user_sign_up(id INT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(50) NOT NULL, email VARCHAR(50) NOT NULL, username VARCHAR(30) UNIQUE NOT NULL, password VARCHAR(20) NOT NULL)'
            # my_cursor.execute(sql_query_to_create_table)
        except():
            my_cursor.execute('USE user_sign_up')

        sql_query_to_check_if_username_already_exists = 'SELECT * FROM user_sign_up WHERE username = %s'
        my_cursor.execute(sql_query_to_check_if_username_already_exists, (username_entry.get()))

        row = my_cursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exists\nPlease, try choosing another one.')
        else:
            sql_query_to_insert_data_into_table = 'INSERT INTO user_sign_up(name, email, username, password) VALUES(%s, %s, %s, %s)'
            my_cursor.execute(sql_query_to_insert_data_into_table, (name_entry.get(), email_entry.get(), username_entry.get(), password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful!')
            clear_entities()
            sign_up_window.destroy()
            import sign_in


# -------------------------------------------------- linking of pages --------------------------------------------------
def sign_in_page():
    sign_up_window.destroy()
    import sign_in


# ---------------------------------------------------- GUI ----------------------------------------------------

# Create the Tkinter window and run the application
sign_up_window = Tk()
sign_up_window.geometry('1366x768')
sign_up_window.title('Sign up')
sign_up_window.iconbitmap('')
sign_up_window.resizable(False, False)

# set the window state to maximized
# sign_up_window.state('zoomed')

cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/sign_up.jpeg')
cd_bg_label = Label(sign_up_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)

# Heading Label
cd_head_lbl = Label(sign_up_window, text='CREATE AN ACCOUNT', font=('Times New Roman', 25, 'bold'), bg='black',
                    fg='white')
cd_head_lbl.place(x=70, y=50)

# Name Label
Label(sign_up_window, text="Name", bg='black', fg='white', font=('Times New Roman', 20)).place(x=55, y=140)

# Name input TextField
name_entry = Entry(sign_up_window, width=30, font=('Times New Roman', 20), bd=0, fg='black', bg='white')
name_entry.place(x=55, y=180)

# Email Label
Label(sign_up_window, text="Email", bg='black', fg='white', font=('Times New Roman', 20)).place(x=55, y=230)

# Email input TextField
email_entry = Entry(sign_up_window, width=30, font=('Times New Roman', 20), bd=0, fg='black', bg='white')
email_entry.place(x=55, y=270)

# Username Label
Label(sign_up_window, text="Username", bg='black', fg='white', font=('Times New Roman', 20)).place(x=55, y=320)

# Username input TextField
username_entry = Entry(sign_up_window, width=30, font=('Times New Roman', 20), bd=0, fg='black', bg='white')
username_entry.place(x=55, y=360)

# Password Label
Label(sign_up_window, text="Password", bg='black', fg='white', font=('Times New Roman', 20)).place(x=55, y=410)

# Password input TextField
password_entry = Entry(sign_up_window, width=30, font=('Times New Roman', 20), bd=0, fg='black', bg='white')
password_entry.place(x=55, y=450)

# Confirm Password Label
Label(sign_up_window, text="Confirm Password", bg='black', fg='white', font=('Times New Roman', 20)).place(x=55,
                                                                                                                y=500)

# Confirm Password input TextField
confirm_password_entry = Entry(sign_up_window, width=30, font=('Times New Roman', 20), bd=0, fg='black', bg='white')
confirm_password_entry.place(x=55, y=540)

# Sign up Button
Button(sign_up_window, text='SIGNUP', font=('Open Sans', 18, 'bold'), fg='white', bg='firebrick1',
       activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=28, height=1,
       command=connect_to_mysql_db).place(x=55,
                                          y=590)

# Sign in Label
cd_sign_in_lbl = Label(sign_up_window, text="Already have an account?", font=('Open sans', 15, 'bold'),
                       fg='firebrick1',
                       bg='black')
cd_sign_in_lbl.place(x=100, y=655)

# Sign in btn
cd_sign_in_btn = Button(sign_up_window, text='Sign In', font=('Open Sans', 15, 'bold underline'), fg='blue',
                        bg='black', activeforeground='blue', activebackground='white', cursor='hand2', bd=0,
                        command=sign_in_page)
cd_sign_in_btn.place(x=350, y=650)

sign_up_window.mainloop()
