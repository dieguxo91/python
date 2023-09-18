# Sets

# declarar conjuntos
my_set = set()
other_Set = {} # tipado debil

print(type(my_set)) # type set
print(type(other_Set)) # inicialmente es un diccionario

other_Set = {"diego", "garcia", 32}
print(type(other_Set)) # al insertar los datos se convierte en un conjunto (set)

print(len(other_Set))

# print(other_Set[0]) # esto no podriamos hacerlo como en las listas

other_Set.add(1.82)
print(other_Set) # un set no es una estructura ordenada

other_Set.add(1.82) # igual que en otros lenguajes no se pueden repetir
print(other_Set) 

print("paco" in other_Set) # para realizar busquedas utilizamos el in
print("diego" in other_Set)

other_Set.remove("diego") # si podemos borrar cualquier elemento
print(other_Set)

other_Set.clear() # vacia todos los elementos
print(len(other_Set))

del other_Set # nos cargamos la variable
# print(other_Set) # ya no estaria la variable

my_set = {"diego", "garcia", 31}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # ya si podemos acceder al elemento por su indice

other_Set = {"Kotlin", "swift", "python", 31} # concatena los conjuntos pero no se duplican si estan repetidos
my_new_set = my_set.union(other_Set)
print(my_new_set)

print(my_new_set.union({"calle jose moreno"})) # no se guardaria en la variable, cuidado!!

print(my_new_set.difference(my_set))

