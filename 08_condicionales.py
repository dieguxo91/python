# condicionales

# tablas de verdad igual que en otros lenguajes, manera de declarar diferente

my_condition = False
# my_condition = True

 # IF
if my_condition :
    print("Se ejecuta la condicion del if")

print("La ejecución continua")

my_condition = 5 * 2

if my_condition == 10:
    print("la condición 2 funciona")

# IF ELSE

if my_condition > 10: 
    print("Es mayor que 10")
else:
    print("no es mayor que 10")

if my_condition >= 10 and my_condition < 20:
    print("la condición 4 funciona")
else:
    print("no entro en la condición 4")    

if my_condition > 10 or my_condition < 20:
    print("la condición 5 funciona")
else:
    print("no entro en la condición 5")   

# ELIF     

if my_condition > 10 and my_condition < 20:
    print("esta entre 10 y 20")
elif my_condition == 10:
    print("es igual a 10")
else:
    print("no es igual que ni ni esta entre 10 y 20")    

my_string = "Mi cadena de texto"

if my_string == "Mi cadena de texto" :
    print("Cadenas de texto iguales")

other_string = ""

if not(other_string): # si no tiene ningun caracter se considera vacia
    print("La cadena esta vacia")