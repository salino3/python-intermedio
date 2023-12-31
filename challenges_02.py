
### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

array = range(100)

def fizz_buzz():
    for index in range(1, 101):
      if index % 3 == 0 and index % 5 == 0:
         print("FizzBuzz")
      elif index % 3 == 0:
         print("Fizz")
      elif index % 5 == 0:
         print("Buzz")
      else:
         print(index)    


# fizz_buzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def is_anagrama(word_one, word_two):
   word_one_lower = word_one.lower()
   word_two_lower = word_two.lower()

   if word_one_lower == word_two_lower:
      return False
   return sorted(word_one_lower) == sorted(word_two_lower)
   


# print(is_anagrama("amor", "roma"))
# print(is_anagrama("amor", "London"))
# print(is_anagrama("amor", "Amor"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci(prev = 0, loops = 50):
   
   initialPrev = prev
   
   next = prev
   if(prev < 0):
      next = initialPrev - 1
   else:
      next = initialPrev + 1

   for index in range(loops):
        if initialPrev == 0:
            print("Index: ", index, "- Number: ", prev)
            fib = prev + next
            prev = next
            next = fib
        else:
           if initialPrev == prev:
             print("Index: ", index, "- Number: ", prev)
             fib = prev + next
             prev = next
             next = fib         
           else:
             print("Index: ", index, "- Number: ", fib)
             fib = prev + next
             prev = next
             next = fib
   print('----------------')


# fibonacci(-5)

# fibonacci()

# fibonacci(0, 100)

# fibonacci(5)


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def isPrime(number = 0, loop = 100):

    for number in range(number, loop):
      if number >= 2:
        is_divisible = False

        for index in range(2, number):
            if number % index == 0:
              is_divisible = True
              break

        if not is_divisible:
            print(number)
    print('--------------------')
       

# isPrime()

# isPrime(8)

# isPrime(10, 120)


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def reverseWords(text):

   text_len = len(text)
   reverse_text = ""
   for index in range(0, text_len):
     reverse_text += text[text_len - index - 1]
   return reverse_text


print(reverseWords("Buenas Noches"))

# #
def reverseString(text):

   reverse_text = ""
   wordRevers = text[::-1]
   for index in range(0, len(text)):
     reverse_text += wordRevers[index]
   return reverse_text


print(reverseString("Hola mundo"))


