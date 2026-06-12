#Redis = Short-Term Memory
import redis
from fastapi import FastAPI

#connect the redis with local machine..
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

#sets the app FastApi
app = FastAPI()

@app.post("/coordinates")
def coordinates(x: float, y: float):

    # enter's the latest coordinates to ram(redis container) (r.set())
    r.set(
        "latest_coordinates",
        f"{x},{y}"
    )

    return {"status": "saved"}


@app.post("/get_coordinates")
#eill get the value from the redis  (r.get())
def get_coordinates():

    coords = r.get("latest_coordinates")

    return {"coordinates": coords}


# can set an expiry time in it (60 sec)
r.set("latest_coordinates", "10,20", ex=60)

# can find teh ttl [time to live]
ttl = r.ttl("latest_coordinates")

""""

 save
cache.set("user:1", "active")

 read
cache.get("user:1")

 counter
cache.incr("user:1:hits")

auto delete
cache.expire("user:1:hits", 60)

"""