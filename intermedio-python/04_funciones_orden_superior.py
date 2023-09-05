### Higher Order Functions (funciones de orden superior)

def sum_one(value):
    return value + 1

def sum_two_values_and_one(first_value, second_value):
    return sum_one(first_value + second_value)  # una función que llama a otra función

print(sum_two_values_and_one(2,4))

def sum_two_values_whit_function(first_value, second_value, fsum):  # Podemos pasarle una función
    return fsum(first_value + second_value)  

print(sum_two_values_whit_function(2,4,sum_one))

def sum_five(value):
    return value + 5

print(sum_two_values_whit_function(2,4,sum_five))

### Closures

# Se usa sobretodo para los asincronos

def sum_ten():
    def add(value):
        return value +10
    return add
    
add_closure = sum_ten() # hacemos una llamada a la función y retornaria la función encapsulada

print(add_closure(10))

def sum_value(original_value):
    def add(value):
        return value + original_value
    return add
    
add_closure = sum_value(5) # hacemos una llamada a la función con un parametro y retornaria la función encapsulada

print(add_closure(10))

print(sum_value(4)(22)) # podemos hacer la llamada directamente pasandole los parametros seguidos

### Built-in Higher Order Functions

numbers = [2, 5, 10, 21]

def multiply_two(value):
    return value * 2

lambda_multyply_five = lambda value : value * 5

def filter_pares(value): 
    if value % 2 == 0 :
        return True
    return False

#map
mapa = list(map(multiply_two, numbers)) # itera los valores y ejecuta la función que se le pasa

print(mapa)

mapa_two = list(map(lambda_multyply_five, numbers)) # tambien se le puede pasar lambdas

print(mapa_two)

#filter

numbers_pares = list(filter(filter_pares, numbers)) # metemos una función de filtro creada anteriormente

print(numbers_pares)

numbers_impares = list(filter(lambda value : value % 2 != 0, numbers)) # podemos pasarle lambdas

print(numbers_impares)

# reduce

# reduce()
