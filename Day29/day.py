from tkinter import *
from tkinter import messagebox
from password import new_password
from pyperclip import copy

def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="MyPass", message="Please don't leave any field empty !")
        return
    
    save_data = messagebox.askquestion(title="MyPass", message="Do you want to save this information ?")
    
    if save_data == "yes":
        with open("data.txt", "a") as data:
            data.write(f"{website} | {email} | {password} \n")
        
        copy(password_entry.get())
        messagebox.showinfo(title="MyPass", message="All save !")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

def password_generation():
    password_entry.delete(0, END)
    password_entry.insert(0, new_password())
    copy(password_entry.get())

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=200, height=200)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username :")
username_label.grid(column=0, row=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

website_entry = Entry(width=54)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=54)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "elvishenry2402@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generation)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add" , width=46, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()