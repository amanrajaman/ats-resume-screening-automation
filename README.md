# Resume Screening Bot – Python Automation Project
## 🚀 Overview

This project automates the resume screening process similar to an Applicant Tracking System (ATS). It extracts text from resumes (PDF/DOCX), compares them with a job description using keyword matching and NLP-based semantic analysis, ranks candidates, and generates a report (Excel), which is optionally emailed to HR.

This tool saves time and improves hiring efficiency, making it ideal for demonstrating automation skills in an interview.

---

## 🎯 Features

- Extracts resume text (PDF & DOCX)
- Keyword-based scoring using weighted matching
- Semantic similarity scoring using spaCy NLP
- Weighted combined score for ranking candidates
- Generates Excel report with top resumes
- Optional email automation to send report to HR
- Modular code structure, easily scalable

---

## 🛠️ Tech Stack
- Category	Tools/Libraries
- Language	Python
- PDF Parsing	PyPDF2
- DOCX Parsing	python-docx
- NLP Matching	spaCy (en_core_web_md)
- Data Handling	pandas
- Automation	schedule (optional), smtplib
- Reporting	Excel writer
- Logging	logging

---

## 📂 Project Structure
```bash
resume_screening_bot/
│
├── data/
│   ├── resumes/                 ← sample resumes
│   ├── job_description.txt      ← required skills & weights
│
├── modules/
│   ├── extract_text.py          ← PDF/DOCX extraction
│   ├── keyword_matcher.py       ← keyword matching logic
│   ├── nlp_analyzer.py          ← semantic similarity
│   ├── job_parser.py            ← parsing job skills
│   ├── email_sender.py          ← email automation
│
├── main.py                      ← main execution script
├── README.md
└── requirements.txt
```

---

## 📌 Installation
```bash
# git clone https://github.com/your_username/resume-screening-bot.git
# cd resume-screening-bot

# pip install -r requirements.txt

# python -m spacy download en_core_web_md
```
---

## 📥 Setup Configuration

**1️⃣ Add job description weights**
- *Create*
```bash
data/job_description.txt
python:5
automation:4
selenium:3
api testing:3
sql:4
jenkins:2
docker:2
```

---

**2️⃣ Add sample resumes**
- Place PDF/DOCX files in data/resumes/


---

**3️⃣ (Optional) Configure email**
**In main.py**
```bash
sender_email = os.getenv("EMAIL_USER")
app_password = os.getenv("EMAIL_PASS")
receiver_email = "hr@example.com"

- Set environment variables:
setx EMAIL_USER "your_email@gmail.com"
setx EMAIL_PASS "your_app_password"
```

---

## ▶️ Run the Project
```bash
python main.py
```

---

## 📊 Sample Output (Excel Report)
| Resume       | Keyword % | NLP % | Final %  | Matched Skills     |
| ------------ | --------- | ----- | -------- | ------------------ |
| resume1.pdf  | 90        | 80    | **87.0** | python, automation |
| resume2.docx | 60        | 85    | **68.5** | selenium           |
| resume3.pdf  | 40        | 75    | **53.5** | api testing        |

---

## 🔮 Future Enhancements

- Streamlit web UI for demo
- Use OCR (pytesseract) for scanned resumes
- Integration with LinkedIn/API
- Dashboard with search & filters

---

## 📚 Requirements File (example)
```bash
pypdf2
python-docx
pandas
spacy
openpyxl
schedule
```

---

## 🤝 Contributing
Contributions welcome! Fork the repo and submit a PR.

---

## 📬 Contact

- 👨‍💻 Aman Raj Aman
- 📧 amanrajaman011@gmail.com
🔗- [LinkedIn](www.linkedin.com/in/aman-raj-aman011)
  - [GitHub profile](https://github.com/amanrajaman)

