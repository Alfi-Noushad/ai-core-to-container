#The Semantic Semantic Search Engine
import numpy as np

# A miniature database of 3-dimensional word embeddings 
# Dimensions could roughly capture properties like: [Is-Technology, Is-Living, Is-Liquid]
embedding_vault = {
    "processor": np.array([0.98, 0.01, -0.05]),
    "dolphin":   np.array([0.02, 0.99, 0.45]),
    "coffee":    np.array([0.15, 0.10, 0.92]),
    "software":  np.array([0.85, 0.05, -0.10])
}

# --- THE COGNITIVE SEARCH ENGINE ---

def calculate_cosine_similarity(vec_a, vec_b):
    """
    Computes the cosine similarity between two numeric vectors.
    """
    # TODO: Step 1 - Calculate the dot product of vec_a and vec_b using np.dot()
    dot_prod = np.dot(vec_a,vec_b)
    
    # TODO: Step 2 - Calculate the L2 norm (magnitude) of each vector using np.linalg.norm()
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    
    # Prevent divide-by-zero anomalies in production systems
    if norm_a == 0 or norm_b == 0:
        return 0.0
        
    # TODO: Step 3 - Return the dot product divided by the product of the norms
    return dot_prod/(norm_a*norm_b)

def find_most_similar_word(query_vector, database):
    """
    Scans the database dictionary to find the token with the highest semantic match score.
    """
    best_word = None
    highest_score = -1.0
    
    for word, vector in database.items():
        score = calculate_cosine_similarity(query_vector, vector)
        if score > highest_score:
            highest_score = score
            best_word = word
            
    return best_word, highest_score

# --- PIPELINE RUNNER ---
if __name__ == "__main__":
    print("🔍 Activating Semantic Vector Database...")
    
    # Imagine a user searches for something related to coding, yielding this query vector:
    search_query_vector = np.array([0.91, 0.02, -0.02]) 
    
    # Run the similarity search loop
    matched_token, final_similarity = find_most_similar_word(search_query_vector, embedding_vault)
    
    print(f"\n📥 Ingested Search Query Vector: {search_query_vector}")
    print(f"📤 Nearest Semantic Entry Found: '{matched_token}' (Similarity Match: {final_similarity:.4f})")
    
    # Individual cosine verification checks
    test_sim = calculate_cosine_similarity(np.array([1, 0]), np.array([1, 0]))
    assert abs(test_sim - 1.0) < 1e-5, "Identical vectors must yield a cosine similarity of exactly 1.0!"
    assert matched_token == "processor", "Search engine accuracy failure! The closest word should be 'processor'."
    print("\n🎉 Success! Your semantic search loop accurately calculates high-dimensional token similarity.")