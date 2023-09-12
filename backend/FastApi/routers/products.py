from fastapi import APIRouter

router = APIRouter() 

@router.get("/products")
async def products():
    return["peine","raqueta","ordenador","raton","paraguas"]

