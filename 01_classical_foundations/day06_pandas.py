#Feature Normalization Engine
import pandas as pd
import numpy as np
import time

def clean_and_score_dataset(df):
    """
    Cleans and scores raw data using optimized Pandas vector methods.
    Modifies the dataframe in-place.
    """
    # TODO: Step 1 - Vectorized String Cleaning
    # Convert the 'raw_text' column completely to lowercase and strip whitespace.
    # Hint: Use the native string accessor `df['column'].str.lower().str.strip()`
    df['clean_text'] = df['raw_text'].str.lower().str.strip()

    # TODO: Step 2 - Vectorized Length Generation
    # Compute the character length of each entry in 'clean_text'.
    # Hint: Use the native string accessor `df['column'].str.len()`
    df['text_length'] = df['clean_text'].str.len()

    # TODO: Step 3 - Vectorized Conditional Labelling
    # Create an 'anomaly_flag' column. If 'text_length' is less than 15, 
    # flag it as 1 (True anomaly). Otherwise, label it 0 (False).
    # Hint: Use `np.where(condition, value_if_true, value_if_false)`
    df['anomaly_flag'] = np.where(df['text_length'] < 15, 1, 0)
    
    return df

# --- TEST ENVIRONMENT ---
if __name__ == "__main__":
    print("📊 Generating Mock Production Dataset (100,000 Rows)...")
    
    # Create a heavy mock dataset with messy inputs
    mock_data = {
        "raw_text": ["  CRITICAL USER QUERY VALUE  ", "short text", "  # REMOVE COMMENT LOGS  ", "valid descriptive text string"] * 25000
    }
    df = pd.DataFrame(mock_data)

    start_time = time.time()
    
    # Run our high-speed processing engine
    processed_df = clean_and_score_dataset(df)
    
    total_time = time.time() - start_time
    print(f"✅ Engineering Transformation Complete in {total_time:.4f} seconds!")
    
    # Print sample of the results to inspect integrity
    print("\n👀 Output Matrix Sample:")
    print(processed_df[['raw_text', 'clean_text', 'text_length', 'anomaly_flag']].head(4))
    
    # Assertions to ensure vector columns computed correctly
    assert processed_df['clean_text'].iloc[0] == "critical user query value"
    assert processed_df['anomaly_flag'].iloc[1] == 1
    assert processed_df['anomaly_flag'].iloc[3] == 0
    print("\n🎉 All production validations passed successfully!")
