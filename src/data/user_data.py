import sqlite3
from data.db import db
from domain.entities import User

class UserData():
    def create_user(self, data:User):
        conection = sqlite3.connect(db)
        try:
            cursor = conection.cursor()
            cursor.execute('''
                    INSERT INTO usuarios (nome, email)
                    VALUES ('Livia', 'livia@')
                '''
            )
            conection.commit()
        except:
            print("ERRO")
            return False
        finally:
            conection.close()
        return True