# Class

# El tipado de los atributos es debil, se puede setear cualquier valor

class MyPerson: #CamelCase en vez de SnakeCase
    def __init__(self, name, surname, alias = "sin alias"): # constructor de la clase
        self.__name = name # Privatizar los atributos __atributo
        self.surname = surname
        self.alias = alias # sino se le asigna un valor sera el que hayamos puesto por defecto

    def walk(self): # para meter los atibutos del objeto, "metiendo a la misma clase"
        print(self.get_name() , "esta andando")

    def get_name(self):
        return self.__name


my_person = MyPerson("diego", "garcia")
print(my_person.get_name())
print(my_person.surname)
print(my_person.alias)

my_person.walk()