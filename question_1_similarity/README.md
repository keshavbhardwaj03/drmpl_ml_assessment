# Text Similarity System for KeaBuilder

## Problem Statement
We need to build a lightweight system that can match a user query with the most similar existing inputs (e.g., leads or prompts) inside KeaBuilder.

## Approach
We implemented a text similarity system using:

- **TF-IDF Vectorization** → Converts text into numerical vectors  
- **Cosine Similarity** → Measures similarity between vectors  

## System Architecture

1. User Query
2. Vectorization
3. Cosine Similarity
4. Top Match Retrieval
5. Response

## Implementation Details

- **Framework:** FastAPI  
- **Vectorization:** Scikit-learn TF-IDF  
- **Similarity Metric:** Cosine Similarity  
- **Dataset:** 5 sample inputs simulating user prompts  

## Features

- Supports **top-k similar matches**
- Returns **similarity scores**
- Lightweight and fast
- Easily extendable

## Trade-offs

| Approach        | Pros                               | Cons                              |
|----------------|------------------------------------|-----------------------------------|
| TF-IDF         | Fast, simple, no API cost          | Limited semantic understanding    |
| Embeddings     | Better meaning capture             | Higher cost and latency           |

## Future Improvements

- Replace TF-IDF with:
  - Sentence Transformers
  - OpenAI Embeddings
- Use FAISS / Vector DB for scalability
- Add similarity threshold filtering
- Enable real-time data updates
- Improve semantic understanding

## KeaBuilder Use Cases

- Matching user prompts to templates  
- Suggesting similar funnels  
- Detecting duplicate leads  
- Enhancing chatbot responses  


## How to Run (Step-by-Step)

### Step 1: Install Dependencies

>pip install fastapi uvicorn scikit-learn

### Step 2: Run the API

>uvicorn similarity_api:app --host 0.0.0.0 --port 9000 --reload

### Step 3: Run health check in Powershell

>curl.exe http://localhost:9000/healthy/

### Step 4: Run for query in Pwershell

>Invoke-RestMethod -Uri "http://localhost:9000/find_similar/" -Method POST -ContentType "application/json" -Body '{"query":"Create marketing funnel for gym business","top_k":2}'

## Sample Inputs & Outputs

### Example 1

**Request**
{
  "query": "Create marketing funnel for gym business",
  "top_k": 2
}

**Response**

{
  "query": "Create marketing funnel for gym business",
  "top_matches": [
    {
      "matched_text": "Generate a sales funnel for fitness products",
      "similarity_score": 0.82
    },
    {
      "matched_text": "Optimize ads for lead generation",
      "similarity_score": 0.34
    }
  ]
}

### Example 2

**Request**
{
  "query": "Customer support chatbot for website",
  "top_k": 1
}

**Response**

{
  "query": "Customer support chatbot for website",
  "top_matches": [
    {
      "matched_text": "Design chatbot flow for customer support",
      "similarity_score": 0.91
    }
  ]
}

### Example 3

**Request**
{
  "query": "Email marketing for online store",
  "top_k": 3
}

**Response**
{
  "query": "Email marketing for online store",
  "top_matches": [
    {
      "matched_text": "Build an email campaign for ecommerce store",
      "similarity_score": 0.88
    },
    {
      "matched_text": "Optimize ads for lead generation",
      "similarity_score": 0.29
    },
    {
      "matched_text": "Generate a sales funnel for fitness products",
      "similarity_score": 0.18
    }
  ]
}