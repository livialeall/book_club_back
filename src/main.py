from fastapi import FastAPI
from routes.index import router
from routes import user_routes

app = FastAPI(title= "Book Club")

app.include_router(router)
app.include_router(user_routes.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8800,reload=True)