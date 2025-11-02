from scr.database import Base, engine
from scr.models import User, Address  # importa tutti i modelli che vuoi creare

# Crea tutte le tabelle
Base.metadata.create_all(bind=engine)

print("Tabelle create con successo!")
