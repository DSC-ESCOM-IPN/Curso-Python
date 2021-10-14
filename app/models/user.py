from app.schemas.user import UserBase
from sqlmodel import Field


# Modelo BD
class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    # referencias a otras tablas foreingkey
