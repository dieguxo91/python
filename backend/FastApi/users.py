from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

# Entidad user
class User():
    name : str
    surname: str
    edad : int

@app.get("/users") 
async def users():
    return [{"name":"diego", "surname":"Garcia", "edad": 31},
            {"name":"jose", "surname":"vazquez", "edad": 30},
            {"name":"daniela", "surname":"Garcia", "edad": 27}]

@app.get("/users/id_user") 
async def users():
    return [{"name":"diego", "surname":"Garcia", "edad": 31},
            {"name":"jose", "surname":"vazquez", "edad": 30},
            {"name":"daniela", "surname":"Garcia", "edad": 27}]
