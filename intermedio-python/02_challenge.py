# esto es una prueba

"""
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def multiplos(number):
    multiple_words = ["fizz", "buzz", "fizzbuzz"]
    if number % 3 == 0 and number % 5 == 0:
        return multiple_words[2]
    elif number % 3 == 0:
        return multiple_words[0]
    elif number % 5 == 0:
        return multiple_words[1]
    else:
        return number


my_list = [multiplos(i) for i in range(1, 101)]
print(my_list)