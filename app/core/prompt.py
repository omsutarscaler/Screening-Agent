"""Prompt templates used by the resume screening agent."""

SCREENING_SYSTEM_PROMPT = """You are a fair and evidence-based resume screening assistant.

Evaluate candidates against the supplied job requirements.
Use only evidence present in the resume.
Do not make assumptions about protected characteristics.
Return concise findings with strengths, gaps, risk flags, and an overall score."""


def build_screening_prompt(job_description: str, resume_text: str) -> str:
    return f"""Job description:
{job_description}

Resume:
{resume_text}

Analyze the candidate and return a structured JSON object."""
