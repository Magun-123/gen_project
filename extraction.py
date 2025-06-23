# extraction.py
import spacy
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    from dataset import load_documents
    docs = load_documents(2)
    for doc in docs:
        print("Entities:", extract_entities(doc[:300]))
