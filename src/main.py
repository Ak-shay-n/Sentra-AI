import os
import yaml
import json
from fastapi import FastAPI
import uvicorn

# Load settings
with open("config/settings.yaml", "r") as f:
    settings = yaml.safe_load(f)

# Load API keys
with open("config/api_keys.json", "r") as f:
    api_keys = json.load(f)

app = FastAPI(title="Sentra AI", description="Autonomous Cyber Threat Hunting Platform", version="1.0.0")

@app.get("/")
def home():
    return {"status": "running", "message": "Welcome to Sentra AI 🚀"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
