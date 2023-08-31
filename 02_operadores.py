# Operadores Aritméticos

print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicación
print(3 / 4) # división
print(10 % 3) # modulo (resto)
print(10 // 3) # aproximacion de división (Redondeo de numero entero para el resultado)
print(2 ** 3) # exponente

print("hola " + "python") # concatenación de cadenas

# no se puede concatenar distintos tipos
# print("hola " + 5) # forma incorrecta
print("hola " + str(5)) # forma correcta

# multiplica la cadena por el numero de veces que se haya puesto (solo enteros)
print("hola " * 5) 
print("hola " * (2 **3)) 



# Operadores Comparativos

print(3 > 4) # mayor
print(3 < 4) # menor
print(3 <= 4) # menor igual
print(3 >= 4) # mayor igual
print(3 == 4) # igual
print(3 != 4) # distinto

# compara por ASCII
print("hola" < "python")
print("hola" > "python")
print("hola" <= "python")
print("hola" >= "python")
print("hola" == "python")
print("hola" != "python")


# Operadores Lógicos

"""
las palabras reservadas para ello son :
        - and
        - or
        - not()
"""
# pruebas de logica
print(3 > 4 and "hola" > "python") 
print(3 > 4 or "hola" > "python") 
print(3 < 4 and "hola" < "python") 
print(3 > 4 or "hola" < "python") 
print(not(3 > 4))


