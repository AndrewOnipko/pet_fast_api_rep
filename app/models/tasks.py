from sqlalchemy import ForeignKey, String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="tasks")