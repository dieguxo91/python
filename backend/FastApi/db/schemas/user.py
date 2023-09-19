
def user_schema(user) -> dict: # podria ser un User en vez de un dict
    return {"id": str(user["_id"]), # lo casteamos a string para que no haya errores
            "name":user["name"],
            "surname":user["surname"],
            "age": user["age"]}

def users_schema(users)-> list:
    return [user_schema(user) for user in users]