from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from app.config import settings

# Entrada conexion con a BD (maneja pools de conexion)
engine = create_async_engine(settings.db_url, echo=True)

async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        #indicamos al engine que cree todas las tablas si no existen
        await conn.run_sync(SQLModel.metadata.create_all)


# sesion nos permite generar una transaccion en la BD
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, #expire_on_commit=False
    )
    async with async_session() as session:
        yield session
