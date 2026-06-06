# Legal AI Assistant

## Overview

This project is an end-to-end Legal AI Assistant built using Retrieval-Augmented Generation (RAG) principles. The system processes legal documents, retrieves relevant evidence, generates grounded legal summaries, and improves future drafts through operator feedback.

## Key Features

* OCR and PDF text extraction
* Structured field extraction
* Semantic chunking and embeddings
* FAISS vector database
* Evidence retrieval
* Grounded legal draft generation using Llama 3.1 (Ollama)
* Human feedback learning loop
* Streamlit-based web interface
* Evaluation framework

## System Architecture

Document
→ OCR & Extraction
→ Structured Data
→ Chunking
→ Embeddings
→ FAISS Vector Store
→ Evidence Retrieval
→ Llama 3.1
→ Grounded Draft
→ Operator Feedback
→ Improved Future Drafts

## Technology Stack

* Python
* Ollama
* Llama 3.1
* FAISS
* Sentence Transformers
* Streamlit
* SQLite
* pdfplumber
* pytesseract

## Project Structure

document_processing/
retrieval/
drafting/
feedback/
evaluation/

streamlit_app.py
build_index.py
requirements.txt

## Setup Instructions

Create virtual environment:

python -m venv venv

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Download model:

ollama pull llama3.1

Build index:

python build_index.py

Run application:

streamlit run streamlit_app.py

## Evaluation Results

* Retrieval Accuracy: 100%
* Grounding Check: Passed
* Evidence Traceability: Enabled
* Feedback Learning: Implemented

## Future Improvements

* Multi-document retrieval
* Hybrid search
* Advanced legal citation support
* Cloud deployment

## Author

Aditya.
