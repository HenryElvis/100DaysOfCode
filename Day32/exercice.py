import smtplib
import datetime as dt
from random import choice

email = "elvishenry2402@gmail.com"
password = "rpwdynumgwfkjdit"

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 0:

    with open("quotes.txt", "r") as quote:
        data = quote.readlines()

    random_quote = choice(data)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="elvishenry2402@gmail.com", password=password)

        connection.sendmail(
            from_addr=email, 
            to_addrs="elvishenry2402@gmail.com", 
            msg=f"Subject:Monday Motivation\n\n{random_quote}.")
