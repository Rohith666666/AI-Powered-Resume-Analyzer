import pdfplumber
import spacy
import io

# Load the English NLP model for entity recognition
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise RuntimeError("spaCy model not found. Run: python -m spacy download en_core_web_sm")

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extracts raw text from a PDF byte stream using pdfplumber."""
    text = ""
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text

def parse_resume_text(text: str) -> dict:
    """Processes text with spaCy to extract Named Entities (Entities, Orgs, Locations)."""
    doc = nlp(text)
    
    # Categorize extracted entities
    entities = {
        "PERSON": [],
        "ORG": [], # Organizations/Companies
        "GPE": [], # Locations
        "WORK_OF_ART": [] # Often catches degrees or specific project names
    }
    
    for ent in doc.ents:
        if ent.label_ in entities and ent.text.strip() not in entities[ent.label_]:
            entities[ent.label_].append(ent.text.strip())
            
    return {
        "document_length": len(text),
        "extracted_entities": entities
    }