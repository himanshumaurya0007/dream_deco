from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk


cd_ub1_window = Tk()
cd_ub1_window.geometry('1366x768')
cd_ub1_window.title('Urbanovate 1')
cd_ub1_window.iconbitmap('')
cd_ub1_window.resizable(False, False)

cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/ub-1.jpeg')
cd_bg_label = Label(cd_ub1_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)

def ub2():
    cd_ub1_window.destroy()
    import Urbanovate_2

def next_page_to_materials():
    cd_ub1_window.destroy()

def display_popup():
    if not Rad.get() or not Height.get() or not Br.get() or not Width.get():
        messagebox.showerror("Error", "Please enter all values!")
    else:
        cd_ub1_window.destroy()
        import Urbanovate_2

# functions
def go_to_page():
    cd_ub1_window.destroy()


def next_page_to_home():
    cd_ub1_window.destroy()

def ub1():
    cd_ub1_window.destroy()
    import home_page

lbl = Label(cd_ub1_window,  bg='bisque2',width=105,height=120)
lbl.place(x=0, y=0)



# label floor
lbl1 = Label(cd_ub1_window, text='Enter Area Radius', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl1.place(x=20, y=100)
# text field of floor

Rad = Entry(cd_ub1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Rad.place(x=400, y=100)

btn_back = Button(cd_ub1_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=ub1)
btn_back.place(x=0, y=10)

lbl1 = Label(cd_ub1_window, text='Enter No. Of Houses', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl1.place(x=20, y=170)

Height = Entry(cd_ub1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Height.place(x=400, y=170)

lbl1 = Label(cd_ub1_window, text='Enter Other Req.', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl1.place(x=20, y=240)

Width = Entry(cd_ub1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Width.place(x=400, y=240)

lbl1 = Label(cd_ub1_window, text='Specify', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl1.place(x=90, y=310)

Br = Entry(cd_ub1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Br.place(x=400, y=310)

btn_paynow = Button(cd_ub1_window, text='Pay Now', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=display_popup)
btn_paynow.place(x=200, y=400)

cd_ub1_window.mainloop()
