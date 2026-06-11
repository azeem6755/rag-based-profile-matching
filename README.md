# RAG-Based Profile Matching System

An intelligent, sandboxed recruitment candidate matching engine that parses resumes, extracts structured candidate profiles, builds a local vector database, and executes hybrid search algorithms to match profiles with job descriptions using **LM Studio**.

---

## 🚀 Key Features

* **Advanced Document Chunking:** Section-aware chunking detects and groups content from experience, education, skills, and projects, ensuring semantic continuity.
* **LLM-Based Metadata Extraction:** Leverages `google/gemma-4-e4b` in JSON Schema mode to reliably extract Name, Skills, Years of Experience, and Education details.
* **Hybrid Search Engine:** Combines semantic search (cosine similarity vectors using `text-embedding-nomic-embed-text-v1.5`) with hard constraints (minimum experience and must-have skills).
* **Weighted Scoring Model:** Candidate scoring ranges from 0 to 100 based on a balanced formula:
  * **60%** Semantic Similarity
  * **30%** Required Skills Matching
  * **10%** Experience Proximity
* **LLM Verification & Reasoning:** Reviews matches to locate exact proving excerpts and output natural language rationale explaining why a profile is selected.
* **Structured Output Schema:** Guarantees standard output format using rigid JSON schema formatting.

---

## 📁 Repository Structure

```
rag-based-profile-matching/
├── README.md               # Main documentation
├── requirements.txt        # Dependencies
├── fs_tools.py             # File system extraction tools & sandboxing guardrails
├── resume_rag.py           # Parsing, chunking, and database ingestion pipeline
├── job_matcher.py          # Hybrid retrieval, scoring, and explanation engine
├── verify_matching.py      # Automated scenario and filter test suite
├── resumes/                # Directory containing mock candidate resumes
└── docs/
    ├── problemStatement.md # Context & specifications
    └── architecture.md     # System architecture design & diagrams
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- [LM Studio](https://lmstudio.ai/) running locally on port `1234` with the following models loaded:
  - Chat Model: `google/gemma-4-e4b`
  - Embedding Model: `text-embedding-nomic-embed-text-v1.5`

### 2. Configure Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🎯 Usage Instructions

### Step 1: Ingest Resume Documents
To parse mock files from the `resumes/` folder, chunk them, extract metadata via LLM, and build the persistent ChromaDB collections, run:
```bash
python resume_rag.py
```

### Step 2: Query and Match Jobs
Use `job_matcher.py` with the `--jd` parameter to search for matches. You can optional specify hard experience filters (`--min-experience`) and must-have skills (`--skills`).

#### Example 1: Basic Semantic Search
```bash
python job_matcher.py --jd "Looking for a Software Engineer with Django development expertise."
```

#### Example 2: Hybrid Query with Constraints
```bash
python job_matcher.py --jd "Looking for a Python Developer." --min-experience 5 --skills "Python,Docker"
```

---

## 🧪 Verification & Testing

To run the automated integration tests verifying experience filtering and must-have skill matches:
```bash
python verify_matching.py
```
