#### 📌 Introduction
This project is aimed at processing unstructured text documents and enabling an AI agent to extract insights using NLP techniques.

#### 🧱 Approach
- **Dataset**: NLTK Reuters Corpus
- **Preprocessing**: Lowercasing, tokenization, stop word removal
- **Entity Extraction**: Using SpaCy for Named Entity Recognition (NER)
- **Summarization**: Using Gensim's TextRank extractive summarizer

#### 📈 Results
- Extracted key entities like organizations, locations, dates.
- Generated meaningful summaries from articles.
- Agent identified top topics across multiple documents.

#### 🤖 Agent Design
- **Goal**: Answer “What are the top issues/complaints/topics?”
- **Tools Used**: `summarize_text`, `extract_entities`
- **Workflow**:
  1. Search documents
  2. Extract entities
  3. Generate summaries
  4. Aggregate insights
- **Optional Memory**: Cache previously seen answers or documents.
