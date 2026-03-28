import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_multiple_papers(all_papers_text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    # Reduce input size (important)
    combined_text = ""
    for i, text in enumerate(all_papers_text):
        combined_text += f"\n\n----- PAPER {i+1} -----\n{text[:1500]}\n"

    prompt = f"""
You are an expert research analyst.

STRICT RULES:
- Return ONLY valid JSON
- No explanations
- No markdown
- No ```json
- Do NOT return empty fields

Return EXACT JSON:

{{
  "papers": [
    {{
      "paper_number": 1,
      "problem": "text",
      "methodology": "text",
      "results": "text",
      "limitations": "text"
    }}
  ],
  "comparison": {{
    "recurring_weaknesses": "text",
    "common_limitations": "text",
    "overlaps": "text"
  }},
  "research_gaps": [
    {{
      "gap_title": "text",
      "description": "text",
      "reason": "text",
      "novelty_score": "1-10",
      "impact_level": "Low/Medium/High",
      "justification": "text",
      "research_question": "text",
      "suggested_methodology": "text"
    }}
  ]
}}

IMPORTANT:
- Analyze ALL papers
- Generate at least 2 research gaps
- Fill all fields

Papers:
{combined_text}
"""

    response = model.generate_content(prompt)
    return response.text.strip()