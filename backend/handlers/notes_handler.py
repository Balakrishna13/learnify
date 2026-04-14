from ai_client import ask_ai

def summarize_notes(notes):

    prompt = f"""
You are an expert at organizing and summarizing study notes.

Here are the raw notes:

{notes}

Process these notes and give:

Summary:
A clear, concise summary of the main idea in 3-5 sentences.

Key Points:
- Extract and list all the important points from the notes
- Organize them logically
- Fill in any gaps or incomplete points
- Make each point clear and complete

Important Terms:
Define any technical terms or concepts mentioned in the notes.

Quick Revision:
Write a short paragraph that captures everything important for quick revision before an exam.

Be thorough. If the notes are incomplete or unclear, fill in the gaps with accurate information.
"""

    response = ask_ai(prompt)

    return {
        "title": "AI Notes Summary",
        "summary": response
    }