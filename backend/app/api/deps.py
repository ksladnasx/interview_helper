from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.exceptions import AppException
from app.core.jwt import decode_access_token
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repository)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repository: UserRepository = Depends(get_user_repository),
) -> User:
    payload = decode_access_token(token)
    subject = payload.get("sub")

    if subject is None:
        raise AppException(
            message="Invalid token subject",
            code=status.HTTP_401_UNAUTHORIZED,
            error_code="INVALID_TOKEN",
        )

    try:
        user_id = int(subject)
    except ValueError as exc:
        raise AppException(
            message="Invalid token subject",
            code=status.HTTP_401_UNAUTHORIZED,
            error_code="INVALID_TOKEN",
        ) from exc

    user = user_repository.find_by_id(user_id)
    if user is None:
        raise AppException(message="User not found", code=status.HTTP_401_UNAUTHORIZED, error_code="USER_NOT_FOUND")

    return user
