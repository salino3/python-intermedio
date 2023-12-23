
import re


my_string = "Esta es la lección número 7: Lección llamada Expressiones regulares"
my_other_string = "Esta no es la lección número 6: Expressiones regulares"



pattern = r"[lL]ección|Expressiones"

print(re.findall(pattern, my_string))


pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-5]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

print('---------------------------')


pattern = r"[0-9]"
print(re.search(pattern, my_string))

# every number
pattern = r"\d"
print(re.findall(pattern, my_string))

# everything is not number
pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

print('-----------------')

email = "mouredev@mourdev.com"
emailSentence = "Mi email es mouredev@mourdev.com acaba con punto com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print(re.findall(pattern, email))
print(re.match(pattern, email))
print(re.search(pattern, email))

print('-------------------')

pattern = r"^[a-zA-Z0-9_.+-]+@@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# +$ or .*
pattern = r"^[a-zA-Z0-9_.+-]+@@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.].*"


email = "mouredev@@mourdev.es.mx"

print(re.findall(pattern, email))
print(re.match(pattern, email))
print(re.search(pattern, email))


# good web about regex: https://regex101.com/



