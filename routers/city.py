from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from scr.database import SessionLocal
from scr.models import User, Address
from typing import List

router = APIRouter(prefix="/users_by_city", tags=["users_by_city"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{city}", response_model=List[str])
def users_in_city(city: str, db: Session = Depends(get_db)):
    # Query join tra User e Address
    users = db.query(User).join(Address).filter(Address.city == city).all()
    return [user.name for user in users]

# 🔹 2️⃣ Numero di utenti che abitano in una città
@router.get("/{city}/count", response_model=dict)
def count_users_in_city(city: str, db: Session = Depends(get_db)):
    count = db.query(User).join(Address).filter(Address.city == city).count()
    return {"city": city, "numero_di_utenti": count}