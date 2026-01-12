import os
from modules.extract_text import extract_text
from modules.keyword_matcher import calculate_keyword_score
from modules.job_parser import load_job_skills
import pandas as pd
from modules.email_sender import send_email_with_attachment
from modules.nlp_analyzer import calculate_semantic_similarity

def process_resumes(resume_folder, job_skills, job_description):
    results = []

    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(('.pdf', '.docx')):
            print(f"Processing {filename}...")
            resume_text = extract_text(file_path)

            keyword_score = calculate_keyword_score(resume_text, job_skills)
            nlp_score = calculate_semantic_similarity(resume_text, job_description)
            
            final_score = round((keyword_score['relevance_%'] * 0.7) + (nlp_score * 0.3), 2)
            
            results.append({
                "Resume": filename,
                "Keyword Score %": keyword_score['relevance_%'],
                "NLP Similarity %": nlp_score,
                "Final Score %": final_score,
                "Matched Skills": ", ".join(keyword_score['matched_skills'])
            })

    return results

def save_results_to_excel(results, output_path="resume_screening_results.xlsx"):
    df = pd.DataFrame(results)
    df = df.sort_values(by="Final Score %", ascending=False)  # Rank highest first
    df.to_excel(output_path, index=False)
    print(f"\nReport generated: {output_path}")
    

if __name__ == "__main__":
    print("Starting Resume Screening...\n")

    resume_folder = "data/resumes"
    job_skills_file = "data/job_description.txt"

    # Load job skill weights
    job_skills = load_job_skills(job_skills_file)
    with open("data/job_description.txt", "r") as file:
        job_description_text = file.read()

    # Process resumes
    results = process_resumes(resume_folder, job_skills, job_description_text)

    # Save report
    save_results_to_excel(results)

    print("\n Screening Completed Successfully!")

    save_results_to_excel(results)

    # Email credentials (REPLACE with environment variables in real case)
    sender_email = "alvinconcordofficial@gmail.com"
    app_password = "dlsb yqwd qshp razn"  # From Gmail app password
    receiver_email = "akashkumarrawani5457@gmail.com"

    send_email_with_attachment(
        sender_email,
        app_password,
        receiver_email,
        subject="Automated Resume Screening Results",
        body="Hello,\n\nPlease find attached the latest resume screening report.\n\nRegards,\nResume Bot",
        attachment_path="resume_screening_results.xlsx"
    )