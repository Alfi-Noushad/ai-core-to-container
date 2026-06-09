import asyncio
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dataclasses import dataclass

app = FastAPI(title="Phase 1 Graduation AI Engine")

# === CORE ARCHITECTURE COMPONENTS ===

# MODULE 1: Memory-Optimized State (Day 1 - Dataclasses & Slots)
@dataclass(slots=True)
class VerifiedVectorPayload:
    vector_id: int
    data_array: np.ndarray  # Storing native numpy array instances

# MODULE 2: Strict Data Validation Interface (Day 9 - FastAPI/Pydantic)
class VectorInputSchema(BaseModel):
    vector_id: int
    raw_values: list[float] = Field(min_items=3, max_items=3, description="Must be an embedding vector of exactly dimension 3.")

# === CORE PROCESSING PIPELINE ===

# MODULE 3: Asynchronous Enrichment Core (Day 3 & Day 4 - Asyncio & NumPy)
async def process_single_vector_async(payload: VectorInputSchema) -> VerifiedVectorPayload:
    """
    Simulates asynchronous data cleaning and converts raw input data lists 
    into memory-optimized, native NumPy vector representations.
    """
    # Simulate a tiny non-blocking processing latency (Day 3)
    await asyncio.sleep(0.05)
    
    # Convert list to an active NumPy vector array (Day 4)
    np_vector = np.array(payload.raw_values)
    
    # Return packaged within our slot-protected data holder class (Day 1)
    return VerifiedVectorPayload(vector_id=payload.vector_id, data_array=np_vector)

# === WEB CONTAINER LAYER ===

@app.post("/process-embeddings")
async def process_embeddings_endpoint(input_batch: list[VectorInputSchema]):
    """
    The main enterprise entry point gateway. Takes batches of input strings,
    schedules them across an active async task pool, and computes analytical data.
    """
    if not input_batch:
        raise HTTPException(status_code=400, detail="Data ingestion batch cannot be empty.")
    
    # TODO: Step 1 - Build your concurrent execution task pool (Day 3)
    # Loop over every payload item in `input_batch` and call process_single_vector_async(payload).
    # Gather all tasks concurrently using await asyncio.gather(*tasks) into a list called 'verified_batch'.
    tasks = []
    for payload in input_batch:
        tasks.append(process_single_vector_async(payload))
    # Placeholder to make code syntactically valid until you fill it out:
    verified_batch = await asyncio.gather(*tasks)

    # TODO: Step 2 - Matrix Assembly & Math Analytics (Day 4 - NumPy)
    # Extract the internal `.data_array` from every element inside your 'verified_batch' list.
    # Stack them vertically into a single 2D NumPy array matrix using `np.vstack([item.data_array for item in verified_batch])`.
    # Calculate the global mean of the entire resulting matrix using `.mean()`.
    matrix_mean = 0.0
    matrix = np.vstack([item.data_array for item in verified_batch])
    matrix_mean = matrix.mean()

    # Step 3 - Structural JSON Response (Day 9)
    return {
        "status": "SUCCESS_GRADUATED",
        "processed_records_count": len(verified_batch),
        "global_matrix_mean": float(matrix_mean)
    }

# --- RUNNING & VERIFYING YOUR SYSTEM ---
# 1. Start the microserver engine in your local terminal window:
#    uvicorn phase1_graduation:app --reload
#
# 2. Open http://127.0.0.1:8000/docs in your browser.
# 3. Hit the POST /process-embeddings route, choose 'Try it out', and pass this valid JSON array input block:
# [
#   {"vector_id": 1, "raw_values": [0.1, 0.2, 0.3]},
#   {"vector_id": 2, "raw_values": [0.4, 0.5, 0.6]}
# ]
#
# 4. Hit Execute. If your math and async pools match correctly, you will receive a global matrix mean of 0.35!