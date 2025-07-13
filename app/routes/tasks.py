from fastapi import APIRouter, Depends, HTTPException, status
from app.services.task_service import TaskService
from app.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from app.docs import tasks_docs as doc

router = APIRouter()

@router.get("/", response_model=list[TaskRead], **doc.get_tasks)
async def get_tasks(service: TaskService = Depends()):
    return await service.get_tasks()


@router.get("/{task_id}", response_model=TaskRead, **doc.get_task)
async def get_task(task_id: int, service: TaskService = Depends()):
    task = await service.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@router.post("/", response_model=TaskRead, **doc.create_task)
async def create_task(task: TaskCreate, service: TaskService = Depends()):
    return await service.create_task(task)


@router.put("/{task_id}", response_model=TaskRead, **doc.update_task)
async def update_task(task_id: int, task_data: TaskUpdate, service: TaskService = Depends()):
    task = await service.update_task(task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@router.delete("/{task_id}", **doc.delete_task)
async def delete_task(task_id: int, service: TaskService = Depends()):
    deleted = await service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Задача не найдена")