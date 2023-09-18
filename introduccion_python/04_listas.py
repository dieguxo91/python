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

my_list = [32, 5, 13, 26]

# Funciones
other_list.append("calle jose moreno") # inserta por el final
print(other_list)

other_list.insert(1, "paco") # inserta en la posición indicada
print(other_list)

other_list.remove("paco") # elimina el primer elemento si se encuentra en la lista
print(other_list)

other_list.pop() # elimina el ultimo elemento
print(other_list)

other_list.pop(0) # elimina el elemento por su indice que indiques en el metodo
print(other_list)
del other_list[0] # esto es igual que lo hecho arriba
print(other_list)

my_new_list = my_list.copy() # copia la lista y se hace independiente, no va con referencias
my_list.clear() # vacia la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # dar la vuelta a la lista
print(my_new_list)

my_new_list.sort() # ordenar la lista con o sin criterios
print(my_new_list)

print(my_new_list[1:2]) # cortar por un indice en concreto, en este caso es del 1 al 2 



