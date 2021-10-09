from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db import get_session, init_db
from app.models import User, UserBase

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/")
async def root():
    return {"msg": "hello world"}


@app.get("/users", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@app.post("/users")
async def add_user(user: UserBase, session: AsyncSession = Depends(get_session)):
    user = User(name=user.name, password=user.password, age=user.age)
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return {"msg": "user added"}
