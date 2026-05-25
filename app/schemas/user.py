from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator


class UserBase(BaseModel):
    name: str
    email: EmailStr
    department: Optional[str] = None
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str
    is_admin: bool = False

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres.")
        return v


class UserUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None


class UserPasswordUpdate(BaseModel):
    current_password: str
    new_password: str

    @field_validator("new_password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres.")
        return v


class UserResponse(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str
