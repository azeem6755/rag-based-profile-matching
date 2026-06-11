# RAG-Based Profile Matching System

## Project Overview & Context
Building upon the sandboxed document parser and assistant developed in Milestone 1, the RAG-Based Profile Matching System aims to automate and enhance candidate screening for recruiters and hiring managers. Instead of manually inspecting unstructured resumes (PDF, DOCX, TXT) or relying on simple, brittle keyword searches, this system leverages Retrieval-Augmented Generation (RAG) and hybrid semantic search.

By parsing resumes, extracting key metadata, storing embeddings in a vector database, and evaluating profiles against job descriptions (JDs), the system identifies the top matching candidates with detailed scoring and natural language reasoning.

---

## The Problem
Recruiting teams are routinely inundated with hundreds of resumes for open roles. Traditional sorting mechanisms suffer from two main issues:
1. **Brittle Keyword Matching:** Simple keyword-based filtering is inflexible. For example, a candidate with "Machine Learning Developer" listed on their resume might be missed if the query is strictly looking for "ML Engineer", despite the roles being semantically identical.
2. **Lack of Strict Constraint Filtering:** Pure semantic search (using vector embeddings) excels at matching concepts but can struggle with hard constraints. If a job description strictly requires "5+ years of Python experience" or "AWS certification," semantic search might still rank a candidate with only 1 year of Python highly because the rest of their profile is generally relevant.

We need a **hybrid approach** that combines semantic search (to capture conceptual similarity) with metadata/keyword filtering (to enforce hard constraints), followed by an intelligent ranking engine that scores matches and explains *why* a profile fits.

---

## System Architecture & Components

The system is split into two primary components:

### Part A: RAG System Setup
A document ingestion and preprocessing pipeline that prepares resumes for querying.
* **Document Processing Pipeline:**
  * Load unstructured resumes (`.pdf`, `.docx`, `.txt`) using the file system tools and sandboxing logic from Milestone 1.
  * Chunk resumes intelligently (e.g., preserving section boundaries like Education, Experience, and Skills).
  * Generate high-quality embeddings using standard models (e.g., OpenAI, Cohere, or Hugging Face).
  * Store the chunks and embeddings in a vector database (e.g., ChromaDB, Pinecone, or Weaviate).
* **Metadata Extraction:**
  * Extract key candidate metadata fields, specifically: `Name`, `Skills`, `Experience Years`, and `Education`.
  * Store metadata alongside the vector embeddings to facilitate hybrid queries and deterministic filtering.

### Part B: Job Matching Engine
An evaluation and ranking engine that processes job descriptions against the vector database.
* **Semantic & Hybrid Search:**
  * Accept a job description as input and convert it into a vector embedding.
  * Retrieve the top-K similar resumes (e.g., K = 10) from the database.
  * Perform hybrid search: combine semantic vector search with keyword/metadata filtering for critical skills and constraints.
* **Ranking & Scoring:**
  * Score matched profiles on a standardized 0–100 scale.
  * Enforce hard requirements (e.g., filtering out candidates who don't meet minimum years of experience or must-have skills).
  * Provide match reasoning explaining which specific sections and skills aligned with the job description.

---

## Output Interface

The system will output matches in a structured JSON format:

```json
{
  "job_description": "[Input Job Description]",
  "top_matches": [
    {
      "candidate_name": "[Candidate Name]",
      "resume_path": "[Path to Resume File]",
      "match_score": 92,
      "matched_skills": ["Python", "Machine Learning"],
      "relevant_excerpts": ["..."],
      "reasoning": "Strong match for ML experience..."
    }
  ]
}
```
