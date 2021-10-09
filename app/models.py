from typing import Optional
from sqlmodel import Field, SQLModel


#Intermedio entre un modelo de Pydantic y un Modelo de la BD
class UserBase(SQLModel):
    name: str
    password: str
    age: int


#Modelo BD
class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    # referencias a otras tablas foreingkey


class StudentBase(SQLModel):
    name: Optional[str]
    school: str


#Modelo BD
class Student(StudentBase, table=True):
    id: int = Field(default=None, primary_key=True)
    # referencias a otras tablas foreingkey
