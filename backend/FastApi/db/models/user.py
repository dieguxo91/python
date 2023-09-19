# Entidad user
from pydantic import BaseModel


class User(BaseModel):
    id: str | None # para que no sea pbligatorio, ya que el id se crea solo
    name : str
    surname: str
    age : str