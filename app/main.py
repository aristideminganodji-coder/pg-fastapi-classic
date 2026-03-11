from fastapi import FastAPI
from app.database import engine,Base
from app.models import user
from app.routers import auth,users,tasks

#creation des tables
Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message":"API connected to PostgreSQL"}