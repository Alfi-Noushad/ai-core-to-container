#Security Validation Layer
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Ironclad Financial Risk Engine")

# Simulated ML Weight Coefficients Matrix
def predict_default_risk(score: int, utilization: float) -> float:
    # Risk calculation: Base risk modified by utilization ratio and credit rating bounds
    return min(1.0, max(0.0, (utilization * 1.5) - (score / 850.0)))

# TODO: Step 1 - Define the strict Pydantic parsing blueprint class.
# Inherit directly from Pydantic's BaseModel.
# Declare two fields:
# - credit_score: Must be an integer type (int)
# - credit_utilization_ratio: Must be a floating-point type (float)
class CreditAssessmentRequest(BaseModel): 
    credit_score: int
    credit_utilization: float

# --- SAFE PRODUCTION INFERENCE ROUTE ---
# TODO: Step 2 - Bind this function to an HTTP POST route matching the path "/evaluate-risk"

@app.post("/evaluate-risk")
async def calculate_credit_risk(data: CreditAssessmentRequest): # TODO: Step 3 - Add 'CreditAssessmentRequest' as the data type hint for payload
    """
    Ingests financial attributes, runs schema type compliance validation checks,
    and forwards clean structured types to the downstream calculation graph.
    """
    # TODO: Step 4 - Extract your variables from the 'payload' object using object dot notation.
    # Note: Because payload is a Pydantic object, you do NOT use dict lookups like payload["key"].
    # Extract 'credit_score' and 'credit_utilization_ratio' into their respective variables.
    raw_score =data.credit_score
    raw_utilization = data.credit_utilization
    
    # Run the sanitized variables through our model math loop
    calculated_risk = predict_default_risk(raw_score, raw_utilization)
    
    return {
        "validation_check": "PASSED",
        "assessed_default_probability": round(calculated_risk, 4)
    }

if __name__ == "__main__":
    print("🚀 Spawning Type-Safe Validation Service on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)