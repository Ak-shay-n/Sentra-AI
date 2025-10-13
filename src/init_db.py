from src.db import engine
from src.models.threat import Base

print("📦 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Done!")
