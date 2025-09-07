from pyresparser import ResumeParser

# Resume ka path
data = ResumeParser('data/sample_resume.pdf').get_extracted_data()

print("Parsed Resume Data:", data)
