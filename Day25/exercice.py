import csv
import pandas

# data = []

# with open("weather-data.csv") as d:
#     data.append(d.readlines())

# print(data)

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)

#     temperature = []
#     for d in data:
#         if d[1] != "temp":
#             temperature.append(int(d[1]))
    
#     print(temperature)

#     for d in data:
#         print(d)

# data = pandas.read_csv("weather-data.csv")

# tem_list = data["temp"].to_list()
# print(sum(tem_list) / len(tem_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

# data_dict = {
#     "names" : ["Amy", "James", "Angela"],
#     "scores" : [75, 56, 65]
# }

# dict_to_data = pandas.DataFrame(data_dict)
# print(dict_to_data)

# dict_to_data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("Squirrel-data.csv")

squirrel_color = squirrel_data["Primary Fur Color"]

squirrel_grey = len(squirrel_data[squirrel_color == "Gray"])
squirrel_black = len(squirrel_data[squirrel_color == "Black"])
squirrel_cinamon = len(squirrel_data[squirrel_color == "Cinnamon"])

data_color = {
    "color" : ["red", "black", "grey"],
    "counts" : [squirrel_cinamon, squirrel_black, squirrel_grey]
}

data_squirrel_color = pandas.DataFrame(data_color)
data_squirrel_color.to_csv("squirrel_color.csv")