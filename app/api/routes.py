from fastapi import APIRouter

from app.models.schemas import ScreeningRequest, ScreeningResult
from app.services.screening_service import screening_service

router = APIRouter()


@router.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/screenings", response_model=ScreeningResult, tags=["screening"])
def create_screening(request: ScreeningRequest) -> ScreeningResult:
    return screening_service.screen(request)
