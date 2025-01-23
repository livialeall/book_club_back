from domain.business.user_business import UserBusiness
from domain.entities.User import User
from fastapi import HTTPException
from routes.index import router

business = UserBusiness();

@router.post("/create_user")
def create_user(user_data:User):
    try:
        business.create_user(user_data)
        return {"status":200,"message": "Cadastro efetuado com sucesso"}
    except HTTPException as e:
        raise HTTPException(e)