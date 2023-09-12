# manejo de paquetes

#PIP    Python index package   https://pypi.org/

# pip --version     mira la version
# pip --upgrade pip --user      Actualiza pip a la version (abrir vscode como admin)
# pip install <nombre-package>
# pip uninstall <nombre-package>
# pip show <nombre-package>
"""
# pip list      nos da una lista de los packages instalados
Package         Version
--------------- ------------
numpy           1.25.2
pandas          2.1.0
pip             23.2.1
python-dateutil 2.8.2
pytz            2023.3.post1
setuptools      58.1.0
six             1.16.0
tzdata          2023.3
"""

import numpy # pip install numpy 

print(numpy.version.version)

numpy_array = numpy.array([2,4,6,8,9])

print(type(numpy_array))

print(numpy_array * 2) # se multiplicaria en todos los elementos del array


import pandas # pip install pandas

# libreria para hacer peticiones al back

import requests # pip install requests 

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response.status_code) # para ver el codigo , correcto el 200 recuerda
print(response.json()) # nos devuelve el json de la petición que le hicimos al back

# Arithmetics package

import my_package # importamos el package 
from my_package import arithmetics # importamos el modulo del package

print(arithmetics.sum_two_values(2))

