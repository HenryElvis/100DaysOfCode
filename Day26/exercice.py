from random import randint
import pandas

numbers = [1, 2, 3]
new_list = [n + 2 for n in numbers]

# print(new_list)

name = "Angela"
new_name = [letter for letter in name]

# print(new_name)

new_range = [r * 2 for r in range(1, 5)]
# print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

list_of_name = [n.upper() for n in names if len(n) > 5]
# print(list_of_name)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]

# print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]

# print(result)

with open("file1.txt") as f_file:
    first_file_number = [int(n) for n in f_file.readlines()]

with open("file2.txt") as s_file:
    second_file_number = [int(n) for n in s_file.readlines()]

result = [n for n in first_file_number if n in second_file_number]

# print(result)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_dict  = {student:randint(0, 100) for student in names}

# print(student_dict)

passed_student = {student:value for student, value in student_dict.items() if value >= 60}
# print(passed_student)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()

result = {word:len(word) for word in words}

# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key:(value * 9 / 5) + 32 for key, value in weather_c.items()}

# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student_dict_data = pandas.DataFrame(student_dict)

# for (student, score) in student_dict_data.iterrows():
#     print(score.score)
