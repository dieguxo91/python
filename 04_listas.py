# Listas

# Declarar listas
my_list = list()
other_list = []

my_list = [32, 5, 13, 26]

print(my_list)
print(len(my_list))

other_list = [31, 1.82, "diego", "garcia"]

print(other_list)
print(len(other_list))
print(type(other_list)) # tipo list

print(other_list[0])
print(other_list[-4]) # podemos utilizar negativo para empezar por el final, solo tendria de indice negativo los mismo que de longitud
print(other_list[::-1]) # dar la vuelta a la lista, como los string que son arrays de caracteres 
print(other_list.count("hola")) # nos dice las veces que se encuentra el valor en la lista

# guardar array en variables, todas a la vez (cuidado tiene que tener el mismo número de variables)
age, height, name, surname = other_list
print(name)
print(age)

# tambien se puede hacer asi, pero es mas lioso
age, height, name, surname = other_list[0],  other_list[1],  other_list[2],  other_list[3]

print(name)
print(age)

# concatenar listas o sacar las dos por pantalla
print(my_list , other_list)
print(my_list + other_list)

# se pueden pisar los tipos de las variables list
my_list = 2
print(my_list)
print(type(my_list))

