from tkinter import *

def convert():
    current_miles = float(miles.get())
    result = round(current_miles * 1.609)
    km.config(text=result)

window = Tk()
window.minsize(width=500, height=200)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles = Entry(width=20)
miles.grid(column=1, row=0)
miles.focus()

label_miles = Label(text="Miles", font=("Arial", 24, "normal"))
label_miles.grid(column=2, row=0)
label_miles.config(padx=30, pady=0)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "normal"))
is_equal_label.grid(column=0, row=1)

km = Label(text="0", font=("Arial", 18, "normal"))
km.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 24, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=30, pady=0)

button = Button(text="Calculate", font=("Arial", 24, "normal"), command=convert)
button.grid(column=1, row=2)

window.mainloop()