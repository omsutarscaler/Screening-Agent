"""Agent instructions and output contract."""

SCREENING_INSTRUCTIONS = """
1. Compare the candidate's skills and experience with the job requirements.
2. Distinguish required qualifications from preferred qualifications.
3. Cite resume evidence for every key conclusion.
4. Do not invent employers, degrees, dates, skills, or certifications.
5. Flag missing or ambiguous information without penalizing it as a fact.
6. Avoid discriminatory judgments related to age, gender, ethnicity, disability,
   religion, nationality, marital status, or protected characteristics.
"""

SCREENING_OUTPUT_FIELDS = (
    "overall_score",
    "recommendation",
    "matched_requirements",
    "missing_requirements",
    "strengths",
    "concerns",
    "summary",
)
