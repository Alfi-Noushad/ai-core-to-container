import chromadb
from chromadb.utils import embedding_functions
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

chroma_client = chromadb.PersistentClient(path="./chroma_storage")

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

#create db
collection = chroma_client.get_or_create_collection(
    name="my_docs",
    embedding_function=sentence_transformer_ef
)

# FastApi
app = FastAPI(title="Semantic matchup")

class SearchQuery(BaseModel):
    query_text: str
    max_results: int = 1

@app.post("/semantic-search", status_code=status.HTTP_200_OK)
def semantic_search_endpoint(data: SearchQuery):
    if not data.query_text.strip():
        raise HTTPException(
            status_code=status.HTTP_420_UNPROCESSABLE_ENTITY, 
            detail="Query text cannot be empty."
        )
    
    try:
        # Query the database collection using semantic distance matching
        raw_results = collection.query(
            query_texts=[data.query_text],
            n_results=data.max_results
        )

        # Check if any documents were found
        if not raw_results["documents"] or not raw_results["documents"][0]:
            return {"message": "No matching context found in vector space.", "results": []}
        
        # Format the matrix output arrays into a clean client-side dictionary list
        formatted_results = []
        for i in range(len(raw_results["documents"][0])):
            formatted_results.append({
                "id": raw_results["ids"][0][i],
                "matched_text": raw_results["documents"][0][i],
                "metadata": raw_results["metadatas"][0][i],
                "semantic_distance": round(raw_results["distances"][0][i], 4)
            })



        return {
            "user_query": data.query_text,
            "total_matches": len(formatted_results),
            "top_match": formatted_results[0]
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Vector Query Exception: {str(e)}"
        )
