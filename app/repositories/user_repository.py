from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate  
from app.logger import simple_logger, get_logger
from fastapi import Depends
import logging

class UserRepository:
    def __init__(self, session: AsyncSession, logger: logging.Logger):
        self.session = session
        self.logger = logger

    @simple_logger
    async def get_all(self) -> list[User]:
        stmt = select(User)
        result = await self.session.execute(stmt)
        return result.scalars().all()


    @simple_logger
    async def create(self, user_data: UserCreate) -> User:
        new_user = User(
            username=user_data.username,
            email=user_data.email
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
    

    @simple_logger
    async def get_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()


    @simple_logger
    async def update(self, user_id: int, data: UserUpdate) -> User | None:
        user = await self.get_by_id(user_id)
        if not user:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(user, key, value)
        await self.session.commit()
        await self.session.refresh(user)
        return user


    @simple_logger
    async def delete(self, user_id: int) -> bool:
        user = await self.get_by_id(user_id)
        if not user:
            return False
        await self.session.delete(user)
        await self.session.commit()
        return True