from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

import pymysql
from PIL import ImageTk


# -------------------------------------------------- MySQL DB Functions
# --------------------------------------------------
def clear_entities():
    combo_2.delete(0, END)
    combo_1.delete(0, END)
    Height.delete(0, END)
    Width.delete(0, END)
    Br.delete(0, END)
    Req.delete(0, END)


# -------------------------------------------------- MySQL DB Connection
# --------------------------------------------------
def connect_to_mysql_db():
    if combo_2.get() == '' or combo_1.get() == '' or Height.get() == '' or Width.get() == '' or Br.get() == '' or Req.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    else:
        try:
            # con = pymysql.connect(host='localhost', user='root', password='2711', database='sem4_py_mini_project')
            con = pymysql.connect(host='localhost', user='root', password='Sanchit@2004')
            my_cursor = con.cursor()
        except():
            messagebox.showerror('Error', 'Database connectivity issue!\nPlease, try again')
            return
        try:
            sql_query_to_select_created_db = 'USE sem4_py_mini_project'
            my_cursor.execute(sql_query_to_select_created_db)

            sql_query_to_insert_data_into_table = 'INSERT INTO exterior_1(product_type, floors, dim_height, dim_width, dim_breadth, requirement) VALUES(%s, %s, %d, %d, %d, %d)'
            my_cursor.execute(sql_query_to_insert_data_into_table,
                              (combo_2.get(), combo_1.get, Height.get(), Width.get(), Br.get(), Req.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful!')
            clear_entities()
            cd_ext1_window.destroy()
            import exterior_2
        except():
            my_cursor.execute('USE exterior_1')



# Create the Tkinter  and run the application
cd_ext1_window = Tk()
cd_ext1_window.geometry('1366x768')
cd_ext1_window.title('Exterior 1')
cd_ext1_window.iconbitmap('')
cd_ext1_window.resizable(False, False)

cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/ext-1.jpeg')
cd_bg_label = Label(cd_ext1_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)


def next_page_to_materials():
    cd_ext1_window.destroy()


def ub2():
    cd_ext1_window.destroy()
    import exterior_2


def ub1():
    cd_ext1_window.destroy()
    import home_page


def display_popup():
    if not Req.get() or not Height.get() or not Br.get() or not Width.get():
        messagebox.showerror("Error", "Please enter all values!")
    else:
        cd_ext1_window.destroy()
        import exterior_2


# functions
def go_to_page():
    cd_ext1_window.destroy()


def next_page_to_home():
    cd_ext1_window.destroy()


lbl = Label(cd_ext1_window, bg='black', width=105, height=120)
lbl.place(x=0, y=0)

# label floor
lbl1 = Label(cd_ext1_window, text='Select Product', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=100)
# text field of floor
combo_2 = ttk.Combobox(state="readonly", values=["House", "Hospital", "School"], font=("Helvetica", 19))
combo_2.place(x=400, y=100)

# label house space
lbl1 = Label(cd_ext1_window, text='Floors', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=170)
# text field of floor
combo_1 = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"], font=("Helvetica", 19))
combo_1.place(x=400, y=170)

btn_back = Button(cd_ext1_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                  activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                  command=ub1)
btn_back.place(x=0, y=10)
lbl1 = Label(cd_ext1_window, text='Floor Dimension', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=240)

lbl1 = Label(cd_ext1_window, text='Height', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=310)

Height = Entry(cd_ext1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Height.place(x=400, y=310)

lbl1 = Label(cd_ext1_window, text='Width', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=380)

Width = Entry(cd_ext1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Width.place(x=400, y=380)

lbl1 = Label(cd_ext1_window, text='Breadth', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=450)

Br = Entry(cd_ext1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Br.place(x=400, y=450)

lbl1 = Label(cd_ext1_window, text='Requirements', font=("Helvetica", 26), bg='black', fg='white')
lbl1.place(x=90, y=520)

Req = Entry(cd_ext1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Req.place(x=400, y=520)

btn_paynow = Button(cd_ext1_window, text='Confirm', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                    activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                    command=connect_to_mysql_db)
btn_paynow.place(x=90, y=590)

btn_paynow = Button(cd_ext1_window, text='Pay Now', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                    activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                    command=ub2)
btn_paynow.place(x=90, y=660)

cd_ext1_window.mainloop()
