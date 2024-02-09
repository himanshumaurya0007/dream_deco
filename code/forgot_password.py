from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk


# -------------------------------------------------- MySQL DB Connection --------------------------------------------------
def reset_password():
    if username_entry.get() == '' or new_password_entry.get() == '' or confirm_new_password_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    elif new_password_entry.get() != confirm_new_password_entry.get():
        messagebox.showerror('Error', 'New password and confirm new password mismatched!')
    else:
        con = pymysql.connect(host='localhost', user='root', password='2711', database='sem4_py_mini_project')
        my_cursor = con.cursor()
        sql_query = 'SELECT * FROM user_sign_up WHERE username = %s'
        my_cursor.execute(sql_query, (username_entry.get()))

        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Incorrect username!')
        else:
            sql_query = 'UPDATE user_sign_up SET password = %s WHERE username = %s'
            my_cursor.execute(sql_query, (new_password_entry.get(), username_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Password reset successfully!')
            forgot_password_window.destroy()
            import sign_in


# -------------------------------------------------- linking of pages --------------------------------------------------
def sign_in_page():
    forgot_password_window.destroy()
    import sign_in


# ---------------------------------------------------- GUI ----------------------------------------------------

# Create the Tkinter window and run the application
forgot_password_window = Tk()
forgot_password_window.geometry('1366x768')
forgot_password_window.title('Forgot Password')
forgot_password_window.iconbitmap('')
forgot_password_window.resizable(False, False)

# set the window state to maximized
# forgot_password_window.state('zoomed')

cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/forgot.jpeg')
cd_bg_label = Label(forgot_password_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)

# Changing bb color to white
# Label(forgot_password_window, bg='white', height=1366, width=768).place(x=0, y=0)

# Heading Label
cd_head_lbl = Label(forgot_password_window, text='RESET PASSWORD', font=('Times New Roman', 30, 'bold'), bg='black',
                    fg='white')
cd_head_lbl.place(x=890, y=200)

# Username Label
Label(forgot_password_window, text="Username", bg='black', fg='orchid1', font=('Times New Roman', 20)).place(x=890, y=300)

# Username input TextField
username_entry = Entry(forgot_password_window, width=18, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
username_entry.place(x=890, y=340)

# Username line for TextField
Frame(forgot_password_window, width=253, height=2, bg='orchid1').place(x=890, y=380)

# New Password Label
Label(forgot_password_window, text="New Password", bg='black', fg='orchid1', font=('Times New Roman', 20)).place(x=890, y=410)

# New Password input TextField
new_password_entry = Entry(forgot_password_window, width=18, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
new_password_entry.place(x=890, y=450)

# New Password line for TextField
Frame(forgot_password_window, width=253, height=2, bg='orchid1').place(x=890, y=490)

# Confirm New Password Label
Label(forgot_password_window, text="Confirm New Password", bg='black', fg='orchid1', font=('Times New Roman', 20)).place(x=890, y=520)

# Confirm New Password input TextField
confirm_new_password_entry = Entry(forgot_password_window, width=18, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
confirm_new_password_entry.place(x=890, y=560)

# Confirm New Password line for TextField
Frame(forgot_password_window, width=253, height=2, bg='orchid1').place(x=890, y=600)

# Sign up Button
Button(forgot_password_window, text='RESET', font=('Open Sans', 20, 'bold'), fg='white', bg='purple',
       activeforeground='white', activebackground='orchid1', cursor='hand2', bd=0, width=12, height=1, command=reset_password).place(x=950, y=640)

forgot_password_window.mainloop()
