# Writing to PostgreSQL (The Permanent Disk Storage Layer)
from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base  # to create a base class
from sqlalchemy.orm import sessionmaker     #!!!uses [ orm ] to perform every action in pyton itself.....
import datetime

#Create a Base class that our custom tables will inherit from
Base = declarative_base()

#Define the structural blueprint (Table) for our logs
class log(Base):
    __tablename__ = "details of log.."


    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)


#creates table if not there in the postgres
Base.metadata.create_all(bind=engine)

#opens a temporary communicaton channel
db_session = SessionLocal()

try: 

    #creates new row val to enter into the table    [his does NOT save anything yet to disk]
    mock_log_row = log(
    id = 1,
    ip_address="192.168.1.99",
    )

    # Stage the row and commit it permanently to the hard drive container
    db_session.add(mock_log_row)
    db_session.commit()

    #Read data back
    saved_records = db_session.query(log).all()

    #loop throught the saved_rec to get the items
    for row in saved_records:
        print(f"[{row.timestamp}] ID:{row.id} | IP:{row.ip_address}")

except Exception as e:
    #rollback if anything happens
    db_session.rollback()

finally:
    # Always close the session to free up system resources
    db_session.close()



   

