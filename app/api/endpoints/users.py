from os import stat
from app.db.session import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()


@router.get("/", response_model=list([User]), status_code=status.HTTP_200_OK)
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(name=user.name, password=user.password, age=user.age, email=user.email, address=user.address)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return {"msg": "user created"}


@router.put("/{user_id}")
async def update_user(user_id: int, user: UserUpdate, session: AsyncSession = Depends(get_session)):
    query = await session.execute(select(User).where(User.id==user_id))
    result = query.scalar()
    result.email = user.email
    result.password = user.password
    await session.commit()
    await session.refresh(result)
    return result


@router.delete("/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    query = await session.execute(select(User).where(User.id==user_id))
    user = query.scalar()
    await session.delete(user)
    await session.commit()
    return {"msg": "user deleted"}
