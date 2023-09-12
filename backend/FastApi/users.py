from fastapi import FastAPI
from pydantic import BaseModel # nos permite crear una entidad (parecido a la anotacion del lombok)

app = FastAPI() 

# Entidad user
class User(BaseModel):
    id: int
    name : str
    surname: str
    age : int


# Creando una falsa BBDD
users_list = [User( id = 1,name = "diego", surname = "Garcia", age = 31),
         User(id = 2,name = "jose", surname = "vazquez", age = 30),
         User(id = 3,name = "daniela", surname = "Garcia", age = 27)]

@app.get("/users") # devuelve la BBDD falsa
async def users():
    return users_list

@app.get("/usersjson") # ejemplo, no es lo normal
async def usersjson():
    return [{"name":"diego", "surname":"Garcia", "age": 31},
            {"name":"jose", "surname":"vazquez", "age": 30},
            {"name":"daniela", "surname":"Garcia", "age": 27}]

@app.get("/user/{id}")  
async def user(id: int): # importante ponerle el tipo, sino pondra el path como un String
    return search_user(id)
    
@app.get("/username/{name}") 
async def user(name: str):
    users = list(filter(lambda user: user.name == name, users_list))
    if len(users) > 0:
        return users[0]
    else:
        return {"error":"El nombre no pertenece a ningun usuario"}
    
@app.post("/user/") # Funciona correctamente
async def post_user(user: User):
    if type(search_user(user.id)) != User :
        users_list.append(user)
        return user
    else:
        return {"error":"El usuario ya existe"}
    
@app.put("/user/") # Funciona correctamente
async def put_user(user: User):

    found = False

    for index, saved_user in enumerate(users_list): # Cuando queremos poner el indice tendremos que ponerle el enumerate a la lista
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if found:
        return {"message":"Usuario actualizado"}
    else:
        return {"error":"El usuario no ha podido ser actualizado"}

@app.delete("/user/{id}") # Funciona correctamente
async def put_user(id:int):
    for saved_user in users_list:
        if saved_user.id == id:
            users_list.remove(saved_user)
            return {"message":"Usuario eliminado"}
        else:
            return {"error":"El usuario no ha podido ser eliminado"}

# mejor hacer una función como si fuera este el controlador que llama al servicio

def search_user(id:int): # Funcion del "Service"
    users = list(filter(lambda user: user.id == id, users_list))
    if len(users) > 0:
        return users[0]
    else:
        return {"error":"El id no pertenece a ningun usuario"}
