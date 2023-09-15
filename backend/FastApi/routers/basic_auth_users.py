from fastapi import FastAPI,Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer # la clase que se va a encargar de authentication
# requesform es la forma en la que se va a enviar los criterios de authentication

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login") # url que se va a encargar de la authentication

class User(BaseModel):
    username : str
    name: str
    email : str
    disabled: bool

class UserDB(User): # Usuario de BBDD --Herencia--
    password:str

users_db = {
    "dieguxo91":{
    "username" : "dieguxo91",
    "name": "diego",
    "email" : "diegogarcia1@gmail.com",
    "disabled": False,
    "password" : "123456"
    },
    "dieguxo92":{
    "username" : "dieguxo92",
    "name": "diego",
    "email" : "diegogarcia2@gmail.com",
    "disabled": True,
    "password" : "654321"
    }
}

def create_user_db(username: str): # función para encontrar el username que es "nuestro token (Provisional)"
    if username in users_db:
        return UserDB(**users_db[username]) # Pueden ir varios 
    
def search_user(username: str): # funcion para securizar la contraseña, creariamos un usuario normal, la password se guarda en BBDD
    if username in users_db:
        return User(**users_db[username])
    
    
async def current_user(token: str = Depends(oauth2)): # un criterio de dependecia
    user = search_user(token)
    if not user: # si no hay token no habria usuario, por lo cual  nos daria no autorizado
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="Credenciales de autenticación invalidas", headers={"WWW-Authenticate":"Bearer"})
    
    if user.disabled: # seria para controlar los permisos
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    return user
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
        
    user_db = users_db.get(form.username)
    print( user_db)
    if not user_db:
        raise HTTPException(status_code=400,
                             detail="El usuario no es correcto")
    
    user = create_user_db(form.username)

    if not user.password == form.password: # deberiamos de compararlas encriptadas
        raise HTTPException(status_code=400,
                             detail="La contraseña no es correcta")

    return{"access_token": user.username, "token_type": "bearer"} # deberia crearse un token para ello

@app.get("/usuario/me")
async def me(user: User = Depends(current_user)):
    return user

