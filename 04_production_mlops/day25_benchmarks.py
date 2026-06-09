#The High-Volume Concurrency Stress Engine
import asyncio
import time
import numpy as np
import httpx

# Target endpoint to stress test (Ensure your Day 23 API server is running!)
TARGET_URL = "http://127.0.0.1:8000/evaluate-risk"
MOCK_PAYLOAD = {"credit_score": 750, "credit_utilization": 0.25}

async def hit_endpoint_and_measure(client):
    """
    Fires a single request to the API and measures exact round-trip duration.
    """
    start = time.perf_counter()
    try:
        response = await client.post(TARGET_URL, json=MOCK_PAYLOAD)
        status_code = response.status_code
    except Exception:
        status_code = 500
        
    end = time.perf_counter()
    # Return flight duration converted directly to milliseconds
    return (end - start) * 1000.0, status_code

async def run_stress_test(concurrency_count):
    print(f"⚡ Unleashing {concurrency_count} parallel requests against risk engine...")
    
    # Configure low-level socket limits to allow high concurrency
    limits = httpx.Limits(max_keepalive_connections=concurrency_count, max_connections=concurrency_count)
    
    async with httpx.AsyncClient(limits=limits, timeout=10.0) as client:
        # TODO: Step 1 - Generate a list containing 'concurrency_count' individual tasks 
        # calling the hit_endpoint_and_measure(client) routine.
        tasks = [hit_endpoint_and_measure(client) 
                 for _ in range(concurrency_count)]
        
        start_wall_time = time.perf_counter()
        # TODO: Step 2 - Await and gather all tasks concurrently using asyncio.gather
        results = await asyncio.gather(*tasks)
        end_wall_time = time.perf_counter()
        
    # Unpack durations and statuses
    durations = [r[0] for r in results]
    statuses = [r[1] for r in results]
    
    total_wall_time_seconds = end_wall_time - start_wall_time
    successful_requests = statuses.count(200)
    
    # ============================================
    # 📊 STATISTICAL METRIC CALCULATIONS
    # ============================================
    # TODO: Step 3 - Calculate system throughput (Total successful requests / total wall time seconds) 
    requests_per_second = successful_requests / total_wall_time_seconds if total_wall_time_seconds > 0 else 0.0
    
    # TODO: Step 4 - Compute the P50 (median) and P95 latency metrics from the durations list.
    # Hint: Use numpy's np.percentile(durations, percentile_value ) function layout.
    p50_latency = np.percentile(durations, 50)
    p95_latency = np.percentile(durations, 95)
    
    print("\n📊 Microservice Performance Profile Results:")
    print(f"   -> Total Concurrency Load:     {concurrency_count} requests")
    print(f"   -> Wall Clock Execution Time: {total_wall_time_seconds:.3f} seconds")
    print(f"   -> System Throughput Rate:    {requests_per_second:.1f} Requests/Sec (RPS)")
    print(f"   -> P50 (Median) Latency:      {p50_latency:.2f} ms")
    print(f"   -> P95 (Worst-Case) Latency:  {p95_latency:.2f} ms")
    print(f"   -> Request Success Rate:       {(successful_requests / concurrency_count) * 100000 / 1000:.1f}%")
    
    assert successful_requests > 0, "All stress test requests failed! Confirm your API server is running on port 8000."
    print("\n🎉 Success! Your benchmarking engine extracted precise performance profiles.")

if __name__ == "__main__":
    # Initialize the asynchronous network event loop with a load of 250 parallel requests
    asyncio.run(run_stress_test(concurrency_count=250))