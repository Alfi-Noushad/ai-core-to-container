#The Multi-Threaded Lazy Aggregator
import polars as pl
import os

def run_lazy_analytics_pipeline(csv_path):
    """
    Constructs a Polars LazyFrame computation graph to transform, 
    filter, and aggregate log data concurrently.
    """
    # TODO: Step 1 - Initialize a Polars LazyFrame scanning the target file path
    lazy_query = pl.scan_csv(csv_path)

    # TODO: Step 2 - Chain a filtering method to keep only rows where 
    # the "confidence_score" column is strictly greater than 0.70.
    # Hint: Use `.filter(pl.col("column_name") > value)`
    lazy_query = lazy_query.filter(pl.col("confidence_score") > 0.70) # Fix this line

    # TODO: Step 3 - Group by the "category" column and calculate the count of rows.
    # Hint: Chain `.group_by("column").agg(pl.len().alias("total_records"))`
    lazy_query = lazy_query.group_by("category").agg(pl.len().alias("total_records")) # Fix this line

    # TODO: Step 4 - Finalize the execution. Collect the results into a standard DataFrame.
    # Hint: Chain `.collect()` at the very end of your expression pool.
    return lazy_query.collect()

# --- TEST ENVIRONMENT ---
if __name__ == "__main__":
    print("🧊 Constructing Lazy Data Testing Pipeline...")
    mock_file = "mock_analytics_logs.csv"
    
    # Write sample logs locally
    with open(mock_file, "w") as f:
        f.write("category,confidence_score,value\n")
        f.write("AGENT_A,0.92,105\n")
        f.write("AGENT_B,0.45,200\n")  # Should be filtered out
        f.write("AGENT_A,0.88,410\n")
        f.write("AGENT_C,0.12,90\n")   # Should be filtered out
        f.write("AGENT_B,0.75,320\n")
        f.write("AGENT_A,0.95,150\n")
        
    try:
        # Run the Polars compilation graph
        final_dataframe = run_lazy_analytics_pipeline(mock_file)
        
        print("\n📈 Polars Optimization Pipeline Complete!")
        print("👀 Aggregate Execution Output Matrix:")
        print(final_dataframe)
        
        # Verify correctness via explicit category assertions
        # We look up values from our generated DataFrame structure
        agent_a_count = final_dataframe.filter(pl.col("category") == "AGENT_A").select("total_records").item()
        agent_b_count = final_dataframe.filter(pl.col("category") == "AGENT_B").select("total_records").item()
        
        assert agent_a_count == 3
        assert agent_b_count == 1
        print("\n🎉 Polars Lazy-Engine verified! Analytics accurately compiled without memory overhead.")
        
    finally:
        if os.path.exists(mock_file):
            os.remove(mock_file)