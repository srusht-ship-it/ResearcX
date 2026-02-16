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
        combined_text += f"\n\n----- PAPER {i+1} -----\n{text[:3000]}\n"

    # IMPORTANT: Escaped JSON braces using {{ }}
    prompt = f"""
You are an expert academic research analyst.

Analyze the following research papers.

Return ONLY valid JSON.
Do NOT include explanations.
Do NOT include markdown.
Do NOT wrap JSON in ```.

Return strictly in this structure:

{{
  "papers": [
    {{
      "paper_number": 1,
      "problem": "",
      "methodology": "",
      "results": "",
      "limitations": ""
    }}
  ],
  "comparison": {{
    "recurring_weaknesses": "",
    "common_limitations": "",
    "overlaps": ""
  }},
  "research_gaps": [
    {{
      "gap_title": "",
      "description": "",
      "reason": "",
      "novelty_score": "",
      "impact_level": "",
      "justification": "",
      "research_question": "",
      "suggested_methodology": ""
    }}
  ]
}}

Instructions:
1. Analyze EACH paper separately.
2. Then compare all papers.
3. Identify research gaps.
4. For each gap assign novelty score (1-10).
5. Assign impact level: Low / Medium / High.

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
