from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./db.sqlite3"

engine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session_factory = sessionmaker(bind=engine,
                                    expire_on_commit=False,
                                    class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_async_session():
    async with async_session_factory() as session:
        yield session
