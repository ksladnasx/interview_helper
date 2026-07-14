from fastapi import status

from app.core.exceptions import AppException
from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginResponse, RegisterRequest
from app.schemas.user import UserResponse


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register(self, payload: RegisterRequest) -> User:
        existing_user = self.user_repository.find_by_username(payload.username)
        if existing_user is not None:
            raise AppException(
                message="Username already exists",
                code=status.HTTP_409_CONFLICT,
                error_code="USERNAME_EXISTS",
            )

        return self.user_repository.create(
            username=payload.username,
            password=hash_password(payload.password),
            avatar=payload.avatar,
        )

    def login(self, username: str, password: str) -> LoginResponse:
        user = self.user_repository.find_by_username(username)
        if user is None or not verify_password(password, user.password):
            raise AppException(
                message="Invalid username or password",
                code=status.HTTP_401_UNAUTHORIZED,
                error_code="INVALID_CREDENTIALS",
            )

        token = create_access_token(subject=str(user.id))
        return LoginResponse(access_token=token, user=UserResponse.model_validate(user))
