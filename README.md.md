# AI-Powered Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-009688)
![spaCy](https://img.shields.io/badge/spaCy-3.6.1-09A3D5)

An asynchronous REST API microservice designed to efficiently parse PDF resumes and extract critical named entities (skills, organizations, locations, etc.) using Natural Language Processing. 

Built with a strict focus on memory-efficient document ingestion and low-latency inference, this service acts as the core backend engine for modern ATS (Applicant Tracking System) pipelines.

## 🚀 Tech Stack
* **Framework:** FastAPI (Python)
* **NLP Engine:** spaCy (`en_core_web_sm`)
* **Document Processing:** pdfplumber
* **Server:** Uvicorn (ASGI)

## ⚡ Core Architecture & Optimizations
* **Memory-Efficient Extraction:** Utilizes `pdfplumber` to process PDF byte-streams in chunks, preventing large file overhead and avoiding memory bloat compared to standard `PyPDF` wrappers.
* **Asynchronous I/O:** Built on FastAPI to ensure non-blocking concurrent handling of multiple document uploads.
* **Lightweight NLP Pipeline:** Integrates a pre-trained spaCy model for rapid Named Entity Recognition (NER), classifying text into entities (Organizations, Persons, Locations) for downstream indexing.

## 🛠️ Local Setup & Installation

1. **Clone the repository:**
```bash
   git clone [https://github.com/your-username/AI-Powered-Resume-Analyzer.git](https://github.com/your-username/AI-Powered-Resume-Analyzer.git)
   cd AI-Powered-Resume-Analyzer

2. Create a virtual environment and install dependencies:

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt

   
3. Download the required spaCy NLP model:

   python -m spacy download en_core_web_sm

4. Run the server:

   uvicorn main:app --host 0.0.0.0 --port 8000 --reload

API Usage
POST /api/v1/parse
Accepts a PDF file upload (multipart/form-data) and returns a JSON payload of extracted NLP entities.

Example cURL Request:

curl -X 'POST' \
  '[http://127.0.0.1:8000/api/v1/parse](http://127.0.0.1:8000/api/v1/parse)' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample_resume.pdf;type=application/pdf'


Example Response:

JSON
{
  "filename": "sample_resume.pdf",
  "status": "success",
  "data": {
    "document_length": 4205,
    "extracted_entities": {
      "PERSON": ["John Doe", "Jane Smith"],
      "ORG": ["Juspay", "Google", "University of Technology"],
      "GPE": ["Bangalore", "India"],
      "WORK_OF_ART": ["B.Tech Computer Science"]
    }
  }
}

