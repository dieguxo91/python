# Excepciones

number_one, number_two = 5, 1

number_two = "1"

# Try - Except
try :
    print(number_one + number_two)
except:
    print("Se ha producido un error")

# Try - Except - Else (Opcional)
try :
    print(number_one + number_two)
except:
    print("Se ha producido un error")
else: # Solo se lee si no se ha producido el error (Excepción)
    print("La ejecución continúa correctamente")

# Try - Except - Finnaly (Opcional)

try :
    print(number_one + number_two)
except:
    print("Se ha producido un error")
finally: # Se lee indistintamente de si se produce la excepción o no
    print("La ejecución continúa correctamente")

# Tipos de errores (se pueden poner varios except)

try :
    print(number_one + number_two)
except TypeError: # este bloque solo se ejecuta si se produce un error de tipo
    print("Se ha producido un error")
except ValueError: # este bloque solo se ejecuta si se produce un error de valores
    print("Se ha producido un error")

# Captura de la información de la excepción

try :
    print(number_one + number_two)
except Exception as error: # se captura en una variable
    print(error)