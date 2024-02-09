from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk

# Create the Tkinter  and run the application
cd_int1_window = Tk()
cd_int1_window.geometry('1366x768')
cd_int1_window.title('Interior 1')
cd_int1_window.iconbitmap('')
cd_int1_window.resizable(False, False)


cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/int-1.jpeg')
cd_bg_label = Label(cd_int1_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)


def display_popup():
    if not Req.get() or not Height.get() or not Br.get() or not Width.get():
        messagebox.showerror("Error", "Please enter all values!")
    else:
        cd_int1_window.destroy()
        import interior_2


def next_page_to_materials():
    cd_int1_window.destroy()


# functions
def go_to_page():
    cd_int1_window.destroy()


def next_page_to_home():
    cd_int1_window.destroy()

def ub1():
    cd_int1_window.destroy()
    import home_page

lbl = Label(cd_int1_window,  bg='blue2',width=105,height=120)
lbl.place(x=0, y=0)



# label floor
lbl1 = Label(cd_int1_window, text='Select Product', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=100)
# text field of floor
combo_2 = ttk.Combobox()
combo_2= ttk.Combobox(state="readonly", values=["House", "Hospital", "School" ], font=("Helvetica", 19))
combo_2.place(x=400, y=100)


btn_back = Button(cd_int1_window, text='Back', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=ub1)
btn_back.place(x=0, y=10)

lbl1 = Label(cd_int1_window, text='Dimensions', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=170)

lbl1 = Label(cd_int1_window, text='Height', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=240)

Height = Entry(cd_int1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Height.place(x=400, y=240)

lbl1 = Label(cd_int1_window, text='Width', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=310)

Width = Entry(cd_int1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Width.place(x=400, y=310)

lbl1 = Label(cd_int1_window, text='Breadth', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=380)

Br = Entry(cd_int1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Br.place(x=400, y=380)

lbl1 = Label(cd_int1_window, text='Area', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=450)

Ar = Entry(cd_int1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Ar.place(x=400, y=450)

lbl1 = Label(cd_int1_window, text='Requirements', font=("Helvetica", 26),bg='black',fg='white')
lbl1.place(x=90, y=520)

Req = Entry(cd_int1_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Req.place(x=400, y=520)

btn_paynow = Button(cd_int1_window, text='Pay Now', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=display_popup)
btn_paynow.place(x=90, y=590)

cd_int1_window.mainloop()
