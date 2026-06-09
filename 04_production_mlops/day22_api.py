import uvicorn
from fastapi import FastAPI

# --- MODEL APP CORE INITIALIZATION ---
app = FastAPI(
    title="Enterprise Token Inference Server",
    description="Production API microservice layer for processing real-time system metrics.",
    version="1.0.0"
)

# Simulated trained model function tracking corporate resource consumption costs
# Cost Formula: Base connection rate ($1.50) + ($0.05 * thousand tokens processed)
def production_inference_model(tokens_k):
    return 1.50 + (tokens_k * 0.05)

# --- HOME ENTRY ROUTE (HEALTH CHECK) ---
@app.get("/")
async def health_check():
    """
    Standard automated orchestrator route to confirm the container node is fully healthy.
    """
    return {"status": "ONLINE", "hardware_check": "HEALTHY"}

# --- MODEL INFERENCE ROUTE ---
# TODO: Step 1 - Bind this function to an HTTP POST route matching the path "/predict"
# Hint: Use the @app.post("/predict") decorator syntax
@app.post("/predict")
async def predict_token_cost(payload: dict):
    """
    Extracts high-volume usage features and scores real-time financial projections.
    """
    # TODO: Step 2 - Extract the key "tokens_consumed_k" from the payload dictionary.
    # Fallback to a default float value of 0.0 if the key is missing from the query.
    raw_tokens = payload["tokens_consumed_k"]
    
    # TODO: Step 3 - Stream the extracted numerical value through the production_inference_model function.
    model_score = production_inference_model(raw_tokens)
    
    # TODO: Step 4 - Return a JSON response container mapping the score.
    # Format: {"input_tokens_k": raw_tokens, "calculated_cost": model_score}
    return {"input_tokens_k": raw_tokens, "calculated_cost": model_score} 

# --- DEVELOPMENT RUNNER ENTRYPOINT ---
if __name__ == "__main__":
    print("🚀 Spawning local Uvicorn ASGI instance on http://127.0.0.1:8000")
    print("📝 Tip: You can visit http://127.0.0.1:8000/docs once live to view automated interactive Swagger documentation API maps!")
    
    # Fire up the local network listener loop hosting our app configuration
    uvicorn.run(app, host="127.0.0.1", port=8000)