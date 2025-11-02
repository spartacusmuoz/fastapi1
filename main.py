from fastapi import FastAPI
from scr.database import Base, engine
from routers import users, address, city   # importa entrambi

# Creazione tabelle se non esistono
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API FastAPI con Users e Address")

# Includi tutti i router
app.include_router(users.router)
app.include_router(address.router)
app.include_router(city.router)

# Root dell'API
@app.get("/")
def root():
    return {"message": "API pronta"}
