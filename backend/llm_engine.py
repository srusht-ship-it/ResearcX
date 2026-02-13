import google.generativeai as genai

genai.configure(api_key="AIzaSyA3V0QZgfpPSB5LcllWqYCxS21QNnnOlxw")

def analyze_paper(text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    You are an academic research assistant.

    From the research paper below extract:

    1. Problem Statement
    2. Methodology Used
    3. Key Results
    4. Limitations (explicit and implicit)

    Return clearly structured headings.

    Research Paper:
    {text[:4000]}
    """

    response = model.generate_content(prompt)

    return response.text

def compare_papers(all_analyses):

    model = genai.GenerativeModel("gemini-2.5-flash")

    combined_text = "\n\n".join(all_analyses)

    prompt = f"""
    You are an academic research analyst.

    Compare the following research papers.

    Identify:
    1. Recurring weaknesses
    2. Common limitations
    3. Overlapping research patterns

    Papers:
    {combined_text}
    """

    response = model.generate_content(prompt)

    return response.text
