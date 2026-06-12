from fastapi import FastAPI, Depends
from pydantic import BaseModel

import redis

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session
)
#POSTGRES..----------------------------
#DATABASE SETUP
POSTGRES_URL = "postgresql://admin_user:super_secret_password@localhost:5432/sandbox_memory"
engine = create_engine(POSTGRES_URL)
#creates a factory for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Postgres structural table
class SecurityLog(Base):
    __tablename__ = "security_logs"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String)
    verdict = Column(String)

#Create the table on startup
Base.metadata.create_all(bind=engine)

#REDIS..--------------------------------
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

#dependency injection [ creates the db session when req and closes]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_cache():
    return redis_client

#pydantic
class AnalyzeRequest(BaseModel):
    ip_address: str


#fastApi
app = FastAPI()
@app.post("/analyze")
def analyze(
    data: AnalyzeRequest,
    db: Session = Depends(get_db), #Before calling this endpoint, execute this function and provide its result as an argument
    cache = Depends(get_cache)  #or cache: redis.Redis = Depends(get_cache)
):
    
    key = f"ip:{data.ip_address}"

    count = cache.incr(key)

    if count == 1:
        cache.expire(key, 10)

    if count > 3:
        verdict = "BLOCK"
    else:
        verdict = "SAFE"
    
    #add value to the row in db
    log = SecurityLog(
        ip_address=data.ip_address,
        verdict=verdict
    )

    #add it and commit to db
    db.add(log)
    db.commit()

    #returns the json to client in endpoint
    return {
        "ip": data.ip_address,
        "count": count,
        "verdict": verdict
    }




