from ai_client import ask_ai

def explain_topic(topic):

    prompt = f"""
You are an expert tutor. Explain the topic "{topic}" in depth.

Give a thorough explanation with the following sections:

Definition:
A clear, precise definition of the topic.

Intuition:
A simple, intuitive explanation using analogies or real world comparisons. Help the reader truly understand it, not just memorize it.

Key Points:
- List the most important things to know about this topic
- Include any important properties, rules, or characteristics
- Be specific and detailed

Example:
A detailed real world example that clearly demonstrates the concept. Walk through it step by step.

If relevant, also include:
- Common misconceptions
- How it connects to related concepts
- Why it matters in practice

Be thorough and detailed. Don't give a surface level explanation.
"""

    response = ask_ai(prompt)

    return {
        "title": f"AI Topic Explanation",
        "definition": response
    }