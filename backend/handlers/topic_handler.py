from ai_client import ask_ai

def explain_topic(topic):

    prompt = f"""
Explain the topic: {topic}

Give output in this format:

Definition:
Clear definition

Intuition:
Simple explanation

Example:
Real world example
"""

    response = ask_ai(prompt)

    return {
        "title": "AI Topic Explanation",
        "definition": response
    }