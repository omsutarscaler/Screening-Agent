from pydantic import BaseModel, Field


class ScreeningRequest(BaseModel):
    job_description: str = Field(min_length=10)
    resume_text: str = Field(min_length=10)


class ScreeningResult(BaseModel):
    overall_score: int = Field(ge=0, le=100)
    recommendation: str
    matched_requirements: list[str] = Field(default_factory=list)
    missing_requirements: list[str] = Field(default_factory=list)
    strengths: list[str] = Field(default_factory=list)
    concerns: list[str] = Field(default_factory=list)
    summary: str
