from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.index import router
from routes import user_routes

app = FastAPI(title= "Book Club")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:5174"],  # Origem permitida
    allow_credentials=True,  # Permite envio de cookies/autenticação
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)
app.include_router(router)
app.include_router(user_routes.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8800,reload=True)