let currentMode = "code";
let currentOutputHTML = "";

// Initialize the app by fetching history from PostgreSQL
document.addEventListener("DOMContentLoaded", renderHistory);

function setMode(mode, btn) {
    currentMode = mode;
    document.querySelectorAll(".mode-btn")
        .forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
}

async function processInput() {
    const text = document.getElementById("inputText").value;

    if (!text.trim()) {
        alert("Please enter input");
        return;
    }

    const btn = document.querySelector(".process-btn");
    btn.classList.add("loading");
    btn.querySelector(".btn-text").textContent = "Processing...";

    // Reset UI for new output
    document.getElementById("copyBtn").style.display = "none";
    document.getElementById("exportBtn").style.display = "none";
    document.getElementById("output").innerHTML = `
        <div class="spinner">
            <div class="spinner-ring"></div>
            <span class="spinner-text">Thinking...</span>
        </div>`;

    try {
        const response = await fetch("http://127.0.0.1:8000/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mode: currentMode, text: text })
        });

        const data = await response.json();
        let outputHTML = "";

        // Dynamically build output based on AI response keys
        if (data.title)       outputHTML += `<h2>${data.title}</h2>`;
        if (data.summary)     outputHTML += `<div class="section"><h3>Summary</h3>${marked.parse(data.summary)}</div>`;
        if (data.points) {
            outputHTML += `<div class="section"><h3>Key Points</h3><ul>`;
            data.points.forEach(p => { outputHTML += `<li>${marked.parse(p)}</li>`; });
            outputHTML += `</ul></div>`;
        }
        if (data.explanation) outputHTML += `<div class="section"><h3>Explanation</h3>${marked.parse(data.explanation)}</div>`;
        if (data.steps) {
            outputHTML += `<div class="section"><h3>Steps</h3><ol>`;
            data.steps.forEach(s => { outputHTML += `<li>${marked.parse(s)}</li>`; });
            outputHTML += `</ol></div>`;
        }
        if (data.complexity)  outputHTML += `<div class="section"><h3>Complexity</h3>${marked.parse(data.complexity)}</div>`;
        if (data.definition)  outputHTML += `<div class="section"><h3>Definition</h3>${marked.parse(data.definition)}</div>`;
        if (data.intuition)   outputHTML += `<div class="section"><h3>Intuition</h3>${marked.parse(data.intuition)}</div>`;
        if (data.example)     outputHTML += `<div class="section"><h3>Example</h3>${marked.parse(data.example)}</div>`;

        currentOutputHTML = outputHTML;
        document.getElementById("output").innerHTML = outputHTML;
        document.getElementById("copyBtn").style.display = "block";
        document.getElementById("exportBtn").style.display = "block";

        // Refresh the history sidebar from the database after processing
        renderHistory();

    } catch (error) {
        document.getElementById("output").innerHTML =
            `<div class="error">⚠ Error connecting to backend. Make sure the server is running.</div>`;
    } finally {
        btn.classList.remove("loading");
        btn.querySelector(".btn-text").textContent = "Process";
    }
}

// Fetches the last 10 items from PostgreSQL via the FastAPI /history route
async function renderHistory() {
    const list = document.getElementById("historyList");
    if (!list) return;

    try {
        const response = await fetch("http://127.0.0.1:8000/history");
        const history = await response.json();

        if (!history || history.length === 0) {
            list.innerHTML = `<div class="history-empty">No history yet</div>`;
            return;
        }

        list.innerHTML = history.map(item => `
            <div class="history-item" onclick="loadHistoryItem('${item.mode}', '${item.input.replace(/'/g, "\\'")}')">
                <div class="history-item-mode">${item.mode}</div>
                <div class="history-item-text">${item.input.substring(0, 40)}${item.input.length > 40 ? '...' : ''}</div>
                <div class="history-item-time">${item.time}</div>
            </div>
        `).join('');
    } catch (error) {
        console.error("History fetch error:", error);
        list.innerHTML = `<div class="history-empty">Error loading history</div>`;
    }
}

// Re-loads a previous input into the text area for editing or re-processing
function loadHistoryItem(mode, text) {
    document.getElementById("inputText").value = text;
    currentMode = mode;

    // Synchronize the mode buttons
    document.querySelectorAll(".mode-btn").forEach(b => {
        b.classList.remove("active");
        if (b.textContent.trim().toLowerCase().includes(mode)) {
            b.classList.add("active");
        }
    });
}

function copyOutput() {
    const text = document.getElementById("output").innerText;
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById("copyBtn");
        btn.textContent = "✓ Copied!";
        btn.classList.add("copied");
        setTimeout(() => {
            btn.textContent = "⎘ Copy";
            btn.classList.remove("copied");
        }, 2000);
    });
}

async function exportPDF() {
    const date = new Date().toLocaleString();
    const footer = `<div class="pdf-footer">Generated by Learnify • ${date}</div>`;
    const output = document.getElementById("output");

    output.insertAdjacentHTML("beforeend", footer);

    setTimeout(() => {
        window.print();
        const footerEl = document.querySelector(".pdf-footer");
        if (footerEl) footerEl.remove();
    }, 100);
}