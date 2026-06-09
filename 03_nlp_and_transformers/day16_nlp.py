#The Raw Ingestion Tokenizer Engine
import numpy as np

# A sample text corpus representing log prompts sent to an assistant agent
training_corpus = "AI is altering the technology landscape. The technology landscape is changing fast!"

# --- THE NATURAL LANGUAGE PROCESSING ENGINE ---

def build_vocabulary_pipeline(text_data):
    """
    Cleans raw text data by removing punctuation, lowercasing, 
    and mapping tokens to discrete integer tracking arrays.
    """
    # Pre-processing: Clean punctuation and lowercase everything
    for punctuation in [".", "!", ",", "?"]:
        text_data = text_data.replace(punctuation, "")
    cleaned_text = text_data.lower()
    
    # Split text into single word tokens
    all_tokens = cleaned_text.split()
    
    # TODO: Step 1 - Extract all unique tokens, sort them alphabetically,
    # and append a special "<UNK>" string token at the very end of the list.
    unique_tokens = sorted(list(set(all_tokens))) + ["<UNK>"]
    
    # TODO: Step 2 - Create the 'word_to_id' dictionary mapping tokens to integer indices.
    # Hint: Use a dictionary comprehension over enumerate(unique_tokens)
    word_to_id = {tokens: idx for idx ,tokens in enumerate(unique_tokens)}
    
    return unique_tokens, word_to_id

def encode_sentence_to_ids(sentence, lookup_dict):
    """
    Transforms a new string sentence into a sequence list of integer IDs.
    """
    # Lowercase and split the new incoming sentence string
    tokens = sentence.lower().replace(".", "").split()
    
    encoded_sequence = []
    
    # TODO: Step 3 - Loop over each word token inside the 'tokens' list.
    # Look up its integer ID inside 'lookup_dict'. 
    # CRITICAL: If the word does not exist in the dictionary, fall back to lookup_dict["<UNK>"].
    # Append the resulting integer ID to the 'encoded_sequence' list.
    for token in tokens:
        encoded_sequence.append(lookup_dict.get(token, lookup_dict["<UNK>"]))
    return encoded_sequence

# --- RUNNING & EVALUATING YOUR TOKENS ---
if __name__ == "__main__":
    print("📝 Booting Low-Level NLP String Tokenizer...")
    
    # Step 1 & 2: Construct the vocabulary maps
    vocab_list, token_lookup_map = build_vocabulary_pipeline(training_corpus)
    
    print(f"\n📚 Total Vocabulary Size Created: {len(vocab_list)} words")
    print("📋 Vocabulary Lookup Map Indices:")
    for token, idx in token_lookup_map.items():
        print(f"   -> {token}: {idx}")
        
    # Test sentence containing an out-of-vocabulary word ("awesome")
    test_prompt = "AI technology is awesome."
    
    # Step 3: Run the translation pipeline
    integer_sequence = encode_sentence_to_ids(test_prompt, token_lookup_map)
    
    print(f"\n📥 Input Validation Prompt: '{test_prompt}'")
    print(f"📤 Resulting Encoded Integer ID Sequence: {integer_sequence}")

    # Integrity assertions to verify indexing rules are perfectly met
    assert len(vocab_list) == 9, "Vocabulary size mismatch. Ensure you handled duplicates and added '<UNK>'."
    assert integer_sequence[0] == token_lookup_map["ai"], "First element should match the index of 'ai'."
    assert integer_sequence[-1] == token_lookup_map["<UNK>"], "The word 'awesome' was unseen; it must map to '<UNK>'."
    print("\n🎉 Success! Your text tokenization pipeline accurately maps strings into categorical indices.")