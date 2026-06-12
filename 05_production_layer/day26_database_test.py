# database_test.py
import redis
import time

# 1. Connect to the local Redis server instance running on your machine
# (By default, Redis communicates over network port 6379)
try:
    r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
    
    print("🗄️ Connected to Redis State Storage Engine!")

   # WRITING DATA 

    dummy_coordinate = "0.715,0.233,-0.012"
    print(f"✍️ Writing current stream state to database... Key: 'index_finger_pos'")
    
    # .set() stores the value inside your system RAM instantly
    r.set("index_finger_pos", dummy_coordinate)

   
    # READING DATA (Simulating another program retrieving it)
  
    # Imagine your C# or game engine wants to know where the hand is right now:
    time.sleep(0.5) # Simulate a brief time delay
    
    # .get() fetches the current state instantly from memory
    retrieved_state = r.get("index_finger_pos")
    print(f"📥 Retrieved state from memory database: {retrieved_state}")

except redis.exceptions.ConnectionError:
    print("⚠️ REDIS SERVER NOT RUNNING YET!")
    print("👉 To run this completely, your computer needs the Redis background server running.")
    print("👉 But look closely at the code syntax—it looks just like a Python dictionary!")