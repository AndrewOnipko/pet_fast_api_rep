from fastapi import APIRouter, Depends, HTTPException, status
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.docs import users_docs as doc

router = APIRouter()

@router.get("/", response_model=list[UserRead], **doc.get_users)
async def get_users(service: UserService = Depends()):
    return await service.get_users()


@router.post("/", response_model=UserRead, **doc.create_user)
async def create_user(user: UserCreate, service: UserService = Depends()):
    return await service.create_user(user)


@router.get("/{user_id}", response_model=UserRead, **doc.get_user)
async def get_user(user_id: int, service: UserService = Depends()):
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@router.put("/{user_id}", response_model=UserRead, **doc.update_user)
async def update_user(user_id: int, data: UserUpdate, service: UserService = Depends()):
    user = await service.update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@router.delete("/{user_id}", **doc.delete_user)
async def delete_user(user_id: int, service: UserService = Depends()):
    deleted = await service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Пользователь не найден")