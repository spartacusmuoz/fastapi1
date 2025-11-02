from .database import SessionLocal
from .models import User, Address

# Crea una sessione
db = SessionLocal()

# Recupera tutti gli utenti
users = db.query(User).all()

print("UTENTI:")
# Stampa i dati
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}, Phone: {user.phone}")
# Recupera tutti gli indirizzi
addresses = db.query(Address).all()

print("\nINDIRIZZI:")
for addr in addresses:
    print(f"ID: {addr.id}, User_ID: {addr.user_id}, City: {addr.city}, Street: {addr.street}")

# Chiudi la sessione
db.close()
