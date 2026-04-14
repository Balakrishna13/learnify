from ai_client import ask_ai

def explain_code(code):

    prompt = f"""
You are an expert programming tutor. Analyze and explain this code in depth:

{code}

Give a thorough explanation with the following sections:

Explanation:
What does this code do overall? Explain the purpose and logic clearly.

Step by Step:
Walk through the code line by line or block by block. Explain what each part does, why it's written that way, and how it contributes to the overall functionality.

Key Concepts:
What programming concepts, patterns or techniques are used here? Explain each one clearly.

Time Complexity:
Analyze the time and space complexity. Explain why, not just what it is.

Example:
Show a concrete example of this code running with sample input and output. Walk through what happens step by step.

Possible Improvements:
Suggest any improvements, optimizations or best practices that could make this code better.

Be detailed and thorough. Assume the reader is a student trying to deeply understand the code.
"""

    response = ask_ai(prompt)

    return {
        "title": "AI Code Explanation",
        "explanation": response
    }