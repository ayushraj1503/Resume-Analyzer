from fastapi import APIRouter, HTTPException
from app.models import AnalyzeRequest, AnalyzeResponse
from app.services import analyze_resume_vs_jd

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse, summary="Analyze Resume vs Job Description")
def analyze(request: AnalyzeRequest):
    """
    Submit a resume and a job description.
    Returns a structured AI analysis including:
    - Match score (0–100)
    - Matched and missing skills
    - Resume improvement suggestions
    - Interview preparation tips
    """
    if len(request.resume_text.strip()) < 50:
        raise HTTPException(status_code=400, detail="Resume text is too short. Please provide full resume content.")
    if len(request.job_description.strip()) < 50:
        raise HTTPException(status_code=400, detail="Job description is too short.")

    try:
        result = analyze_resume_vs_jd(request.resume_text, request.job_description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
