import os
import yaml
import json
from fastapi import FastAPI
import uvicorn

# Load settings (with fallback)
try:
    with open("config/settings.yaml", "r") as f:
        settings = yaml.safe_load(f)
except FileNotFoundError:
    settings = {"debug": True, "log_level": "INFO"}

# Load API keys (with fallback)
try:
    with open("config/api_keys.json", "r") as f:
        api_keys = json.load(f)
except FileNotFoundError:
    api_keys = {"status": "Please configure API keys"}

app = FastAPI(title="Sentra AI", description="Autonomous Cyber Threat Hunting Platform", version="1.0.0")

@app.get("/")
def home():
    return {"status": "running", "message": "Welcome to Sentra AI 🚀"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
