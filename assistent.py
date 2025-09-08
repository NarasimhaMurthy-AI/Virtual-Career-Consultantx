import json
import re
from typing import List, Dict

def load_data(path: str = "data/career_data.json") -> List[Dict]:
    """Load career data from JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalize(text: str) -> str:
    """Convert text to lowercase and remove special characters."""
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text.strip()

def parse_skills(text: str) -> List[str]:
    """Split skills by comma, semicolon, or newline."""
    parts = re.split(r"[,;\n]+", text or "")
    return [normalize(p) for p in parts if p.strip()]

def recommend(skills_input: str, education: str, interests: List[str]) -> List[str]:
    """Recommend careers based on skills, education, and interests."""
    skills = set(parse_skills(skills_input))
    careers = load_data()
    recs: List[str] = []

    for job in careers:
        # Normalize career requirements
        job_skills = {normalize(s) for s in job["skills"]}
        job_edu = set(job["education"])
        job_interests = set(job["interests"])

        # Matching conditions
        skill_match = skills.intersection(job_skills)
        edu_match = education in job_edu
        interest_match = set(interests).intersection(job_interests)

        if skill_match and edu_match and interest_match:
            recs.append(job["career"])

    return recs or ["No matching careers found. Try adding more skills."]
