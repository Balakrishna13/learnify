# ⬡ Learnify — Smart Learning Assistant

Learnify is an AI-powered learning assistant that explains code, summarizes notes, and breaks down topics in a clear, structured way.

## Features
- 💻 **Code Mode:** Explains any code snippet step-by-step with complexity analysis.
- 📝 **Notes Mode:** Summarizes and structures messy raw notes into study-ready guides.
- 🧠 **Topic Mode:** Deep-explains concepts using clear definitions, intuitive analogies, and real-world examples.
- 💾 **Persistent History:** Saves your past queries locally in your browser so you never lose your progress.
- 📋 **Copy Output:** Instantly copy any AI-generated explanation to your clipboard.
- 📄 **Professional PDF Export:** Generates a beautifully formatted, print-ready document with a clean academic layout, optimized typography, and a subtle branding signature.

## Tech Stack
- **Frontend** — HTML, CSS, JavaScript
- **Backend** — Python, Flask
- **AI** — Groq API (LLaMA 3)

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/learnify.git
cd learnify
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API key
Create a `.env` file inside the `backend/` folder:
GROQ_API_KEY = key in .env file

### 4. How To Run
Open split terminal
In the 1st terminal(python), enter :
cd backend (or acc.to the path)
python app.py

In the 2nd terminal(powershell), enter :
cd frontend (or acc.to the path)
start index.html
