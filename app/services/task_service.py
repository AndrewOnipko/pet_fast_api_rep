from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_async_session
from app.repositories.task_repository import TaskRepository
from app.schemas.tasks import TaskCreate, TaskUpdate, TaskRead
from app.logger import simple_logger, get_logger
import logging

class TaskService:
    def __init__(self, session: AsyncSession = Depends(get_async_session), logger: logging.Logger = Depends(get_logger)):
        self.logger = logger
        self.repository = TaskRepository(session, logger)


    @simple_logger
    async def get_tasks(self) -> list[TaskRead]:
        tasks = await self.repository.get_all()
        return [TaskRead.model_validate(task) for task in tasks]


    @simple_logger
    async def get_task(self, task_id: int) -> TaskRead | None:
        task = await self.repository.get_by_id(task_id)
        return TaskRead.model_validate(task) if task else None


    @simple_logger
    async def create_task(self, data: TaskCreate) -> TaskRead:
        task = await self.repository.create(data)
        return TaskRead.model_validate(task)


    @simple_logger
    async def update_task(self, task_id: int, data: TaskUpdate) -> TaskRead | None:
        task = await self.repository.update(task_id, data)
        return TaskRead.model_validate(task) if task else None


    @simple_logger
    async def delete_task(self, task_id: int) -> bool:
        return await self.repository.delete(task_id)