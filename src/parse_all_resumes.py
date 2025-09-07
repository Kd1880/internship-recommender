import os
import re
import spacy
import pandas as pd
from PyPDF2 import PdfReader

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Folder containing resumes
RESUME_FOLDER = "data"

# Output CSV file
OUTPUT_CSV = "parsed_resumes.csv"

# Regex patterns
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
PHONE_REGEX = r'\+?\d[\d\s-]{7,}\d'
EDUCATION_KEYWORDS = ["Bachelor", "B\.Sc", "B\.Tech", "Master", "M\.Sc", "M\.Tech", "PhD", "Diploma", "High School", "HSC", "SSC"]
SKILLS_LIST = ["Python", "Java", "C++", "Machine Learning", "Deep Learning", "SQL", "MySQL", "TensorFlow", "Keras", "PyTorch"]  # Add more if needed

# Helper functions
def extract_text(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_emails(text):
    return re.findall(EMAIL_REGEX, text)

def extract_phones(text):
    return re.findall(PHONE_REGEX, text)

def extract_education(text):
    edu = []
    for keyword in EDUCATION_KEYWORDS:
        if re.search(keyword, text, re.IGNORECASE):
            edu.append(keyword)
    return edu

def extract_skills(text):
    skills = []
    for skill in SKILLS_LIST:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            skills.append(skill)
    return skills

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

# Main parsing loop
resumes = [f for f in os.listdir(RESUME_FOLDER) if f.lower().endswith(".pdf")]
parsed_data = []

if not resumes:
    print("⚠️ No resumes found.")
else:
    for resume_file in resumes:
        path = os.path.join(RESUME_FOLDER, resume_file)
        print(f"Parsing: {resume_file}")
        try:
            text = extract_text(path)
            data = {
                "File": resume_file,
                "Name": extract_name(text),
                "Email": ", ".join(extract_emails(text)),
                "Phone": ", ".join(extract_phones(text)),
                "Education": ", ".join(extract_education(text)),
                "Skills": ", ".join(extract_skills(text))
            }
            parsed_data.append(data)
        except Exception as e:
            print(f"❌ Error parsing {resume_file}: {e}")
        print("-" * 50)

# Save to CSV
if parsed_data:
    df = pd.DataFrame(parsed_data)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"✅ All parsed data saved to {OUTPUT_CSV}")
