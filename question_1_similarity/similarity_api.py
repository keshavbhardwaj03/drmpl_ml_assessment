from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Initialize FastAPI app
app = FastAPI(title="KeaBuilder Similarity Matching System")

# Dummy dataset (simulating prompts/leads in KeaBuilder)
documents = [
    "Generate a sales funnel for fitness products",
    "Create a landing page for real estate leads",
    "Build an email campaign for ecommerce store",
    "Design chatbot flow for customer support",
    "Optimize ads for lead generation"
]

# Convert text → vectors
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

# Request schema
class Query(BaseModel):
    query: str
    top_k: int


@app.get("/healthy/")
def home():
    print("Health check endpoint accessed")
    return {"message": "Similarity Matching API is running"}


@app.post("/find_similar/")
def find_similar(query: Query):
    try:
        print(f"Processing similarity query: {query}")
        print(f"Received query: {query.query} with top_k: {query.top_k}")
        query_vec = vectorizer.transform([query.query])
        similarities = cosine_similarity(query_vec, doc_vectors)[0]

        # Get top-k results
        top_k = min(query.top_k, len(documents))
        top_indices = similarities.argsort()[-top_k:][::-1]

        results = [
            {
                "matched_text": documents[i],
                "similarity_score": float(similarities[i])
            }
            for i in top_indices
        ]
        print(f"results: {results}")
        return {
            "query": query.query,
            "top_matches": results
        }
    
    except Exception as e:
        print(f"Error processing query: {e}")
        return {"error": "An error occurred while processing the query."}