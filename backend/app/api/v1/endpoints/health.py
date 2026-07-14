from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.common import ApiResponse

router = APIRouter()


@router.get("", response_model=ApiResponse[dict[str, str]])
def health_check() -> ApiResponse[dict[str, str]]:
    return ApiResponse(data={"status": "ok"})


@router.get("/db", response_model=ApiResponse[dict[str, str]])
def database_health_check(db: Session = Depends(get_db)) -> ApiResponse[dict[str, str]]:
    db.execute(text("SELECT 1"))
    return ApiResponse(data={"status": "ok"})
