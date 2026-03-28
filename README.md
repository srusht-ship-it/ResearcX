# 🧠 ResearcX AI – Research Gap Finder

ResearcX AI is a GenAI-powered system that performs multi-document reasoning on research papers to automatically:

- ✅ Extract key insights
- ✅ Compare multiple studies
- ✅ Identify recurring limitations
- ✅ Detect research gaps
- ✅ Evaluate innovation potential
- ✅ Suggest research questions and methodologies

It transforms manual literature review into intelligent research analysis.

## 🎯 Problem Statement

Researchers spend significant time manually analyzing multiple research papers to identify limitations and uncover research gaps. This process is:

- ⏱️ Time-consuming
- 🤔 Subjective
- 📊 Difficult to scale

ResearcX AI solves this by automating research understanding, comparison, and gap detection.

## 💡 Solution

ResearcX AI provides:

- 📄 **Multi-paper analysis** – Analyze multiple PDFs simultaneously
- 🔎 **Cross-paper comparison** – Identify patterns across papers
- 🚀 **Research gap detection** – Find unaddressed research areas
- 📊 **Novelty scoring** – Rate innovation potential (1–10)
- ⚡ **Impact prediction** – Assess potential impact (Low/Medium/High)
- 🧪 **Research question generation** – Auto-generate follow-up questions

## 🏗️ Architecture

```
PDF Upload → Text Extraction → LLM Processing → JSON Output → Streamlit UI
```

**Components:**

- **Frontend:** Streamlit (Web UI)
- **Backend:** Python (Logic & API integration)
- **LLM:** Google Gemini API (AI reasoning)
- **Parser:** PyMuPDF (PDF extraction)
- **Output:** Structured JSON data

## ⚙️ Tech Stack

- Python 3.13+
- Streamlit (UI framework)
- PyMuPDF (PDF parsing)
- Google Gemini API (LLM)
- python-dotenv (Environment config)

## 📂 Project Structure

```
ResearcX/
├── frontend/
│   └── app.py                 # Streamlit web interface
├── backend/
│   ├── llm_engine.py          # Gemini API integration & reasoning
│   ├── pdf_parser.py          # PDF text extraction
│   └── test.py                # Backend testing script
├── .env                       # Environment variables (API keys)
└── README.md                  # This file
```

## 🔧 Installation & Setup

### Prerequisites

- Python 3.13+
- A Google Gemini API key (free at [aistudio.google.com](https://aistudio.google.com))

### Step 1: Clone Repository

```bash
cd d:\ResearcX
```

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### Step 3: Install Dependencies

```bash
pip install streamlit pymupdf google-generativeai python-dotenv
```

### Step 4: Configure API Key

Edit the `.env` file in the project root:

```
GEMINI_API_KEY=your_actual_api_key_here
```

## 🚀 Running the Application

### Run the Main Streamlit App

```bash
cd d:\ResearcX
python -m streamlit run frontend/app.py
```

The app will open in your browser at `http://localhost:8501`

**How to use:**

1. Upload one or more PDF research papers
2. Click the "🚀 Analyze Papers" button
3. Wait for AI analysis to complete
4. View research gaps, novelty scores, and generated questions

### Run Backend Tests

To test the Gemini API connection:

```bash
python backend/test.py
```

This will list all available Gemini models for your API key.

## 🔑 Environment Variables

Create a `.env` file with:

```
GEMINI_API_KEY=your_google_gemini_api_key
```

**To get a free API key:**

1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Copy your key and paste it in `.env`

## 📋 Usage Example

1. **Upload PDFs:** Click "📂 Upload Research Papers" and select multiple PDF files
2. **Analyze:** Click "🚀 Analyze Papers" to process
3. **View Results:** See structured analysis including:
   - Paper summaries
   - Identified problems and solutions
   - Research gaps
   - Novelty scores
   - Impact predictions
   - Generated research questions

## ⚠️ Troubleshooting

### Issue: `streamlit: The term 'streamlit' is not recognized`

**Solution:** Use the full Python path:

```bash
python -m streamlit run frontend/app.py
```

### Issue: `ModuleNotFoundError: No module named 'google.generativeai'`

**Solution:** Install dependencies:

```bash
pip install google-generativeai pymupdf
```

### Issue: `GEMINI_API_KEY not found`

**Solution:** Ensure `.env` file exists in the project root with your API key.

### Issue: PDF extraction fails

**Solution:** Ensure the PDF is not corrupted and PyMuPDF is installed:

```bash
pip install pymupdf
```

## 📝 API Reference

### `analyze_multiple_papers(all_papers_text)`

Analyzes multiple paper texts using Gemini API.

- **Input:** List of paper text strings
- **Output:** JSON with analysis results

### `extract_text_from_pdf(uploaded_file)`

Extracts text from uploaded PDF file.

- **Input:** Streamlit uploaded file object
- **Output:** Extracted text string

## 🤝 Contributing

Feel free to extend ResearcX AI with:

- Additional LLM models
- Enhanced PDF parsing
- Database integration
- Export formats (CSV, JSON, etc.)

## 📄 License

This project is open source.
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
