# tipos de errores (controladores de errores)

try:
    print("hola")
except:
    print("error")

# SyntaxError   (Algo mal escrito, la consola nos dice lo que esta mal)
# print "Hola comunidad"
print ("Hola comunidad")

# NameError    (Variable no existe)
# print(name)
name = "diego"
print(name)

# IndexError     (Fuera del indice de la lista)
my_list = [1,2,3,4]
# print(my_list[4])
print(my_list[3])

# ModulesNotFoundError   (importar un modulo erroneo)
# import maths
import math

# AttributeError     (El atributo de la clase no existe)
# print(math.PI)
print(math.pi)

# KeyError     (Nombre de la key del diccionario incorrecta)
my_dict = {"nombre":"diego", "apellido":"garcia", "edad":31, 1:"python"}
# print(my_dict["name"])
print(my_dict["edad"])

# TipeError     (el indice deberia ser un entero, al meter un string nos da un error de tipo)
print(my_list[1])
# print(my_list["nombre"])

# importError     (error al importar una función de un modulo, no existe
# from math import PI
from math import pi as number_pi   # se le pueden poner alias a las funciones importadas
print(number_pi)

# ValueError     (Error cuando casteamos un cadena, no se puede convertir el valor que se pasa como parametro)
# my_int = int("10 años")
# print(my_int)

#ZeroDivisionError
# print(4/0)
print(4/2)