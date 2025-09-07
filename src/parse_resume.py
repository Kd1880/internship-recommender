<<<<<<< HEAD
from pyresparser import ResumeParser

# Resume ka path
data = ResumeParser('data/sample_resume.pdf').get_extracted_data()

print("Parsed Resume Data:", data)
=======
import pdfplumber

resume_text = ""
with pdfplumber.open("data/sample_resume.pdf") as pdf:
    for page in pdf.pages:
        resume_text += page.extract_text() + "\n"

print("Extracted Resume Text:\n")
print(resume_text)
>>>>>>> 8e54b73 (Updated resume parser and added CSV export)
