from tkinter import *
import os

root=Tk()


t_frame = Frame(root)
b_frame = Frame(root)


def login():
    correct_password = 'admin'
    input_password=E2.get()
    input_username=E1.get()
    if correct_password == input_password and correct_password==input_username:
        root.quit()
        os.system('demo.py')

    else:
        lab11=Label(t_frame,text='Username and Password incorrect',fg='RED')
        E1.delete(0, END)
        E2.delete(0,END)
        lab11.pack()


i_var = PhotoImage(file="background.PNG")
lab = Label(t_frame, image=i_var)
lab.pack(side=TOP)
lab1 = Label(b_frame, text="USERNAME:")
lab2 = Label(b_frame, text="PASSWORD:")

E1 = Entry(b_frame)
E2 = Entry(b_frame)
E2.config(show="*")

b1 = Button(b_frame, text="SUBMIT", fg="GREEN",command=login)
t_frame.pack(side=TOP)
b_frame.pack(side=BOTTOM)
lab1.grid(row=0, column=0)
E1.grid(row=0, column=1)
lab2.grid(row=1, column=0)
E2.grid(row=1, column=1)
b1.grid(row=2, column=1)


root.mainloop()

