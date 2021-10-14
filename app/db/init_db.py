from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

# Entrada conexion con a BD (maneja pools de conexion)
engine = create_async_engine(settings.db_url, echo=True)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        # indicamos al engine que cree todas las tablas si no existen
        # await conn.run_sync(SQLModel.metadata.create_all)
