import spacy

# Load NLP model only once
nlp = spacy.load("en_core_web_md")

def calculate_semantic_similarity(resume_text, job_description):
    """
    Returns a similarity score between 0 and 100
    """
    try:
        resume_doc = nlp(resume_text)
        job_doc = nlp(job_description)
        similarity = resume_doc.similarity(job_doc)  # spaCy similarity between 0 and 1
        return round(similarity * 100, 2)  # Convert to % and round
    except Exception as e:
        print(f"NLP similarity error: {e}")
        return 0
