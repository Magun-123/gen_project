# agent.py
from dataset import load_documents
from preprocessing import preprocess_text
from extraction import extract_entities
from summarization import summarize_text
from collections import Counter

def agent_answer_top_issues():
    docs = load_documents(10)
    issues = []
    summaries = []

    for doc in docs:
        summaries.append(summarize_text(doc))
        ents = extract_entities(doc)
        issues.extend([e[0] for e in ents if e[1] in ("ORG", "PRODUCT", "GPE", "EVENT", "NORP", "DATE")])

    top_issues = Counter(issues).most_common(5)
    return top_issues, summaries[:3]

if __name__ == "__main__":
    issues, top_summaries = agent_answer_top_issues()
    print("🔍 Top Issues:")
    for item in issues:
        print("-", item)

    print("\n📝 Example Summaries:")
    for summary in top_summaries:
        print("-", summary[:300], "\n")
