def load_job_skills(file_path):
    """
    Read skill weights from a text file formatted as:
    skill:weight
    Example:
    python:5
    selenium:3
    """
    
    skills = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                skill, weight = parts[0].strip().lower(), int(parts[1].strip())
                skills[skill] = weight
    return skills

# Test
if __name__ == "__main__":
    skills = load_job_skills("data/job_description.txt")
    print(skills)
