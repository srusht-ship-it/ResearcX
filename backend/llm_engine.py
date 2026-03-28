import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()



# -------------------------------------------------
# CONFIGURE GEMINI (Use environment variable)
# -------------------------------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Set it as environment variable.")

genai.configure(api_key=api_key)


# -------------------------------------------------
# MAIN FUNCTION
# -------------------------------------------------
def analyze_multiple_papers(all_papers_text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    # Combine truncated paper text
    combined_text = ""
    for i, text in enumerate(all_papers_text):
        combined_text += f"\n\n----- PAPER {i+1} -----\n{text[:1500]}\n"

    # IMPORTANT: Escaped JSON braces using {{ }}
    prompt = f"""
You are an expert research analyst.

STRICT RULES:
- Return ONLY valid JSON
- Do NOT add explanations
- Do NOT add markdown
- Do NOT add ```json
- Ensure ALL keys are present
- Do NOT return empty fields

Return EXACTLY in this format:

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
- Analyze ALL provided papers
- Generate AT LEAST 2 research gaps
- Do NOT return empty arrays

Papers:
{combined_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return json.dumps({
            "error": str(e)
        })
