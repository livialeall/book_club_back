import sqlite3
from data.db import db
from domain.entities import User

class UserData():
    def create_user(self, data:User):
        name = data.name
        email = data.email

        conection = sqlite3.connect(db)
        try:
            cursor = conection.cursor()
            cursor.execute('''
                    INSERT INTO users (name, email)
                    VALUES (?,?)
                ''',(name, email)
            )
            conection.commit()
        except Exception as e:
                raise Exception (e)
        finally:
            conection.close()
        return True