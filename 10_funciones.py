# Funciones

# función sin parametros
def my_function (): 
    print("Hola, soy una función")

my_function()
my_function()

# función con parametros
def sum_two_values (first_number, second_number): 
    sum = first_number + second_number
    return sum

result = sum_two_values(2,3)
print(result)

# se puede asociar los valores a los parametros desordenados
def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="garcia", name="diego") 


def print_name_whit_default (name, surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")

print_name_whit_default("diego", "garcia","dieguxo" ) 
print_name_whit_default("diego", "garcia" )

# Si añadimos el asterico podremos insertar una tupla
def print_upper_text(*texts): 
    for text in texts:
        print(str(text).upper())

print_upper_text("hola")
print_upper_text("hola", "diego")
    