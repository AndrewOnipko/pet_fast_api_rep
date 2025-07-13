from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import users, tasks
from app.db import engine, Base 

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield 
    await engine.dispose()
    
app = FastAPI(
    title="Task Manager API",
    description="REST API pet project",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])