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
