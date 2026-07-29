from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums import UserRole


class UserBase(BaseModel):
    full_name: str
    email: str


class UserResponse(UserBase):
    id: UUID
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)