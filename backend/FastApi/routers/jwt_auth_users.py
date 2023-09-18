from fastapi import APIRouter,Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext # para el contexto de encriptación
from datetime import datetime, timedelta # para los tiempos de acceso

"""
librerias para el JWT:
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]" # algoritmo del token
"""

ALGORITHM = "HS256" # Tipo de hasheo de la password
ACCESS_TOKEN_DURATION = 1

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

# Esto se haria importando la clase en este modulo, pero para la guia lo hacemos asi

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
    "password" : "$2y$10$wlJyQdwBX5ojT9gplRFMVe2/LwRYobbbr8dPs5EGkK5hZxeWTFSpu"
    },
    "dieguxo92":{
    "username" : "dieguxo92",
    "name": "diego",
    "email" : "diegogarcia2@gmail.com",
    "disabled": True,
    "password" : "$2y$10$llk.XXb9V53xtmUv16szVOSE5yYc14aHgcbVJwnHzdZcnfMeSO.9e"
    }
}

def search_user(username: str): 
    if username in users_db:
        return User(**users_db[username])
    
def create_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username]) 

async def auth_user(token : str = Depends(oauth2)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticación invalidas",
                            headers={"WWW-Authenticate":"Bearer"})

    try:
        username = jwt.decode(token,ALGORITHM).get("sub")
        if username is None:
            raise exception

    except JWTError:  # importar para el error del JSON Web token
        raise exception
    
    return search_user(username)


async def current_user(user : User = Depends(auth_user)): # un criterio de dependecia
 
    if user.disabled: # seria para controlar los permisos
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
        
    user_db = users_db.get(form.username)
    print( user_db)
    if not user_db:
        raise HTTPException(status_code=400,
                             detail="El usuario no es correcto")
    
    user = create_user_db(form.username)

    if not crypt.verify(form.password, user.password): 
        raise HTTPException(status_code=400,
                             detail="La contraseña no es correcta")

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_DURATION) # momento actual mas el tiempo que durara el token
   
    """
    Campos del jwt:
    sub para el nombre de usuario
    exp para la fecha de expiracion 
    """
    access_token = {"sub": user.username, "exp": expire} 

    return{"access_token": jwt.encode(access_token,ALGORITHM), "token_type": "bearer"} # deberia crearse un token para ello

@router.get("/usuario/me")
async def me(user: User = Depends(current_user)):
    return user