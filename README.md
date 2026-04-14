# ⬡ Learnify — Smart Learning Assistant

Learnify is an AI-powered learning assistant that explains code, summarizes notes, and breaks down topics in a clear, structured way.

## Features
- 💻 **Code Mode:** Explains any code snippet step-by-step with complexity analysis.
- 📝 **Notes Mode:** Transforms fragmented, messy notes into structured, exam-ready study guides.
- 🧠 **Topic Mode:** Breaks down complex concepts using a "Definition-Intuition-Example" framework for deep understanding.
- 💾 **Persistent History:** Local browser integration ensures your previous queries are saved and accessible even after a restart.
- 📋 **Copy Output:** Single-click clipboard integration for seamless sharing.
- 📄 **Professional PDF Export:** Generates high-quality, print-optimized documents featuring a minimalist academic layout, refined typography, and a subtle branding signature.

## Tech Stack
- **Frontend** — HTML5, CSS3, JavaScript(ES6+)
- **Backend** — Python, Flask
- **AI Engine** — Groq API (LLaMA 3)

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

## 💡Why Learnify?
Unlike standard AI chats, Learnify is built with a Print-First Design. The PDF export engine uses custom @media print logic to ensure that your study materials are formatted perfectly for physical paper—no cut-off code blocks, no cluttered UI elements, just clean knowledge.
