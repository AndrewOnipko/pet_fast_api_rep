from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db import get_async_session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.utils.logger import simple_logger, get_logger
import logging

class UserService:
    def __init__(self, session: AsyncSession = Depends(get_async_session), logger: logging.Logger = Depends(get_logger)):
        self.logger = logger
        self.repository = UserRepository(session, logger)


    @simple_logger
    async def get_users(self) -> list[UserRead]:
        users = await self.repository.get_all()
        return [UserRead.model_validate(user) for user in users]


    @simple_logger
    async def create_user(self, user_data: UserCreate) -> UserRead:
        user = await self.repository.create(user_data)
        return UserRead.model_validate(user)
    

    @simple_logger
    async def get_user(self, user_id: int) -> UserRead | None:
        user = await self.repository.get_by_id(user_id)
        if user:
            return UserRead.model_validate(user)
        return None
    

    @simple_logger
    async def update_user(self, user_id: int, data: UserUpdate) -> UserRead | None:
        user = await self.repository.update(user_id, data)
        if user:
            return UserRead.model_validate(user)
        return None
    

    @simple_logger
    async def delete_user(self, user_id: int) -> bool:
        return await self.repository.delete(user_id)