
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
    "age": {
        "mario": 34,
        "luigi": 23
    },
    "language": "Typescript",
    "website": "https://...."
   } 

json.dump(json_test, json_file, indent = 2)











