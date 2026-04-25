from pydantic import BaseModel, Field
from typing import List


class AnalyzeRequest(BaseModel):
    resume_text: str = Field(..., description="The full text content of the candidate's resume.")
    job_description: str = Field(..., description="The full job description text.")


class SkillGap(BaseModel):
    skill: str
    importance: str  # "High", "Medium", "Low"
    suggestion: str


class AnalyzeResponse(BaseModel):
    match_score: int = Field(..., description="Overall match percentage (0–100).")
    summary: str = Field(..., description="2–3 sentence overall assessment.")
    matched_skills: List[str] = Field(..., description="Skills the candidate already has that match the JD.")
    missing_skills: List[SkillGap] = Field(..., description="Skills that are missing with suggestions.")
    resume_improvements: List[str] = Field(..., description="Concrete resume bullet improvements.")
    interview_prep_tips: List[str] = Field(..., description="Tips specific to this role.")
