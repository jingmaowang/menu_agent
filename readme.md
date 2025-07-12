# 🍝 Menu Agent — Italian Dish Explainer

This project is a Retrieval-Augmented Generation (RAG) agent that explains Italian dish names in English. It uses LangChain, FAISS, and Streamlit to provide detailed, context-aware culinary explanations.

---

## 🔍 Features

- 🧠 RAG agent powered by LangChain
- 📖 Supports Italian-to-English dish explanation with ingredients, preparation, and cultural background
- 🔍 FAISS vector search over menu data
- 🌐 Streamlit web interface
- 📊 Judgeval integration for observability and evaluation

---

## 🏗️ Tech Stack

- **LLM**: DeepSeek via OpenAI SDK (or OpenAI-compatible API)
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **RAG**: LangChain + FAISS
- **Frontend**: Streamlit
- **Evaluation**: Judgeval Tracer + Evals

---

## 🚀 Getting Started
### 🔑 API Keys Required

To run this project, you must provide the following API keys:

1. **LLM API Key** — Used to access the language model.  
   *In this project, I use [DeepSeek](https://deepseek.com) as the LLM provider.*

2. **Judgment Labs API Key** — Used for tracing and evaluation via `judgeval`.

You can obtain a Judgment Labs API key by following their official documentation:  
👉 https://docs.judgmentlabs.ai/documentation

Set these API keys directly in the code (`agent.py`), or configure them as environment variables.


###  1.```
.pip install -r requirements.txt
```
pip install -r requirements.txt