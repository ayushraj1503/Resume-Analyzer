import os
import json
from groq import Groq
from app.models import AnalyzeResponse
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an expert technical recruiter and career coach with deep knowledge of software engineering, data science, and AI roles.

Your task is to analyze a candidate's resume against a job description and return a structured JSON analysis.

You MUST respond ONLY with a valid JSON object — no markdown, no explanation, no extra text.

The JSON schema must be:
{
  "match_score": <integer 0–100>,
  "summary": "<2–3 sentence assessment>",
  "matched_skills": ["<skill1>", "<skill2>", ...],
  "missing_skills": [
    {
      "skill": "<skill name>",
      "importance": "<High | Medium | Low>",
      "suggestion": "<how to learn or demonstrate this skill>"
    }
  ],
  "resume_improvements": ["<specific bullet point improvement 1>", ...],
  "interview_prep_tips": ["<role-specific tip 1>", ...]
}

Be specific, honest, and actionable. Do not be generic.
"""


def analyze_resume_vs_jd(resume_text: str, job_description: str) -> AnalyzeResponse:
    user_message = f"""
RESUME:
{resume_text}

---

JOB DESCRIPTION:
{job_description}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.3,
        max_tokens=1500,
        response_format={"type": "json_object"},  # Structured output mode
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)
    return AnalyzeResponse(**data)
