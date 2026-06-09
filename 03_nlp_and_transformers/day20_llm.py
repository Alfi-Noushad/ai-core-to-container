#The Automated Text Ingestion & Generation Engine
import os
from transformers import pipeline

# Disable unnecessary warning logs in the console terminal output
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

def initialize_llm_generator():
    """
    Downloads and prepares an open-weight text generation pipeline.
    We are using 'gpt2' as a lightweight, fast, cross-platform checkpoint.
    """
    print("📥 Loading pre-trained Hugging Face transformer parameters...")
    # TODO: Step 1 - Initialize the text generation pipeline.
    # Pass 'text-generation' as the first positional task argument, 
    # and set model='openai-community/gpt2'.
    gen_pipeline = pipeline("text-generation",model="openai-community/gpt2")

    return gen_pipeline

def execute_model_inference(generator_pipeline, input_prompt):
    """
    Feeds a string prompt into the text generator and applies decoding constraints.
    """
    print(f"\n🧠 Processing Prompt: '{input_prompt}'")
    
    # TODO: Step 2 - Call your generator_pipeline instance passing your input_prompt string.
    # In addition to the prompt, configure these key-value arguments:
    # 1. Set max_new_tokens=20 (tells the model how many words to write)
    # 2. Set temperature=0.7 (adds a light touch of creative variation)
    # 3. Set do_sample=True (enables our custom sampling configurations)
    pipeline_outputs = generator_pipeline(input_prompt,
                                          max_new_tokens=20,
                                          temperature=0.7,
                                          do_sample=True
                                          )
    
    # TODO: Step 3 - Unpack the returned payload. 
    # The pipeline returns a list containing a single dictionary.
    # Extract the string mapped to the "generated_text" key.
    generated_string = pipeline_outputs[0]["generated_text"]
    
    return generated_string

# --- CORE RUNNER ---
if __name__ == "__main__":
    print("🚀 Initializing Production Language Model Interface...")
    
    # Boot up the pipeline engine
    text_generator = initialize_llm_generator()
    
    # Test generation with a technology prompt context
    prompt = "Artificial Intelligence will change software development by"
    
    # Run the model forward inference sequence
    completed_response = execute_model_inference(text_generator, prompt)
    
    print("\n✨ Model Response Output:")
    print(f"========================================\n{completed_response}\n========================================")
    
    # Verify the text was generated and contains our original prompt context
    assert len(completed_response) > len(prompt), "The model failed to generate new tokens!"
    assert prompt in completed_response, "The model lost or overwrote the baseline input prompt structure."
    print("\n🎉 Success! Your Hugging Face generation harness is running and executing inference.")
    