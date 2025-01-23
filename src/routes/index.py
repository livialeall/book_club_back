from domain.business.user_business import UserBusiness
from domain.entities.User import User
from fastapi import APIRouter, HTTPException

router = APIRouter();
business = UserBusiness();

@router.get("/")
def hello():
    return {"message": "Hello, World!"}
