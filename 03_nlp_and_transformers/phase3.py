import os
import numpy as np
from transformers import pipeline

# Suppress system warning notifications
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# --- SYSTEM TRAINING DATA ---
system_corpus = "Transformers leverage self-attention mechanisms to map text context in parallel."

# ============================================
# 📝 LANE A: LOW-LEVEL VOCABULARY METRICS
# ============================================
print("📝 Executing Lane A: Low-Level Vocabulary Extraction...")

def build_custom_vocabulary(text):
    """
    Normalizes text data, strips periods, lowercases, 
    and constructs a unique vocabulary index tracker.
    """
    cleaned = text.lower().replace(".", "")
    tokens = cleaned.split()
    # TODO: Step 1 - Extract unique tokens, sort alphabetically, and append "<UNK>"
    unique_tokens = sorted(list(set(tokens))) + ["<UNK>"]
    
    # TODO: Step 2 - Build a dictionary mapping tokens to integer indices
    word_to_id = {token: idx for idx, token in enumerate(unique_tokens)}
    return word_to_id

token_map = build_custom_vocabulary(system_corpus)
print(f"   -> Custom Corporate Vocabulary Size: {len(token_map)} unique tokens.")

# ============================================
# 🔥 LANE B: PRODUCTION HF GENERATION HARNESS
# ============================================
print("\n🤖 Executing Lane B: Hugging Face Production Inference...")

# TODO: Step 3 - Initialize the 'text-generation' pipeline using 'openai-community/gpt2'
hf_generator = pipeline("text-generation",model="openai-community/gpt2")

prompt = "Transformers are capable of"

# TODO: Step 4 - Fire the prompt into hf_generator.
# Set max_new_tokens=15, temperature=0.5, and do_sample=True.
generation_outputs = hf_generator(prompt,
                                max_new_tokens=15,
                                temperature=0.5,
                                do_sample=True
                                )
    

raw_generated_text = generation_outputs[0]["generated_text"]
print(f"   -> Generated Output Text:\n      '{raw_generated_text}'")

# ============================================
# 📊 CONVERGENCE AUDIT METRICS
# ============================================
print("\n📊 Running System Verification Audit...")

# Split the generated text into normalized tracking words
audit_tokens = raw_generated_text.lower().replace(".", "").split()

# Translate the text into our custom integer ID space to check alignment
encoded_audit_ids = [token_map.get(word, token_map["<UNK>"]) for word in audit_tokens]
print(f"   -> Text mapped to Custom Vocabulary Space IDs: {encoded_audit_ids}")

# Count how many words fell into the Out-of-Vocabulary (<UNK>) category
unknown_token_index = token_map["<UNK>"]
number_of_unks = encoded_audit_ids.count(unknown_token_index)
print(f"   -> Out-of-Vocabulary (<UNK>) tokens detected: {number_of_unks}")

# Graduation validation protections
assert len(token_map) == 10, "Custom vocabulary mapping dimensions are miscalculated."
assert len(encoded_audit_ids) >= len(prompt.split()), "The production pipeline failed to return the payload sequence."
print("\n🎉 Phase 3 Graduation Complete! You have successfully orchestrated low-level data structures alongside LLM frameworks.")