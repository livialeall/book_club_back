from data.user_data import UserData
from domain.entities import User

user_data = UserData()

class UserBusiness:
    def create_user(self,data:User):
        try:
            """ if(user_data.existing_user(data.email)):
                raise Exception("Usuário já está cadastro com esse email") #colocar um tipo especifico de exceção """
            user_data.create_user(data)
        except Exception as e:
            #logar para o desenvolvedor a exceção e
            raise Exception(e) #colocar um tipo especifico de exceção
            