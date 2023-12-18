
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

def fibonacci(prev = 0):
   
   initialPrev = prev
   
   next = prev
   if(prev < 0):
      next = initialPrev - 1
   else:
      next = initialPrev + 1

   for index in range(50):
        if initialPrev == 0:
            print("Index: ", index, "Number: ", prev)
            fib = prev + next
            prev = next
            next = fib
        else:
           if initialPrev == prev:
             print("Index: ", index, "Number: ", prev)
             fib = prev + next
             prev = next
             next = fib         
           else:
             print("Index: ", index, "Number: ", fib)
             fib = prev + next
             prev = next
             next = fib
   print('----------------')

   
 
fibonacci(-5)

fibonacci()

fibonacci(5)
