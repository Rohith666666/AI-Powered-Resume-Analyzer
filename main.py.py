from fastapi import FastAPI, File, UploadFile, HTTPException
from nlp_logic import extract_text_from_pdf, parse_resume_text

app = FastAPI(title="AI Resume Parser API", version="1.0")

@app.get("/")
async def health_check():
    return {"status": "active", "service": "AI Resume Parser API"}

@app.post("/api/v1/parse")
async def parse_resume_endpoint(file: UploadFile = File(...)):
    """Endpoint to upload a PDF resume and return extracted NLP entities."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file format. Only PDF files are supported.")
    
    try:
        # 1. Read the file stream asynchronously 
        file_bytes = await file.read()
        
        # 2. Extract text using pdfplumber (optimized for memory efficiency)
        raw_text = extract_text_from_pdf(file_bytes)
        
        if not raw_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text. The PDF might be an image/scanned.")
        
        # 3. Parse entities using spaCy NLP pipeline
        parsed_data = parse_resume_text(raw_text)
        
        return {
            "filename": file.filename,
            "status": "success",
            "data": parsed_data
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error processing document: {str(e)}")