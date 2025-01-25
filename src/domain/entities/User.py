from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    name:str | None  
    email:str
    contact:str
    password:str