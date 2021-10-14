from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Entrada conexion con a BD (maneja pools de conexion)
engine = create_async_engine(settings.db_url, echo=True)

# sesion nos permite generar una transaccion en la BD
async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine,
        class_=AsyncSession,  # expire_on_commit=False
    )
    async with async_session() as session:
        yield session
