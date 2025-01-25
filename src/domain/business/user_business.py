from fastapi import HTTPException
from data.user_data import UserData
from domain.entities import User
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

user_data = UserData()
ph = PasswordHasher()

class UserBusiness:
    def create_user(self,data:User):
        try:
            data.password = ph.hash(data.password)
            user_data.create_user(data)
        except HTTPException as e:
            #logar para o desenvolvedor a exceção e
            raise HTTPException(e) #colocar um tipo especifico de exceçãod
        
    def login (self,auth:User):
        user_email = auth.email
        user_password = auth.password
        try:
            result = user_data.verify_email(user_email)
            if(result[0]== None):
                return False #Nenhum usuario com esse email
            stored_password = result[1]
            if(ph.verify(stored_password,user_password)):
                return True
        except VerifyMismatchError:
            raise Exception(f"A senha não está correta")
        except Exception as e:
            raise Exception(f"Erro ao fazer login: {e}") #erro amigavel para o usuario e log para o desenvolvedor
        

            