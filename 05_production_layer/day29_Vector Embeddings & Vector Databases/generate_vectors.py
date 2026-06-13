#pip install sentence-transformers
from sentence_transformers import SentenceTransformer   

# This downloads a lightweight, highly efficient 90MB model on the first run
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample sentences to vectorize
documents = [
    "A malicious cyberattack breached the database server.",
    "The chef prepared a fresh apple pie for dessert.",
    "Unauthorized intrusion detected on network switch 4."
]

#embedding transfer the words to vectors[dense vector (text string into a fixed-length array of floating-point numbers)]
embeddings = model.encode(documents)

#Let's inspect what the model created
for idx, text in enumerate(documents):

    vector = embeddings[idx]

    print("\n------------------------------------------------------------")
    print(f"📄 Text: '{text}'")
    print(f"📊 Vector Shape: {vector.shape} dimensions")

    # Print just the first 5 numbers of the vector to see what it looks like
    print(f"🔢 Sample Coordinates (First 5 values): {vector[:5]}")