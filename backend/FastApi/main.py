from fastapi import FastAPI
from routers import products,users,jwt_auth_users, users_db # Routers
from fastapi.staticfiles import StaticFiles

"""
para que funcione tenemos que instalar las librerias:
pip install "fastapi[all]"
pip install "uvicorn[standard]"
"""

"""
ir a la carpeta raiz de la aplicación
Arrancar el servidor comando : uvicorn main:app --reload    main = nombre del fichero
Deter el servidor Ctrl + c
"""

# http://127.0.0.1:8000/docs   ->  Podemos acceder a la documentacion de nuestra API

app = FastAPI() # una variable con el constructor de fastapi

# Router 
app.include_router(products.router) 
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static") # para montar ficheros estatico (imágenes)

@app.get("/") # anotación de FastAPI
async def root():
    return "Hello API!!!" # {"message":"Hello World"}

@app.get("/url") # http://127.0.0.1:8000/url
async def root():
    return  {"url":"https_//mouredev.com/python"}


# para recursos estaticos