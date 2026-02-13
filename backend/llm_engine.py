import google.generativeai as genai

genai.configure(api_key="AIzaSyA3V0QZgfpPSB5LcllWqYCxS21QNnnOlxw")

def summarize_paper(text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
    Extract clearly:

    1. Problem Statement
    2. Methodology Used
    3. Key Results

    Research Paper:
    {text[:4000]}
    """

    response = model.generate_content(prompt)

    return response.text
