# Bucles

# Bucle While

my_variable = 0

while my_variable <= 5 :
    print(my_variable)
    my_variable += 1
else:           # se pueden poner else a los bucles while !!!  Opcional

    print("Mi variable es mayor que 5")

my_variable = 5

while my_variable > 0:
    print(my_variable)
    my_variable -= 1
else:
    print("Mi variable al final del bucle es" , my_variable)


while my_variable < 10:
    if my_variable == 5:
        print("Mi variable vale 5")
    print(my_variable)
    my_variable += 1
else:
    print("tienes un", my_variable)

my_variable = 0

while my_variable < 10:
    if my_variable == 5:
        print("Mi variable vale 5")
        break # para la finalizar el flujo, tambien se salta los else
    print(my_variable)
    my_variable += 1
else:
    print("tienes un", my_variable)

#FOR

my_list = [31, 1.82, "diego", "garcia"]
my_tupla = (31, 1.82, "diego", "garcia")
my_set = {31, 1.82, "diego", "garcia"}
my_dict = {
    "edad":31,
    "altura":1.82,
    "nombre":"diego",
    "apellido":"garcia"}

for element in my_list: # iterar una lista
    print(element)

for element in my_tupla: # iterar una tupla
    print(element)

for element in my_set: # iterar un conjunto
    print(element)

for element in my_dict: # iterar un diccionario (Solo coge las claves)
    print(element)

for element in my_dict.values(): # iterar un diccionario (Solo coge los valores)
    print(element)
else:
    print("El bucle for ha finalizado") # Se puede poner else al finalizar el bucle for

for element in my_list: 
    print(element)
    if element == "diego":
        continue # continua volviendo al for
    print("se ejecuta")