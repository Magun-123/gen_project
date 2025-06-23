# preprocessing.py
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    words = [w for w in tokens if w.isalnum() and w not in stop_words]
    return words

if __name__ == "__main__":
    from dataset import load_documents
    docs = load_documents(2)
    for doc in docs:
        print(preprocess_text(doc[:500]))
