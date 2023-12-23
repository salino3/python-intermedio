
# PIP https://pypi.org

# pip install pip

import numpy # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 17, 30])

print(type(numpy_array))

print(numpy_array * 2)


import pandas # pip install pandas

# pip list

import requests

response_api = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response_api)
print(response_api.status_code)
print(response_api.json())

array_pokemon = response_api.json()

print('----------------------')

print(array_pokemon["results"][0])

# Aritmetics Package

from  my_package import arithmetics

print(arithmetics.sum_two_values(1, 4))



from my_package import other_arithmetics

print(other_arithmetics.sum_two_values(10, 4))










