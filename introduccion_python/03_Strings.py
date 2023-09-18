# Strings

# Salto de linea y tabulación
my_new_line_string = "este es un string\ncon salto de linea"
my_new_line_tabulador = "este es un string\tcon tabulación"
print(my_new_line_string)
print(my_new_line_tabulador)

# sirven los dos tipos de comillas
my_string = "mi String"
my_other_string = 'mi String2'

# Funciones de cadenas Algunos ejemplos

print(len(my_string))
print(my_string.capitalize()) # pone la primera en mayúsculas
print(my_string.upper()) # pone la palabra en mayúsculas
print(my_string.count("S")) # cuentas las veces que se encuentra
print(my_string.isnumeric()) # nos dice si es numerico
print("1".isnumeric())
print(my_string.lower()) # todo a minúscula
print(my_string.upper().isupper()) # nos dice si esta en mayúsculas
print(my_string.startswith("mi")) # la cadena empieza con...


# Formateo

"""
    %s usado para string
    %d usado para numeros
"""

name, surname, age = "Diego", "García", 31

print("Mi nombre es {} {} y mi edad es {}".format(name,surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age) )
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de carácteres

word = "hola"
a,b,c,d = word
print(a)
print(b)
print(c)
print(d)

#División

word_slice = word[1:3] # [ empieza en 1 hasta el 3 ] posiciones 1 y 2
print(word_slice)
word_slice = word[1:] # [ empieza en 1 hasta lenght ] 
print(word_slice)
word_slice = word[-2] # [ empieza por el final ] seria la posición penúltima 
print(word_slice)
word_slice = word[0:4:3] # toda la cadena (puedes coger la parte que te interese) y saltando el numero final
print(word_slice)


#Reverse

word_reversed = word[::-1] # empieza por el final
print(word_reversed)
