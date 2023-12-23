
import os

# .txt tile

txt_file = open("./my_file.txt", "w+")
txt_file.write("My name is Giovanni\nMy surname is Doe\n45 years\nI'm workin with Python")


# print(txt_file.read())

# 

print(txt_file.read(10))

# 

print(txt_file.readline())
print(txt_file.readline())

# 

# print(txt_file.readlines())

# 

for line in txt_file.readlines():
    print(line)

# 

txt_file.write("\n\nBut yet I like Kotlin")

txt_file.close()

# for delete the file
# os.remove("./my_file.txt")



#### Other manner for read file .txt

# import os

# file_path = "./my_file.txt"

# full_path = os.path.join(os.getcwd(), file_path)

# with open(full_path, "r") as txt_file:
#     print(txt_file.read())


import json


json_file =  open("./json_file.json", "w+")


json_test = {
    "name": "Joe",
    "surname": "Smith", 
    "age": 45,
    "languages": ["Typescript", "Python", "Swift", "Kotlin"],
    "website": "https://...."
   } 

json.dump(json_test, json_file, indent = 2)

json_file.close()


with open("./json_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("./json_file.json"))


print(json_dict)
print(type(json_dict))
print(json_dict["name"])
print(json_dict["languages"])
print(json_dict["languages"][1])

print('------------------')


# .csv file 

import csv

csv_file =  open("./csv_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Tom", "Smith", 35, "Python", "https://www.google.es"])
csv_writer.writerow(["Tom", "", 40, "Javascript", ""])

csv_file.close()

with open("./csv_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file

# import xlrd # has to be installed




#.xml file

import xml


