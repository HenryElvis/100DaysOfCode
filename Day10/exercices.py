from calendar import isleap
from re import M


def Format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Invalid input"

    f_name = f_name.title()
    l_name = l_name.title()

    return f_name + ' ' + l_name

#print(Format_name(input("What is your first name ? - "), input("What is your last name ? - ")))

def is_leap(year):
    """Return bool if year is leap or not. Take year in parametter"""
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m < 1 or m > 12:
        return "Invalid input"
    
    if m == 2:
        if is_leap(y):
            return 29

    return month_days[m -1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
#print(days)