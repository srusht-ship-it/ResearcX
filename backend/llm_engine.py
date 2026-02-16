import google.generativeai as genai

genai.configure(api_key="AIzaSyA3V0QZgfpPSB5LcllWqYCxS21QNnnOlxw")

def analyze_multiple_papers(all_papers_text):

    model = genai.GenerativeModel("gemini-2.5-flash")  # use your working model

    combined_text = ""

    for i, text in enumerate(all_papers_text):
        combined_text += f"\n\n----- PAPER {i+1} -----\n{text[:3000]}\n"

    prompt = f"""
   Return output strictly in this format:

=== PAPER-WISE ANALYSIS ===
Paper 1:
- Problem:
- Methodology:
- Results:
- Limitations:

Paper 2:
...

=== CROSS PAPER COMPARISON ===
- Recurring Weaknesses:
- Common Limitations:
- Overlaps:

=== RESEARCH GAPS ===
Gap 1:
Reason:
Evidence:

Gap 2:
...

=== SUGGESTED RESEARCH QUESTIONS ===
For Gap 1:
- Research Question:
- Suggested Methodology:


    Papers:
    {combined_text}
    """

    response = model.generate_content(prompt)

    return response.text
