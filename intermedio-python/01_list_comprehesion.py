# lista comprehesion (comprimida)

def sum_five(number):
    return number + 5

my_original_list = [22, 34, 56, 71, 10, 8, 9]

my_range = [i for i in range(7)] #  crear una lista con un rango

print(my_range)

my_list = [i * 2 for i in range(5)] # creariamos un rango de 5 numeros que se multiplican por 2
print(my_list)

my_other_list = [sum_five(i) for i in range(8)] # haria la función solo la primera vez

print(my_other_list)

