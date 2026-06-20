import time
import random
from fastapi import FastAPI, Request, status
from pydantic import BaseModel

app = FastAPI(title="Production Telemetry Sandbox")

# Global variables to simulate our live database tracking dashboard metrics
TOTAL_REQUESTS_PROCESSED = 0
TOTAL_LATENCY_ACCUMULATED = 0.0

class SimulationPayload(BaseModel):
    input_data: str

# ------------------------------------------------------------------------------
# THE TELEMETRY INFERENCE ROUTE
# ------------------------------------------------------------------------------
@app.post("/predict", status_code=status.HTTP_200_OK)
async def predict_and_monitor(payload: SimulationPayload):
    global TOTAL_REQUESTS_PROCESSED, TOTAL_LATENCY_ACCUMULATED
    
    # 1. START THE PERFORMANCE TIMER
    start_time = time.perf_counter()
    
    # 2. SIMULATE MODEL COMPUTE TIME (Varying processing delays)
    # This mimics a machine learning model processing an image or text sequence
    simulated_model_delay = random.uniform(0.02, 0.18) 
    time.sleep(simulated_model_delay)
    
    # Fake inference classification verdict
    mock_verdict = "MALICIOUS" if len(payload.input_data) % 2 == 0 else "SAFE"
    
    # 3. STOP THE PERFORMANCE TIMER
    end_time = time.perf_counter()
    execution_latency_ms = (end_time - start_time) * 1000 # Convert seconds to ms
    
    # Update our global live telemetry counters
    TOTAL_REQUESTS_PROCESSED += 1
    TOTAL_LATENCY_ACCUMULATED += execution_latency_ms
    
    # 4. RETURN Payload along with real-time telemetry headers
    return {
        "prediction_result": mock_verdict,
        "telemetry": {
            "inference_latency_ms": round(execution_latency_ms, 2),
            "status": "HEALTHY" if execution_latency_ms < 150 else "LATENCY_SPIKE_WARNING"
        }
    }

# ------------------------------------------------------------------------------
# THE PROMETHEUS STYLE METRICS SCRAPE ENDPOINT
# ------------------------------------------------------------------------------
@app.get("/metrics")
def metrics_endpoint():
    # This is exactly how Prometheus scrapes data to draw Grafana graphs!
    global TOTAL_REQUESTS_PROCESSED, TOTAL_LATENCY_ACCUMULATED
    
    avg_latency = (TOTAL_LATENCY_ACCUMULATED / TOTAL_REQUESTS_PROCESSED) if TOTAL_REQUESTS_PROCESSED > 0 else 0.0
    
    return {
        "metric_target": "threat_filter_pipeline",
        "total_api_hits": TOTAL_REQUESTS_PROCESSED,
        "rolling_average_latency_ms": round(avg_latency, 2),
        "system_alert_status": "CRITICAL" if avg_latency > 120 else "OK"
    }