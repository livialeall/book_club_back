from fastapi import HTTPException
from data.user_data import UserData
from domain.entities import User

user_data = UserData()

class UserBusiness:
    def create_user(self,data:User):
        try:
            user_data.create_user(data)
        except HTTPException as e:
            #logar para o desenvolvedor a exceção e
            raise HTTPException(e) #colocar um tipo especifico de exceção
            