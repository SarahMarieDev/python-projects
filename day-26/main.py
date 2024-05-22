# from coding exercise: Data Overlap
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
#
# print(result)

# coding exercise: Dictionary Comprehension 1
# Use Dictionary Comprehension to create a dictionary
# that takes each word in the given sentence and calculates
# the number of letters in each word.
# sentence = input()
# result = {word: len(word) for word in sentence.split()}
# print(result)

# coding exercise: Dictionary Comprehension 2
# Use Dictionary Comprehension to create a dictionary
# called weather_f that takes each temperature in degrees
# Celsius and converts it into degrees Fahrenheit.
# weather_c = eval(input())
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# Iterate over a Pandas dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
        
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}