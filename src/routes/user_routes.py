from domain.business.user_business import UserBusiness
from domain.entities.User import User
from fastapi import HTTPException
from routes.index import router

business = UserBusiness();

@router.post("/create_user")
def create_user(user_data:User):
    try:
        result = business.create_user(user_data)
        if(result):
            return {"message": "Cadastro efetuado com sucesso!"}
        else:
            raise HTTPException(status_code=400,detail="Não foi possível efetuar seu cadastro")
    except Exception as e:
        raise HTTPException(e)