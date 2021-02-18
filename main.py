import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

root = tkinter.Tk()

root.geometry("400x150")
root.title('All About Toys For Admin')

#declaring the frames
regframe = tkinter.Frame(root)
mainframe = tkinter.Frame(root)
logframe = tkinter.Frame(root)

#using the mainframe as the firstpage, which is the page the user has to input their username and password
mainframe.pack(fill='both', expand=1)

#the label of the first page that says "login"
first = tkinter.Label(mainframe, text="Login", font=('arial', 15))
first.grid(row=0, column=1, columnspan=3, sticky='w', padx=70)

#user label
user = tkinter.Label(mainframe, text='Username')
user.grid(row=1, column=0)

#password label
password = tkinter.Label(mainframe, text='Password')
password.grid(row=2, column=0)

#textbox for the username
user_entry = ttk.Entry(mainframe, width=45)
user_entry.insert(0, 'Username...')
user_entry.grid(row=1, column=1)

#textbox for the password
password_entry = ttk.Entry(mainframe, width=45, show="*")
password_entry.insert(0, 'Password...')
password_entry.grid(row=2, column=1)

#register button
btn_reg = tkinter.Button(mainframe, text="Register")
btn_reg.grid(row=3, column=0, pady=20)

#login button
btn_login = tkinter.Button(mainframe, text="Login")
btn_login.grid(row=3, column=1, pady=20)

#quit button
btn_quit = tkinter.Button(mainframe, text="Exit")
btn_quit.grid(row=3, column=2, pady=20)

#back button after logging in
btn_backfromlog = tkinter.Button(logframe, text="Back")
btn_backfromlog.grid(row=3, column=2, pady=20)

#back button while in the register page, which will bring to the login page
btn_backfromreg = tkinter.Button(regframe, text="Back")
btn_backfromreg.grid(row=3, column=2, pady=20)

root.mainloop()