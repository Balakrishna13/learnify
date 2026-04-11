from ai_client import ask_ai

def explain_code(code):

    prompt = f"""
Explain this code:

{code}

Give:
- What it does
- Step by step explanation
- Time complexity
"""

    response = ask_ai(prompt)

    return {
        "title": "AI Code Explanation",
        "explanation": response
    }