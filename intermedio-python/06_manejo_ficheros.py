# File Handling (Manejo de ficheros)

import os

# .txt file

txt_file = open("intermedio-python/my_file.txt", "r+") # r+ = leer y escribir, sino existe lo crea
txt_file.write("\nMi nombre es Diego\nMi apellido es Garcia \n32 años\nMe encanta java y python\nAunque tambien me gusta JavaScript")
# print(txt_file.read()) Lo lee entero
# print(txt_file.read(10)) lee 10 caracteres 
# print(txt_file.readline()) # Lee una linea
# print(txt_file.readline()) # poniendolo otra vez leeria la siguiente linea

for line in txt_file.readlines(): # hariamos un bucle leyendo las lineas
    print(line)

txt_file.close()


#.json file

import json

my_json = open("intermedio-python/my_file.json" , "r+")
json_text = {
    "name":"diego", 
    "surname":"garcia", 
    "age":31, 
    "language":"python"
    }

json.dump(json_text, my_json) # para guardar un json, meteriamos el objeto json y el archivo json 
my_json.close()

with open("intermedio-python/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("intermedio-python/my_file.json")) # para transformalo en diccionario
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("intermedio-python/my_file.csv", "r+") # w+ sobreescribe el archivo

csv_writer = csv.writer(csv_file, delimiter=".") # el atributo delimiter cambia el separador entre las palabras

csv_writer.writerow(["name", "surname","age","language"])
csv_writer.writerow(["Diego", "García","31","python"])
csv_writer.writerow(["Jose", "Vazquez","30","java"])

with open("intermedio-python/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

# import xlrd # debe instalarse el módulo

# .xml file

import xml
