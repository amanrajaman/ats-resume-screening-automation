import re

def calculate_keyword_score(resume_text, job_skills):
    """
    resume_text: cleaned extracted text from resume (string)
    job_skills: dict {skill: weight}
    """

    score = 0
    matched_skills = []

    for skill, weight in job_skills.items():
        # Check whole word match (avoid "java" inside "javascript")
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, resume_text):
            score += weight
            matched_skills.append(skill)

    max_score = sum(job_skills.values())
    relevance_percentage = round((score / max_score) * 100, 2) if max_score > 0 else 0

    return {
        "matched_skills": matched_skills,
        "total_score": score,
        "max_score": max_score,
        "relevance_%": relevance_percentage
    }

if __name__ == "__main__":
    sample_resume_text = "experienced python automation engineer with selenium and api testing"
    job_skills = {"python": 5, "automation": 4, "api testing": 3, "java": 2}

    result = calculate_keyword_score(sample_resume_text, job_skills)
    print(result)
