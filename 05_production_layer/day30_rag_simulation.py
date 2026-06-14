# RAG simulation
import chromadb
from chromadb.utils import embedding_functions  
from sklearn.metrics.pairwise import cosine_similarity

#Now your vectors are stored on disk. with persistance..
chroma_client = chromadb.PersistentClient(path="./chroma_storage")

# Configure ChromaDB to automatically use the exact same embedding model
# This ensures incoming queries are mapped to the same 384-dimensional space

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

#create the db model
collection = chroma_client.get_or_create_collection(
    name="my_docs",
    embedding_function=sentence_transformer_ef
)

#Add documents
collection.add(
    documents=[
        "Python is a programming language.",
        "ChromaDB is a vector database.",
        "Kerala is a state in India."
    ],
    #metadatas=[],        #we can add metadata 
    ids=["doc1", "doc2", "doc3"]
)

search_query = "what is python"
print(f"👤 User Question: '{search_query}'")

#find the most similar embedding
query_result = collection.query(
    query_texts= [search_query],
    n_results=1
)

#takes the doc from the db
retrieved_sol = query_result['documents'][0][0]

#Create the Master Prompt that grounds the AI
master_prompt = f"""
================================================================================
SYSTEM PROMPT TEMPLATE INJECTED BY BACKEND
================================================================================
Instructions: Answer the question using only the verified context below.

[CONTEXT DATA]: 
{retrieved_sol}

[USER QUESTION]: 
{search_query}
================================================================================
"""

print(master_prompt)


#generate simulation..
print("Simulated Generation output:")
print(f"-> {retrieved_sol}")