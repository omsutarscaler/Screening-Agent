from app.core.prompt import SCREENING_SYSTEM_PROMPT, build_screening_prompt
from app.core.instructions import SCREENING_INSTRUCTIONS, SCREENING_OUTPUT_FIELDS
from app.models.schemas import ScreeningRequest, ScreeningResult


class ScreeningService:
    """Boilerplate service boundary for future model integration."""

    def screen(self, request: ScreeningRequest) -> ScreeningResult:
        # Replace this placeholder with an LLM or rules engine implementation.
        _ = SCREENING_SYSTEM_PROMPT
        _ = SCREENING_INSTRUCTIONS
        _ = build_screening_prompt(
            request.job_description,
            request.resume_text,
        )
        _ = SCREENING_OUTPUT_FIELDS

        return ScreeningResult(
            overall_score=0,
            recommendation="pending_review",
            matched_requirements=[],
            missing_requirements=[],
            strengths=[],
            concerns=["Automated screening model is not configured"],
            summary="Boilerplate result. Connect an AI provider to perform screening.",
        )


screening_service = ScreeningService()
