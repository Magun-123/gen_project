# 🧠 NLP Document Analysis Agent

This project demonstrates a complete pipeline for analyzing unstructured text documents using Natural Language Processing (NLP). It includes:

- Extraction of key entities (names, dates, locations, metrics, etc.)
- Automatic summarization of documents
- A conceptual agentic component to answer complex queries by chaining extraction and summarization

---

## 📦 Project Structure

```bash
gen_project/
│
├── dataset.py            # Load and sample documents from Reuters corpus (via NLTK)
├── preprocessing.py      # Basic text cleaning and preprocessing
├── extraction.py         # Entity extraction using SpaCy
├── summarization.py      # TextRank-based summarization using Gensim
├── agent.py              # AI agent that navigates documents using extraction + summarization
├── requirements.txt      # List of dependencies
├── README.md             # This file
└── report.pdf            # Brief summary of approach, results, and agent architecture
