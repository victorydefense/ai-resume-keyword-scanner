import pandas as pd
import re

def extract_keywords(text):
    """Extract words from a text and return a list of unique keywords."""
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)

def analyze_match(resume_text, job_text):
    """Compare resume and job description and return keyword match percentage."""
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    common_keywords = resume_keywords.intersection(job_keywords)
    match_percentage = (len(common_keywords) / len(job_keywords)) * 100 if job_keywords else 0

    return {
        "match_percentage": round(match_percentage, 2),
        "common_keywords": list(common_keywords)
    }
