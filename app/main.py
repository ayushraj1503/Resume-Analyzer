from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import analyze

app = FastAPI(
    title="AI Resume & JD Analyzer",
    description="LLM-powered tool to analyze resumes against job descriptions and return structured insights.",
    version="1.0.0",
)

app.include_router(analyze.router, prefix="/api", tags=["Analysis"])
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", include_in_schema=False)
def serve_ui():
    return FileResponse("static/index.html")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "AI Resume Analyzer"}
