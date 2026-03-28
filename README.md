
ResearcX AI is a GenAI-powered system that performs multi-document reasoning on research papers to automatically:

Extract key insights

Compare multiple studies

Identify recurring limitations

Detect research gaps

Evaluate innovation potential

Suggest research questions and methodologies

It transforms manual literature review into intelligent research analysis.

🎯 Problem Statement
Researchers spend significant time manually analyzing multiple research papers to identify limitations and uncover research gaps.

This process is:

Time-consuming

Subjective

Difficult to scale

There is a need for an AI-powered system that can automate research understanding, comparison, and gap detection.

💡 Solution
ResearcX AI provides:

📄 Multi-paper analysis

🔎 Cross-paper comparison

🚀 Research gap detection

📊 Novelty scoring (1–10)

⚡ Impact prediction (Low / Medium / High)

🧪 Research question generation

🏗️ Architecture
PDF Upload → Text Extraction → LLM Processing → JSON Output → Streamlit UI
Components:
Frontend: Streamlit

Backend: Python

LLM: Gemini API

Parser: PyMuPDF

Processing: Prompt Engineering + Multi-document reasoning

⚙️ Tech Stack
Python

Streamlit

PyMuPDF

Google Gemini API

JSON-based structured output

📂 Project Structure
ResearcX/
│
├── frontend/
│   └── app.py
│
├── backend/
│   ├── llm_engine.py
│   └── pdf_parser.py
│
├── venv/
├── .env
└── README.md
🔧 Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-link>
cd ResearcX
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install streamlit pymupdf google-generativeai python-dotenv
4️⃣ Add API Key
Create a .env file in root:

GEMINI_API_KEY=your_api_key_here
5️⃣ Run the App
cd frontend
python -m streamlit run app.py
6️⃣ Open in Browser
http://localhost:8501
🧪 How It Works
Upload 2–3 research papers (PDF)

System extracts text

LLM performs multi-document reasoning

Outputs structured JSON containing:

Paper summaries

Comparison insights

Research gaps

Novelty & impact scores

Results displayed in interactive UI

📊 Features
✔ Multi-document analysis
✔ Structured research understanding
✔ Automated gap detection
✔ Innovation scoring system
✔ Impact prediction
✔ Downloadable JSON report

⭐ Novelty
Unlike traditional tools that only summarize papers, ResearcX AI:

Performs cross-paper reasoning

Identifies hidden research gaps

Provides innovation evaluation

Suggests future research directions

🌍 Applications
Academic research

PhD & thesis work

R&D teams

Innovation labs

Startups & product research

📈 Future Scope
Domain-specific models (Healthcare, Fintech, etc.)

Research trend prediction

Patent gap detection

Visualization dashboards

Integration with research databases