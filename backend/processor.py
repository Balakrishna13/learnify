import os
import psycopg2
from handlers.code_handler import explain_code
from handlers.notes_handler import summarize_notes
from handlers.topic_handler import explain_topic
from dotenv import load_dotenv

load_dotenv()

# Database connection configuration
DB_CONFIG = {
    "dbname": "learnify",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "host": "localhost",
    "port": "5432"
}

def save_to_db(mode, text):
    """Saves the user request to the PostgreSQL history table"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO history (mode, input_text) VALUES (%s, %s)",
            (mode, text)
        )
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ Data saved to PostgreSQL successfully!")
    except Exception as e:
        print(f"❌ Database Error: {e}")

def process_input(mode, text):
    # This line triggers the actual database save
    save_to_db(mode, text)

    if mode == "code":
        return explain_code(text)
    elif mode == "notes":
        return summarize_notes(text)
    elif mode == "topic":
        return explain_topic(text)
    else:
        return {"error": "Invalid mode"}