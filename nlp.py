import spacy
from transformers import pipeline

# Load spaCy's pre-trained medical model
nlp = spacy.load("en_core_sci_md")

# Summarization model (from Hugging Face's Transformers library)
summarizer = pipeline("summarization")

# Function to extract medical entities (e.g., symptoms, diseases) from text
def extract_medical_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to summarize medical notes using transformer-based summarization
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']