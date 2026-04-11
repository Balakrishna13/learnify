from handlers.code_handler import explain_code
from handlers.notes_handler import summarize_notes
from handlers.topic_handler import explain_topic

def process_input(mode, text):

    if mode == "code":
        return explain_code(text)

    elif mode == "notes":
        return summarize_notes(text)

    elif mode == "topic":
        return explain_topic(text)

    else:
        return {"error": "Invalid mode"}