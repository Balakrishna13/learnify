from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from processor import process_input
import os

app = FastAPI(
    title="Learnify API",
    description="Smart Learning Assistant Backend",
    version="1.0"
)

# Enable CORS (like Flask CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def root():
    return {"message": "Learnify FastAPI Backend Running"}


# Main processing route
@app.post("/process")
async def process(data: dict):
    mode = data.get("mode")
    text = data.get("text")

    result = process_input(mode, text)

    return result