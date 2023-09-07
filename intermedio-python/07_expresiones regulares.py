# Regular expressions

import re # modulo de regular expression

my_string = "Esta es la lección 7: Lección llamada Expresiones Regulares 1"
other_string = "Esta no es la lección número 6 : Manejo de ficheros"

# re.I I es Ignore case, para mas atributos mirar el modulo re que esta documentado

# match

match = re.match("Esta es la lección", my_string, re.I) # match empieza la busqueda desde el principio de la cadena
print(match)
start, end = match.span() # span devuelve una tupla, guardamos los indices en unas variables para poder usarlos 
print(my_string[start:end])

match = re.match("Esta es la lección", other_string) # sino la encuentra nos devuelve "none"
if match is not None: # se puede negar con not() "Distinto a java recuerda" o != 
    print(match)
    start, end = match.span() 
    print(other_string[start:end])

# print(re.match("Expresiones Regulares", my_string) )

# search

search = re.search("lección", my_string, re.I) # search busca en toda la cadena y devuelve la primera coincidencia
print(search)
start, end = search.span() # span devuelve una tupla, guardamos los indices en unas variables para poder usarlos 
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I) # devuelve un listado con las veces que lo ha encontrado
print(findall)

# split
print(re.split(":", my_string)) # separa la cadena cuando encuentre el delimitador que nosotros queramos y devuelve una lista

# sub

print(re.sub("Expresiones", "expresiones", my_string)) # sustituye una parte de la cadena que queramos
print(re.sub("[l|L]ección", "LECCIÓN", my_string)) # si queremos cambiar alguna que empiece por mayuscula y otra por minuscula

# patterns

pattern = r"[l|L]ección"
print(re.findall(pattern,my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern,my_string))

pattern = r"[a-zA-Z0-9]" # minusculas, mayusculas y numeros (no letras con tiles ni caracteres especiales)
print(re.findall(pattern,my_string))

pattern = r"\d" # solo números
print(re.findall(pattern,my_string))

pattern = r"\D" # solo alfabetico y caracteres especiales
print(re.findall(pattern,my_string))

# para mas info mirar en internet expresiones regulares

