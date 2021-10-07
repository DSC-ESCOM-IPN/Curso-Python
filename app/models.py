from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    password: str
    age: int


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)


class UserCreate(SQLModel):
    pass