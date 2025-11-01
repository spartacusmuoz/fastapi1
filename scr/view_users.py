from .database import SessionLocal
from .models import User

# Crea una sessione
db = SessionLocal()

# Recupera tutti gli utenti
users = db.query(User).all()

# Stampa i dati
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}, Phone: {user.phone}")

# Chiudi la sessione
db.close()
