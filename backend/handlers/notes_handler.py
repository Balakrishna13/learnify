from ai_client import ask_ai

def summarize_notes(text):

    prompt = f"""
Summarize these notes:

{text}

Give:
- Summary
- Bullet points
"""

    response = ask_ai(prompt)

    return {
        "title": "AI Notes Summary",
        "summary": response
    }