from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    #name:str | None  
    email:str
    password:str