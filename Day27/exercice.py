from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = Label(text="First Label", font=("Arial", 24, "bold"))
# label.place(x=0, y=0)
label.grid(column=0, row=0)

label["text"] = "New Text"
label.config(text="Again New Text")

def button_clicked():
    label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

second_button = Button(text="new button")
second_button.grid(column=2, row=0)

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

print(input.get())

window.mainloop()

def add(*args):
    result = [n for n in args]
    # print(sum(result))

add(1, 2, 5, 6, 25, 7, 9)

def calculate(n, **kwargs):
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]

    # print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

car = Car(make="Nissan", model="GT-R")
# print(car.make)
# print(car.model)
# print(car.color)