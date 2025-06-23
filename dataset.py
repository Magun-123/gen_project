# dataset.py
import nltk
from nltk.corpus import reuters
import random

nltk.download('reuters')
nltk.download('punkt')

def load_documents(num_docs=10):
    file_ids = reuters.fileids()
    selected_ids = random.sample(file_ids, num_docs)
    return [reuters.raw(doc_id) for doc_id in selected_ids]

if __name__ == "__main__":
    docs = load_documents()
    for i, doc in enumerate(docs[:3]):
        print(f"Doc {i+1}:\n", doc[:300], "\n")
