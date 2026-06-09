#The Ingestion API Endpoint Gateway
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="AI Engineering Gateway Pipeline")

# TODO: Step 1 - Complete the Pydantic structural data contract rule validations
class ConfigPayload(BaseModel):
    # Validate that data_path is a string
    data_path: str
    
    # Validate that batch_size is an integer, and must be greater than 0
    # Hint: Use Field(gt=0) to enforce boundary constraints automatically
    batch_size: int = Field(gt=0)
    
    # TODO: Use Field(gt=0.0, lt=1.0) to validate that threshold is a float between 0.0 and 1.0
    threshold: float  = Field(gt=0.0, lt=1.0)

# TODO: Step 2 - Establish an asynchronous POST route mapped to the path URL "/verify-config"
# Hint: Use the decorator format: @app.post("/verify-config")
# Define the function as: async def validate_system_config(payload: ConfigPayload):
pass
@app.post("/verify-config")

async def validate_system_config(payload: ConfigPayload):

    # TODO: Step 3 - Return a success dictionary response showing that validation cleared
    # return {"status": "VALIDATED", "target_path": payload.data_path}
    return {"status": "VALIDATED", "target_path": payload.data_path}


# --- QUICK RUN INSTRUCTIONS ---
# Save the code block. Open your local machine terminal shell environment and execute:
# uvicorn day09_backend:app --reload
#
# Navigate to http://127.0.0.1:8000/docs in your browser to test your API using the interactive Swagger UI!