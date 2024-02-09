from tkinter import *
from tkinter import ttk

from PIL import ImageTk


def nextPagetoConstruct():
    cd_material_window.destroy()


# Create the Tkinter home_page and run the application
cd_material_window = Tk()
cd_material_window.geometry('1366x768')
# heading
cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/Materials.jpeg')
cd_bg_label = Label(cd_material_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)
# label to be construced
lbl1 = Label(cd_material_window, text="Floors to be constructed", fg='red', font=("Helvetica", 26))
lbl1.place(x=30, y=70)
# combobox
comboa = ttk.Combobox(state="readonly", values=["1", "2", "3", "4"], font=("Helvetica", 19))
comboa.place(x=490, y=70)

# 1a
lbl1a = Label(cd_material_window, text="Concrete", fg='black', font=("Helvetica", 26))
lbl1a.place(x=30, y=210)
txtfld1a = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld1a.place(x=250, y=210, height=40, width=130)
# 1b
lbl1b = Label(cd_material_window, text="Brick", fg='black', font=("Helvetica", 26))
lbl1b.place(x=30, y=290)
txtfld1b = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld1b.place(x=250, y=290, height=40, width=130)
# 1c
lbl1c = Label(cd_material_window, text="Steel", fg='black', font=("Helvetica", 26))
lbl1c.place(x=30, y=370)
txtfld1c = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld1c.place(x=250, y=370, height=40, width=130)
# 1d
lbl1d = Label(cd_material_window, text="Glass", fg='black', font=("Helvetica", 26))
lbl1d.place(x=30, y=450)
txtfld1d = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld1d.place(x=250, y=450, height=40, width=130)
# 2a
lbl2a = Label(cd_material_window, text="Wood", fg='black', font=("Helvetica", 26))
lbl2a.place(x=530, y=210)
txtfld2a = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld2a.place(x=750, y=210, height=40, width=130)
# 2b
lbl2b = Label(cd_material_window, text="Tiles", fg='black', font=("Helvetica", 26))
lbl2b.place(x=530, y=290)
txtfld2b = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld2b.place(x=750, y=290, height=40, width=130)
# 2c
lbl2c = Label(cd_material_window, text="Cement", fg='black', font=("Helvetica", 26))
lbl2c.place(x=530, y=370)
txtfld2c = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld2c.place(x=750, y=370, height=40, width=130)
# 2d
lbl2d = Label(cd_material_window, text="Aggregate", fg='black', font=("Helvetica", 26))
lbl2d.place(x=530, y=450)
txtfld2d = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld2d.place(x=750, y=450, height=40, width=130)

txtfld3a = Label(cd_material_window, text="", fg='black', font=("Helvetica", 26))
txtfld3a.place(x=550, y=560, height=40, width=250)


# creating button estimate
btn1b = Button(cd_material_window, text='Estimate Cost', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
               activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=15, height=1)
btn1b.place(x=250, y=560)

btnback = Button(cd_material_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=nextPagetoConstruct)
btnback.place(x=0, y=0)

cd_material_window.mainloop()
