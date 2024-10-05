from flask import Flask, render_template, request
from pymongo import MongoClient
from nlp import extract_medical_entities, summarize_text

app = Flask(__name__)

# MongoDB connection (optional, if you want to store the notes)
client = MongoClient('mongodb://localhost:27017/')
db = client['medical_records']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the medical notes from the user input
    medical_notes = request.form['notes']
    
    # Step 1: Extract medical entities (e.g., symptoms, diseases)
    extracted_entities = extract_medical_entities(medical_notes)
    
    # Step 2: Summarize the medical notes
    summary = summarize_text(medical_notes)
    
    # Optionally, store the medical notes in MongoDB
    db['records'].insert_one({
        'notes': medical_notes,
        'entities': extracted_entities,
        'summary': summary
    })

    # Render the results on a new page or return them in JSON format
    return render_template('result.html', entities=extracted_entities, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
