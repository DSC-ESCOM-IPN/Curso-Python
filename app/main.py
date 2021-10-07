from fastapi import FastAPI, Depends

from app.db import get_session, init_db
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select
from app.models import User, UserCreate


from app.config import settings

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    print(settings.db_url)
    await init_db()


@app.get("/")
async def root():
    return {"msg": "hello worlds"}


@app.get("/users", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return [User(name=user.name, password=user.password, age=user.age) for user in users]


@app.post("/users")
async def add_user(user=UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(name="Jose", password="password", age=12)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
