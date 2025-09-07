import pdfplumber

resume_text = ""
with pdfplumber.open("data/sample_resume.pdf") as pdf:
    for page in pdf.pages:
        resume_text += page.extract_text() + "\n"

print("Extracted Resume Text:\n")
print(resume_text)
