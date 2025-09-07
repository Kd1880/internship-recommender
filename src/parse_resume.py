from pyresparser import ResumeParser

# Resume ka path (data folder me rakhenge)
data = ResumeParser('data/sample_resume.pdf').get_extracted_data()

print("Parsed Resume Data:", data)
