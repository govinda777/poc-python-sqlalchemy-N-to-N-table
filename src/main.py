from fastapi import FastAPI

from user import user_router
from sqlalchemy.orm import Session

# Isto cria as tabelas no banco de dados, se ainda não existirem.
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(group_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
