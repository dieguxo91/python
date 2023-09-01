# Tuplas

# declarar tupla
my_tuple = tuple()
other_tuple = ()

my_tuple = (31, 1.82, "diego", "garcia")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

# Funciones 
print(my_tuple.count("garcia"))
print(my_tuple.index("diego"))

# my_tuple[1] = 1.80 # son valores constantes, una vez creada de una forma no la podriamos editar
# del my_tuple[1] # al ser "constantes" no podemos borrar ningun valor
print(my_tuple)

other_tuple = (23, 45, "tupla")
my_sum_tuple = my_tuple + other_tuple
print(my_sum_tuple) # si podemos combinar las tuplas

my_tuple = list(my_tuple) # se puede cambiar el tipo asi de facil
print(type(my_tuple))

my_tuple[1] = 1.80 # ya si podriamos modificar los datos
print(my_tuple)

my_tuple = tuple(my_tuple) # podriamos cambiar el tipo despues de modificarla
print(type(my_tuple))

del my_tuple # con el del podemos eliminar la variable, ya no esta definida
print(my_tuple)