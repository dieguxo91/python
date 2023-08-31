# Variables en python

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# las cadenas se pueden concatenar con comas ','

print(my_variable, my_int_variable, my_bool_variable)
print("este es el valor de :", my_bool_variable)

# Pruebas con funciones predeterminadas
print(len(my_variable))
print(len(my_int_to_str_variable))
print("mi cadena tiene una longitud de:", len(my_variable))

"""
variables en una sola linea. 
Se puede usar pero es peligroso 
por equivocarse con la posición.
"""
name, surname, alias, age = "diego", "garcía", "dieguxo", "32"
print("mi apellido:", surname, "mi nombre:", name, "mi edad:", age, "mi alias:", alias)

# Función Input
name = input("¿Como te llamas? ") # utilizamos la variable anterior y machacariamos el valor 
age = input("¿Que edad tienes? ")

print("Su nombre es:", name)
print("Su edad es:", age)

# Cambiamos su tipo, El tipado de python no es fuerte
name = 123
age = "paco"
print("Su nombre es:", name)
print("Su edad es:", age)

# podemos "forzar" el tipo de dato
address : str = "Mi dirección"
address = 123
print(type(address)) # de resultado nos saldria 'int' , ya que aunque pongamos el tipo se puede cambiar

