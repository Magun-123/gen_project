# summarization.py
from gensim.summarization import summarize

def summarize_text(text, ratio=0.2):
    try:
        return summarize(text, ratio=ratio)
    except:
        return text  # fallback if too short

if __name__ == "__main__":
    from dataset import load_documents
    docs = load_documents(2)
    for doc in docs:
        print("Summary:\n", summarize_text(doc[:1000]), "\n")
