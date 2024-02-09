from tkinter import *

from PIL import ImageTk

# Create the Tkinter cd_home_window and run the application
cd_home_window = Tk()
cd_home_window.geometry('1366x768')

cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/home.jpeg')
cd_bg_label = Label(cd_home_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)



# heading
def next_page_to_sign_in():
    cd_home_window.destroy()
    import sign_in

def next_page_to_ext_1():
    cd_home_window.destroy()
    import exterior_1
def next_page_to_int_1():
    cd_home_window.destroy()
    import interior_1
def next_page_to_ub_1():
    cd_home_window.destroy()
    import Urbanovate_1
def next_page_to_materials():
    cd_home_window.destroy()
    import materials




# Back button
cd_btn_back = Button(cd_home_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='red',
                     activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                     command=next_page_to_sign_in)
cd_btn_back.place(x=60, y=50)

# Construction Button
btn = Button(cd_home_window, text='Exterior', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
             command=next_page_to_ext_1)
btn.place(x=60, y=300)

# Interior design button
btn = Button(cd_home_window, text='Interior', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
             command=next_page_to_int_1)
btn.place(x=60, y=400)

btn = Button(cd_home_window, text='Urbanovate', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
             command=next_page_to_ub_1)
btn.place(x=400, y=300)

# Interior design button
btn = Button(cd_home_window, text='Materials', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
             activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1,
             command=next_page_to_materials)
btn.place(x=400, y=400)

cd_home_window.mainloop()
