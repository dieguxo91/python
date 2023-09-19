from fastapi import APIRouter, HTTPException,status
from db.models.user import User
from db.client import db_client_ip
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

# Users DB API con host

router = APIRouter(prefix="/userdbip",
                   tags=["userdbip"],
                   responses={status.HTTP_404_NOT_FOUND:{"message":"No encontrado"}}) 


@router.get("/", response_model=list[User])  # para que nos devuelva una lista
async def users():
    return users_schema(db_client_ip.local.users.find()) # creamos esta funcion en el schema para obtener una lista


@router.get("/{id}")  
async def user(id: str): 
    return search_user("_id",ObjectId(id)) # para transformar el id en Object id
    
@router.get("/name/{name}")  # solo es una prueba por otro campo
async def user(name: str):
    try:
        user = search_user("name",name)
        return user
    except:
        return{"error":"No se ha encontrado el usuario"}
    
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def post_user(user: User):
    if type(search_user("name",user.name)) == User :
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    else:
        user_dict = dict(user)
        
        del user_dict["id"] # para que se autogenere el id solo, borramos el id del json

        # al ponerle el inserted_id nos devolveria el id creado para ese usuario
        id = db_client_ip.local.users.insert_one(user_dict).inserted_id # como no conoce los ficheros tiene que ponerse manual (local e users)
        
        new_user = user_schema(db_client_ip.local.users.find_one({"_id":id})) # Mongodb nos crea el campo _id no id, tener en cuenta

        return User(**new_user)


@router.put("/", response_model=User) # Funciona correctamente
async def put_user(user: User):

    try:
        user_dict = dict(user) # primero pasarlo a un diccionario
        del user_dict["id"] # nos cargamos el campo id, ya que no puede actualizarse
        db_client_ip.local.users.find_one_and_replace({"_id":ObjectId(user.id)}, user_dict) # buscar por id y reemplazar
    except:    
        return {"error":"El usuario no ha podido ser actualizado"}
    
    return search_user("_id", ObjectId(user.id))
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT) # Funciona correctamente
async def put_user(id:str):
   found = db_client_ip.local.users.find_one_and_delete({"_id":ObjectId(id)})
   if not found :
       return {"error":"No se ha eliminado el usuario"}

# mejor hacer una función como si fuera este el controlador que llama al servicio, funcion generica

def search_user(field: str, key): # se deberia hacer con el email o el username, que no se pueda repetir vaya
    try:
        user = user_schema(db_client_ip.local.users.find_one({field:key}))
        return User(**user)
    except:
        return{"error":"No se ha encontrado el usuario"}
    
