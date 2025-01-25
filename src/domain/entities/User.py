from typing import Optional
from pydantic import BaseModel


class NewUser(BaseModel):
    name:str | None  
    email:str
    contact:str
    password:str

class User(BaseModel):
    email:str
    password:str
