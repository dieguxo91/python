from fastapi import FastAPI
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

@app.get("/") # anotación de FastAPI
async def root():
    return "Hello World!!!" # {"message":"Hello World"}

@app.get("/url") # http://127.0.0.1:8000/url
async def root():
    return  {"url":"https_//mouredev.com/python"}


