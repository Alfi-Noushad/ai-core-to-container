#The CPU Bound Benchmark
import time
import math
from concurrent.futures import ProcessPoolExecutor

def heavy_cpu_task(number):
    """
    A highly intensive math function simulating heavy data transformation.
    """
    count = 0
    # Loop millions of times doing complex trigonometry computations
    for i in range(1, 5_000_000):
        count += math.sin(i) * math.cos(i)
    return f"Task {number} Completed"

def run_sequentially(tasks):
    print("🐢 Running tasks sequentially on a single core...")
    start = time.time()
    results = []
    for t in tasks:
        results.append(heavy_cpu_task(t))
    print(f"   Finished in {time.time() - start:.2f} seconds.")

def run_with_multiprocessing(tasks):
    print("\n⚡ Running tasks across multiple CPU cores in parallel...")
    start = time.time()
    
    # TODO: Step 1 - Use ProcessPoolExecutor in a 'with' statement.
    with ProcessPoolExecutor() as executor:
    # TODO: Step 2 - Use executor.map() to map the `heavy_cpu_task` function over our `tasks` list.
    # Convert the results into a list and store them in a variable called `results`.
     results =  executor.map(heavy_cpu_task, tasks)
     list(results) 
    results = []
    
    print(f"   Finished in {time.time() - start:.2f} seconds.")

if __name__ == "__main__":
    # 4 heavy loads representing processing a batch of 4 large chunks
    task_list = [1, 2, 3, 4]
    
    # Run 1: Single core execution
    run_sequentially(task_list)
    
    # Run 2: Multi-core parallel execution
    run_with_multiprocessing(task_list)