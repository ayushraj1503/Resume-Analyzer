# 🤖 AI Resume & JD Analyzer

> An LLM-powered REST API built with **FastAPI** and **GROQ openai/gpt-oss-120b** that analyzes a candidate's resume against a job description and returns structured, actionable insights.

---

## 📸 What It Does

Paste a resume and a job description → get back:

- ✅ **Match Score** (0–100) with visual ring indicator  
- 🧠 **AI Summary** of overall fit  
- ✅ **Matched Skills** already present  
- ⚠️ **Skill Gaps** with importance level and how to close them  
- ✏️ **Resume Improvement Suggestions** (specific bullet rewrites)  
- 🎯 **Interview Prep Tips** tailored to the role  

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| LLM | Groq openai/gpt-oss-120b (structured JSON output) |
| Data Validation | Pydantic v2 |
| Server | Uvicorn (ASGI) |
| Frontend | Vanilla JS + HTML/CSS (served by FastAPI) |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer-api.git
cd resume-analyzer-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

```
GROQ_API_KEY=sk-...
```

### 5. Run the server

```bash
python run.py
```

Server starts at: `http://localhost:8000`  
Swagger docs at: `http://localhost:8000/docs`  
UI at: `http://localhost:8000`

---

## 📡 API Reference

### `POST /api/analyze`

**Request Body:**
```json
{
  "resume_text": "Full resume text here...",
  "job_description": "Full JD text here..."
}
```

**Response:**
```json
{
  "match_score": 72,
  "summary": "Strong Python and ML background. Needs JavaScript and LLM tooling.",
  "matched_skills": ["Python", "FastAPI", "SQL", "Pandas"],
  "missing_skills": [
    {
      "skill": "LangChain",
      "importance": "High",
      "suggestion": "Build a small RAG app using LangChain + OpenAI API and put it on GitHub."
    }
  ],
  "resume_improvements": [
    "Add a line mentioning your FastAPI project with endpoint count and deployment method.",
    "Quantify the ML model deployment: mention latency, throughput, or users served."
  ],
  "interview_prep_tips": [
    "Be ready to explain how you'd integrate an LLM into an existing Python microservice.",
    "Practice explaining the difference between fine-tuning and prompt engineering."
  ]
}
```

### `GET /health`

Returns service health status.

---

## 🗂️ Project Structure

```
resume-analyzer-api/
├── app/
│   ├── main.py          # FastAPI app & routing setup
│   ├── models.py        # Pydantic request/response schemas
│   ├── services.py      # GROQ API integration & prompt logic
│   └── routers/
│       └── analyze.py   # /api/analyze endpoint
├── static/
│   └── index.html       # Standalone frontend UI
├── run.py               # Uvicorn entry point
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 💡 Key Engineering Decisions

- **Structured JSON output mode** (`response_format: json_object`) from GROQ ensures the API always returns valid, parseable JSON — no regex or fragile parsing needed.
- **Pydantic v2 models** enforce type safety on both input validation and output serialization automatically.
- **Separation of concerns**: routing, business logic (services), and data models are split into separate modules, making it easy to swap the LLM provider or add new endpoints.

---

## 🔮 Future Improvements

- [ ] Add PDF upload support (extract text from resume PDF)
- [ ] Support multiple LLM providers (Gemini, Claude, Mistral) via a provider abstraction layer
- [ ] Add Redis caching to avoid re-analyzing identical inputs
- [ ] Deploy to Railway / Render with one-click button
- [ ] Add rate limiting middleware

---

## 👤 Author

**Ayush Raj**  
[LinkedIn](https://linkedin.com/in/ayush-raj-15m03) · [GitHub](https://github.com/ayushraj1503)

---

## 📄 License

MIT
