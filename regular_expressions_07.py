
import re
# It starts to look for from the start of string


my_string = "Esta es la lección número 7: Lección llamada expressiones regulares"
my_other_string = "Esta no es la lección número 6: Expressiones regulares"



print(re.match("Esta es la lección", my_string))

print(re.match("Esta es la lección", my_other_string))

print(re.match("Expressiones regulares", my_string))

print('---------------------')

match = re.match("Esta es la lección", my_string, re.I)

print(match)

print(match.span())

print('-------------------.')

match = re.match("Esta es la lección", my_string)

if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])



print('------------------')

start, end = match.span()

print(start)
print(end)
print(my_string[start:end])


print('--------------------.')

# search

search = re.search("lección", my_string, re.I)

print(search)

start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)

print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("expressiones", "Expressiones", my_string))

print(re.sub("lección|Lección", "LECCIÓN", my_string, re.I))

print(re.sub("[l|L]ección", "LECCIÓN", my_string, re.I))

print(re.sub("Expressiones regulares", "regex", my_other_string, re.I))


print('------------------')


import re

my_string = "Esta es la lección número 7: Lección llamada expressiones regulares"

# Definir una función de reemplazo personalizada
def custom_replace(match):
    global replaced_count
    replaced_count += 1
    if replaced_count == 2:
        return match.group(1).upper()
    return match.group(0)

# Inicializar el contador
replaced_count = 0

# Utilizar re.sub con la función de reemplazo personalizada
result = re.sub(r"([l|L]ección)", custom_replace, my_string, flags=re.I)

# Imprimir el resultado
print(result)

print('-----------------------')





