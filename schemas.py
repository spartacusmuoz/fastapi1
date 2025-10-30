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
