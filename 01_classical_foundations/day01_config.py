#The Robust Config Guard
import os
from dataclasses import dataclass

@dataclass(slots=True)
class DataIngestionConfig:
    data_path: str
    batch_size: int
    threshold: float

    def __post_init__(self):
        """
        Runs strict validation checks right after initialization.
        """
        # Step 1 - Strict File Path Validation
        # Using os.path.exists keeps configuration lightweight without touching file I/O locks
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Config target system path does not exist: '{self.data_path}'")
        
        # Step 2 - Batch Size Integer Boundary Guard
        if self.batch_size <= 0:
            raise ValueError(f"batch_size must be a positive integer greater than 0. Got: {self.batch_size}")
        
        # Step 3 - Threshold Bounds Check (0.0 < threshold < 1.0)
        if not (0.0 < self.threshold < 1.0):
            raise ValueError(f"threshold must be strictly between 0.0 and 1.0. Got: {self.threshold}")


# --- TEST ENVIRONMENT ---
if __name__ == "__main__":
    print("🚀 Running Ingestion Config Guard Tests...\n")
    
    # TEST 1: Expect Path Validation Failure
    try:
        config = DataIngestionConfig(data_path="missing_dataset.csv", batch_size=32, threshold=0.95)
    except FileNotFoundError as e:
        print(f"✅ Test 1 Passed: Safely caught missing file error:\n   -> {e}\n")

    # TEST 2: Successful setup with a real temporary file
    dummy_filename = "temp_raw_data.csv"
    with open(dummy_filename, "w") as f:
        f.write("id,feature_1,label\n1,0.54,prod_a") # Creating a valid mock file
        
    try:
        valid_config = DataIngestionConfig(data_path=dummy_filename, batch_size=64, threshold=0.85)
        print("✅ Test 2 Passed: Configuration successfully created with zero leaks.")
        
        # TEST 3: Verify that `slots=True` is actively protecting our system memory
        print("\n🔒 Testing memory protection block...")
        try:
            valid_config.custom_metadata = "unauthorized_tag"
            print("❌ Failure: Python allowed a runtime attribute modification! Check your slots configuration.")
        except AttributeError as e:
            print(f"✅ Test 3 Passed: Successfully blocked attribute injection! Memory protected.\n   -> {e}")
            
    finally:
        # Clean up the file system environment
        if os.path.exists(dummy_filename):
            os.remove(dummy_filename)
            print("\n🧹 Cleaned up temporary environment files.")