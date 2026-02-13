import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """
    Takes a Streamlit uploaded file
    Returns full extracted text
    """

    # Read file as bytes
    pdf_bytes = uploaded_file.read()

    # Open PDF from bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    full_text = ""

    # Loop through pages
    for page in doc:
        full_text += page.get_text()

    doc.close()

    return full_text
