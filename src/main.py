from fastapi import FastAPI, UploadFile, File
from src.scanner import analyze_match  # Updated import path

app = FastAPI()

@app.post("/analyze")
async def analyze_resume(job_desc: UploadFile = File(...), resume: UploadFile = File(...)):
    job_text = (await job_desc.read()).decode("utf-8")
    resume_text = (await resume.read()).decode("utf-8")

    result = analyze_match(resume_text, job_text)
    return result
