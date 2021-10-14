from pydantic.networks import EmailStr
from sqlmodel import SQLModel
from pydantic import EmailStr, BaseModel


# Intermedio entre un modelo de Pydantic y un Modelo de la BD
class UserBase(SQLModel):
    name: str
    email: str
    password: str
    address: str
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
