import pandas as pd
import datetime as dt
from random import randint
import smtplib

EMAIL = "elvishenry2402@gmail.com"
PASSWORD = "rpwdynumgwfkjdit"

birthday = pd.read_csv("birthdays.csv")
birthday = birthday.to_dict(orient="records")

current_date = dt.datetime.now()

day = current_date.day
month = current_date.month

user_birthday = []
message = []

for _ in range(0, len(birthday)):
    if birthday[_]["month"] == month:
        if birthday[_]["day"] == day:
            user_birthday.append(birthday[_])

for user in user_birthday:
    random_letters = f"./letter_templates/letter_{randint(1, 3)}.txt"

    name = user["name"]
    email = user["email"]

    with open(random_letters, "r") as letter:
        content = letter.read()
        message.append(content.replace("[NAME]", name))

for i in range(len(user_birthday)):

    email = user_birthday[i]["email"]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs= email,
            msg=f"Subject:Birthday\n\n{message[i]}")