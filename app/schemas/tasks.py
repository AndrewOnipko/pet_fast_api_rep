from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False

class TaskCreate(TaskBase):
    user_id: int

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None

class TaskRead(TaskBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }