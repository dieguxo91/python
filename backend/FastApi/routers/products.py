from fastapi import APIRouter

router = APIRouter(prefix="/products",# con prefix añadimos la raiz de las rutas del crud 
                   tags=["products"], # separa las rutas en el docs 
                   responses={404:{"message": "No encontrado"},500:{"message": "Fuera de indice"}}) # con responses, podemos controlar los httpStatus

products_list = ["peine","raqueta","ordenador","raton","paraguas"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def product(id : int):
    return products_list[id]
