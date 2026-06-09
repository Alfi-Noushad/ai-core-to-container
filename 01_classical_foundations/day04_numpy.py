import numpy as np

def calculate_cosine_similarity(vec_a, vec_b):
    """
    Calculates the cosine similarity score between two 1D numpy arrays.
    The result should be a single float between -1.0 and 1.0.
    """
    # TODO: Step 1 - Calculate the dot product of vec_a and vec_b using np.dot()
    dot_prod = np.dot(vec_a, vec_b)

    
    # TODO: Step 2 - Calculate the L2 norm (magnitude) of BOTH vectors.
    # Hint: Use the native NumPy linear algebra module: np.linalg.norm()
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    # Avoid crashing with a DivisionByZero error if a vector is completely empty
    if norm_a == 0 or norm_b == 0:
        return 0.0
        
    # TODO: Step 3 - Divide the dot product by the product of the two norms and return it
    return dot_prod / (norm_a * norm_b)

# --- TEST ENVIRONMENT ---
if __name__ == "__main__":
    print("🔎 Initializing Semantic Search Matcher...")

    # Mock user query embedding (e.g., "AI Engineering careers")
    query_vector = np.array([0.15, 0.88, 0.05, 0.43])
    
    # Mock database record embedding A (e.g., "How to become a machine learning developer")
    doc_vector_A = np.array([0.12, 0.85, 0.07, 0.40])
    
    # Mock database record embedding B (e.g., "Baking a chocolate chip cookie recipe")
    doc_vector_B = np.array([0.71, 0.11, 0.68, 0.02])

    # Calculate matches
    similarity_A = calculate_cosine_similarity(query_vector, doc_vector_A)
    similarity_B = calculate_cosine_similarity(query_vector, doc_vector_B)

    print(f"\n📈 Similarity Score with Doc A (Relevant): {similarity_A:.4f}")
    print(f"📉 Similarity Score with Doc B (Irrelevant): {similarity_B:.4f}")
    
    # Assertion check to verify your math execution
    if similarity_A > similarity_B:
        print("\n✅ System Success: The search engine accurately ranked the relevant document higher!")
    else:
        print("\n❌ Math Error: Check your formula division steps.")