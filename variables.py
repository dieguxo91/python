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

#Pruebas con funciones predeterminadas
print(len(my_variable))
print(len(my_int_to_str_variable))
print("mi cadena tiene una longitud de:", len(my_variable))

#variables en una sola linea
name, surname, alias, age = "diego", "garcía", "dieguxo", "32"
print("mi apellido:", surname, "mi nombre:", name, "mi edad:", age, "mi alias:", alias)