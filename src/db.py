from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

# Load config
with open("config/settings.yaml", "r") as f:
    settings = yaml.safe_load(f)

DATABASE_URL = settings["database"]["url"]

# Create engine & session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()