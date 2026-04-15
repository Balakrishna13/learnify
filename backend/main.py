from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from processor import process_input
import os
import psycopg2
from processor import DB_CONFIG # Importing my DB credentials

app = FastAPI(
    title="Learnify API",
    description="Smart Learning Assistant Backend",
    version="1.0"
)

# Enable CORS
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


@app.get("/history")
def get_history():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        # Fetch last 10 records from the history table we created
        cur.execute("SELECT mode, input_text, created_at FROM history ORDER BY created_at DESC LIMIT 10")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        # Format for JS: Convert timestamp to a nice string
        return [
            {
                "mode": r[0], 
                "input": r[1], 
                "time": r[2].strftime("%I:%M %p")
            } for r in rows
        ]
    except Exception as e:
        print(f"Database Error: {e}")
        return []