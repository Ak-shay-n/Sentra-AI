from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Threat(Base):
    __tablename__ = "threats"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String, index=True)
    threat_type = Column(String)
    severity = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)