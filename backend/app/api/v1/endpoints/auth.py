from fastapi import APIRouter, Depends, status

from app.api.deps import get_auth_service, get_current_user
from app.models.user import User
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest
from app.schemas.common import ApiResponse
from app.schemas.user import UserResponse
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/register", response_model=ApiResponse[UserResponse], status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, auth_service: AuthService = Depends(get_auth_service)) -> ApiResponse[UserResponse]:
    user = auth_service.register(payload)
    return ApiResponse(message="Register success", data=user)


@router.post("/login", response_model=ApiResponse[LoginResponse])
def login(payload: LoginRequest, auth_service: AuthService = Depends(get_auth_service)) -> ApiResponse[LoginResponse]:
    result = auth_service.login(payload.username, payload.password)
    return ApiResponse(message="Login success", data=result)


@router.get("/me", response_model=ApiResponse[UserResponse])
def get_me(current_user: User = Depends(get_current_user)) -> ApiResponse[UserResponse]:
    return ApiResponse(data=current_user)
