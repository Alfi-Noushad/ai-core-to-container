import chromadb
from chromadb.utils import embedding_functions       
# ChromaDB can automatically create embeddings if configured with an embedding function

#Now your vectors are stored on disk. with persistance..
chroma_client = chromadb.PersistentClient(path="./chroma_storage")

# Configure ChromaDB to automatically use the exact same embedding model
# This ensures incoming queries are mapped to the same 384-dimensional space

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

#create database
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

#searching
search_query = "What is ChromaDB?"

results = collection.query(
    query_texts=["What is ChromaDB?"],
    n_results=1
)

print(results)


print(f"ID: {results['ids'][0][0]}")
print(f"Document Text: {results['documents'][0][0]}")
# Distance score tells us how close the vectors are geometrically (Lower = Closer/More Similar)
print(f"Vector Distance Score: {results['distances'][0][0]:.4f}")



