from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from scr.database import SessionLocal
from scr.models import Address
from scr.schemas import AddressCreate, AddressRead

router = APIRouter(
    prefix="/addresses",
    tags=["addresses"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET /addresses
@router.get("/", response_model=List[AddressRead])
def get_addresses(db: Session = Depends(get_db)):
    return db.query(Address).all()

# POST /addresses
@router.post("/", response_model=AddressRead)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    db_address = Address(**address.model_dump())  # Pydantic v2
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

# DELETE /addresses/{address_id}
@router.delete("/{address_id}", response_model=dict)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(Address).filter(Address.id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
    db.delete(address)
    db.commit()
    return {"message": f"Address with id {address_id} deleted successfully"}
