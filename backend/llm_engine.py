import google.generativeai as genai

genai.configure(api_key="AIzaSyA3V0QZgfpPSB5LcllWqYCxS21QNnnOlxw")

def analyze_multiple_papers(all_papers_text):

    model = genai.GenerativeModel("gemini-2.5-flash")  # use your working model

    combined_text = ""

    for i, text in enumerate(all_papers_text):
        combined_text += f"\n\n----- PAPER {i+1} -----\n{text[:3000]}\n"

    prompt = f"""
    You are an academic research analyst.

    Below are multiple research papers.

    Perform ALL of the following in a structured format:

    1. For each paper:
       - Problem Statement
       - Methodology
       - Key Results
       - Limitations

    2. Compare the papers:
       - Identify recurring weaknesses
       - Identify common limitations
       - Highlight research overlaps

    3. Based on comparison:
       - Identify clear research gaps
       - Explain why each gap exists

    4. For each research gap:
       - Suggest a research question
       - Suggest possible methodology

    Keep output clean and well-structured with headings.

    Papers:
    {combined_text}
    """

    response = model.generate_content(prompt)

    return response.text
