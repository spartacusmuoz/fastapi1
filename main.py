from fastapi import FastAPI
from database import Base, engine
from routers import users

# Creazione tabelle se non esistono
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Includiamo il router
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Benvenuto alla API FastAPI con MySQL/SQLite!"}
