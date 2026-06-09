#Concurrent API Batch Processing
import asyncio
import time
import random

async def call_mock_ai_service(item_id: int, text_data: str):
    """
    Simulates sending data to an external AI/Embedding API.
    """
    # Simulate an unpredictable network delay between 0.5 and 1.5 seconds
    delay = random.uniform(0.5, 1.5)
    await asyncio.sleep(delay)
    
    # Simulate a successful JSON API response
    return {"id": item_id, "status": "COMPLETED", "embedding_size": 1536}

async def main():
    # A small batch of dirty strings to enrich
    raw_batch = ["user_query_1", "user_query_2", "user_query_3", "user_query_4", "user_query_5"]
    
    start_time = time.time()
    print("🚀 Starting High-Concurrency Enrichment Engine...")

    # TODO: Step 1 - Build a list of asynchronous tasks.
    # Loop over `raw_batch` using enumerate(raw_batch, start=1) to get an ID and the text string.
    # For each item, invoke `call_mock_ai_service(idx, text)` and append that coroutine object to a list named `tasks`.
    tasks = []
    for idx, text in enumerate(raw_batch, start=1):
        task = call_mock_ai_service(idx, text)
        tasks.append(task)
    
    # TODO: Step 2 - Await the completion of all tasks concurrently.
    # Use `await asyncio.gather(*tasks)` to kick off all the requests simultaneously 
    # and store the responses in a variable called `results`.
    results = []
    results = await asyncio.gather(*tasks)

    print(f"\n✨ Successfully processed {len(results)} items!")
    for res in results:
        print(f"   -> {res}")

    total_time = time.time() - start_time
    print(f"\n⏱️ Total Execution Time: {total_time:.2f} seconds.")
    print("💡 If async worked correctly, total time should be ~1.5s instead of ~5.0s!")

if __name__ == "__main__":
    asyncio.run(main())