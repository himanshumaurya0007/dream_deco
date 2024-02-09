from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk

def display_popup():
    if not Email.get() or not combo_1.get()  or not Width.get():
        messagebox.showerror("Error", "Please enter all values!")
    else:
        messagebox.showinfo("Payment Pop-Up", "Your Payment is Successful. Your Project will be emailed to you shortly. Thanks!")

cd_ub2_window = Tk()
cd_ub2_window.geometry('1366x768')
cd_ub2_window.title('Urbanovate 1')
cd_ub2_window.iconbitmap('')
cd_ub2_window.resizable(False, False)


cd_bg_image = ImageTk.PhotoImage(file='../resources/images_resources/ub-2.jpeg')
cd_bg_label = Label(cd_ub2_window, image=cd_bg_image)
cd_bg_label.place(x=0, y=0)


lbl1 = Label(cd_ub2_window, text='Email', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl1.place(x=90, y=300)

Email = Entry(cd_ub2_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Email.place(x=300, y=300)

lbl2 = Label(cd_ub2_window, text='Phone No.', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl2.place(x=90, y=400)

Width = Entry(cd_ub2_window, width=21, font=('Times New Roman', 20, 'bold'), bd=0, fg='purple')
Width.place(x=300, y=400)

lbl3 = Label(cd_ub2_window, text='Payment Option', font=("Helvetica", 26),bg='bisque2',fg='black')
lbl3.place(x=34, y=500)

combo_1 = ttk.Combobox()
combo_1 = ttk.Combobox(state="readonly", values=["Credit Card", "UPI ", "Debit Card" ], font=("Helvetica", 19))
combo_1.place(x=300, y=500)

btn_done = Button(cd_ub2_window, text='Done', font=('Open Sans', 20, 'bold'), fg='white', bg='firebrick1',
                 activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=8, height=1,
                 command=display_popup)
btn_done.place(x=300, y=600)



cd_ub2_window.mainloop()