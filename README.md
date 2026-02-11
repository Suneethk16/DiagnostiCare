# DiagnostiCare

**DiagnostiCare** is a multiagent clinical decision support system that analyzes medical reports and transforms them into structured clinical insights using LangGraph based agent orchestration.

The system processes both text and real world hospital PDFs (including scanned documents via OCR), performs clinical reasoning, generates action plans, applies safety validation and stores patient history with timeline tracking.

## Features

- Extract structured medical data from unstructured reports  
- Perform clinical reasoning over diagnoses and lab results  
- Generate automated follow up action plans  
- Apply safety checks with human-in-the-loop validation  
- Maintain a persistent patient timeline using a database  
- OCR-enabled PDF ingestion (Tesseract)  
- Graph based multi agent orchestration (LangGraph)  
- Automated testing with pytest  
- CI/CD pipeline with GitHub Actions  

## Tech Stack

- **LangGraph** – Multi agent orchestration  
- **Pydantic** – Structured schema validation  
- **Streamlit** – Interactive dashboard  
- **SQLAlchemy + SQLite** – Database persistence  
- **Tesseract OCR** – PDF text extraction  
- **Pytest** – Automated testing  
- **GitHub Actions** – CI/CD  


## Architecture Overview

The system uses a graph-based multi-agent pipeline:

1. **Document Agent** – Extract structured medical information  
2. **Reasoning Agent** – Interpret clinical significance  
3. **Action Agent** – Generate follow up care plan  
4. **Safety Agent** – Flag high-risk actions and enforce approval  

All agents share a structured state through LangGraph.

## How to Run

### 1️) Install dependencies
pip install -r requirements.txt

### 2) Install OCR system dependencies
brew install tesseract
brew install poppler

### 3) Initialize database
python init_db.py

### 4) Start the dashboard
streamlit run dashboard.py

### 5) Run Tests
pytest -v
