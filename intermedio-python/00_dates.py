# Dates (Fechas)

# importamos el objeto datetime del modulo datetime
from datetime import datetime

def print_datetime(date: datetime):
    print(f"año: {date.year}, mes: {date.month}, dia:{ date.day}")
    print(f"horas: {date.hour}, minutos: {date.minute}, segundos:{ date.second}")

def print_date(date: datetime):
    print(f"año: {date.year}, mes: {date.month}, dia:{ date.day}")

    
def print_time(date: datetime):
    print(f"horas: {date.hour}, minutos: {date.minute}, segundos:{ date.second}")


now = datetime.now() # accedemos al dia/ hora que se inicializa la variable

print(now.month)
print(now.day)
print(now.year)
print(now.second)

# representación unica de un tiempo

timestapmp = now.timestamp()

print(timestapmp) 

# prueba con constructor y funcion de impresión 

year_2023 = datetime(2023,9,3)
print_datetime(year_2023)

# time solo cuando queramos coger una hora

from datetime import time

current_time = time(17,19,45)
print_time(current_time)

# date solo cuando queramos coger una fecha

from datetime import date

current_date = date(2023,9,4)
print_date(current_date)

# Podemos hacer operaciones siempre que sean del mismo tipo

print(now - year_2023)


# para trabajar con franjas de fechas

from datetime import timedelta

start_time_delta = timedelta(200, 100, 100, weeks= 10)
end_time_delta = timedelta(300, 100, 100, weeks= 14)

print(end_time_delta - start_time_delta)
