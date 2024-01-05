
#data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(len(temp_list))

# Get average temperature
#print(data["temp"].mean())

#print(data["temp"].max())
# pandas turns column names into attributes
#print(data.condition)

# Get data in rows
#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

# def convertToCelsius(degrees):
#     result = (degrees * 9/5) + 32
#     return result

# monday = data[data.day == "Monday"]
#print(monday.condition)

# monday_temp = int(monday.temp)
# print(convertToCelsius(monday_temp))


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#######################################

import pandas
# Figure out how many of each color squirrel (my solution)

# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color_count = squirrel_data["Primary Fur Color"].value_counts()
# fur_color_data = pandas.DataFrame(fur_color_count)
# fur_color_data.to_csv("fur_color_data.csv")

# Video solution
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") 
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

fur_data = pandas.DataFrame(data_dict)
fur_data.to_csv("fur_data.csv")



