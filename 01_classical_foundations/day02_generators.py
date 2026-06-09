#The Streaming Chunk Pipeline
import os
import sys

def data_streamer(file_path, chunk_size=3):
    """
    A generator that lazily reads a file, skips comment lines (starting with '#') 
    or empty lines, and yields chunks of clean data of size `chunk_size`.
    """
    chunk = []
    
    with open(file_path, 'r') as file:
        for line in file:
            clean_line = line.strip()
            
            # Skip empty lines or files paths that are commented out
            if not clean_line or clean_line.startswith('#'):
                continue
            
            # TODO: Step 1 - Append the clean_line to your chunk list.
            chunk.append(clean_line)
            # TODO: Step 2 - Check if your chunk list has reached the target `chunk_size`.
            # If it has, yield the chunk list and immediately clear the chunk list 
            # so it can reset for the next batch.
            if len(chunk) == chunk_size:
                yield chunk
                chunk.clear()  # Reset the chunk list for the next batch
            pass

        # TODO: Step 3 - After the loop finishes, don't forget the stragglers!
        # If there are any remaining items left inside the chunk list, yield them.
        if chunk:
            yield chunk


# --- TEST ENVIRONMENT ---
if __name__ == "__main__":
    mock_dataset = "mock_data_corpus.txt"
    
    # Let's write a quick mock file with comments and blanks
    with open(mock_dataset, "w") as f:
        f.write("# LLM Training Data Corpus\n\nline 1: text item\nline 2: text item\n")
        f.write("# A rogue comment here\nline 3: text item\nline 4: text item\n")
        f.write("line 5: text item\n\nline 6: text item\n")

    print("🚀 Initializing Streaming Engine...")
    
    # We call our generator here
    pipeline = data_streamer(mock_dataset, chunk_size=2)
    
    # Check the type—it won't execute until we loop over it!
    print(f"Pipeline Object Type: {type(pipeline)}") 
    
    print("\n📦 Streaming Chunks On-Demand:")
    for i, batch in enumerate(pipeline, 1):
        print(f"Batch {i} Ingested: {batch}")
        
    # Clean up file environment
    if os.path.exists(mock_dataset):
        os.remove(mock_dataset)