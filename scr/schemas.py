from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    age: int
    phone: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    model_config = {
        "from_attributes": True  # sostituisce orm_mode=True in Pydantic v2
    }

class AddressBase(BaseModel):
    street: str
    city: str
    lat: float = 0.0   # default → non serve Optional
    lng: float = 0.0
    user_id: int  # collega l'address a un User

class AddressCreate(AddressBase):
    pass

class AddressRead(AddressBase):
    id: int

    model_config = {
        "from_attributes": True  # Pydantic v2, sostituisce orm_mode=True
    }
