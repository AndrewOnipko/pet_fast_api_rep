from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.tasks import Task
from app.schemas.tasks import TaskCreate, TaskUpdate
from app.logger import simple_logger, get_logger
from fastapi import Depends
import logging

class TaskRepository:
    def __init__(self, session: AsyncSession, logger: logging.Logger):
        self.session = session
        self.logger = logger


    @simple_logger
    async def get_all(self) -> list[Task]:
        result = await self.session.execute(select(Task))
        return result.scalars().all()


    @simple_logger
    async def get_by_id(self, task_id: int) -> Task | None:
        result = await self.session.execute(
            select(Task).where(Task.id == task_id)
        )
        return result.scalar_one_or_none()


    @simple_logger
    async def create(self, data: TaskCreate) -> Task:
        task = Task(**data.model_dump())
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task


    @simple_logger
    async def update(self, task_id: int, data: TaskUpdate) -> Task | None:
        task = await self.get_by_id(task_id)
        if not task:
            return None
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(task, key, value)
        await self.session.commit()
        await self.session.refresh(task)
        return task


    @simple_logger
    async def delete(self, task_id: int) -> bool:
        task = await self.get_by_id(task_id)
        if not task:
            return False
        await self.session.delete(task)
        await self.session.commit()
        return True