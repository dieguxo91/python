# Diccionarios

# declarar diccionarios sirvern para guardar datos de tipo clave - valor 
my_dict = dict()
other_dict = {}

print(type(my_dict))
print(type(other_dict))

other_dict = {"nombre":"diego", "apellido":"garcia", "edad":31, 1:"python"} # se insertan igual que si fuera un JSON
print(other_dict)

my_dict = {
    "nombre":"diego",
    "apellido":"garcia",
    "edad":31,
    "lenguajes":{"python","java","javaScript"}
}

print(my_dict)
print(len(my_dict))

print(my_dict["nombre"]) # para acceder a cualquier elemento tenemos que poner la clave
my_dict["nombre"] = "paco"
print(my_dict["nombre"])

del my_dict["nombre"] # para eleminar un elemento del diccionario
print(my_dict)

print("garcia" in my_dict) # no encuentra los valores
print("apellido" in my_dict) # encuentra las claves

print(my_dict.items()) # nos devuelve el diccionario claves y valores
print(my_dict.keys()) # nos devuelve las claves
print(my_dict.values()) # nos devuelve los valores

my_new_dict = my_dict.fromkeys(("apellido", "edad")) # crea un diccionario nuevo con las claves que queramos, estaran vacias
my_new_dict["apellido"] = "fuentesal"
my_new_dict["edad"] = 31
print(my_new_dict)
print(my_dict)

my_new_dict = dict.fromkeys(my_dict) # Podriamos pasar todo el diccionario sin sus valores
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("diego")) # si ponemos un diccionario y un valor se añadira a todas las claves
print(my_new_dict)

print(list(my_dict)) # al transformalo a lista solo nos quedariamos con las claves
print(list(my_dict.values())) # al transformalo a lista con values solo nos quedariamos con los valores
print(type(my_dict.values())) # type dict_values





