import streamlit as st
import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from pdf_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Research Gap Finder")

st.title("📚 AI Research Gap Finder")
st.write("Upload a research paper to extract text.")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if st.button("Extract Text"):
    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)

        st.success("Text extracted successfully!")

        # Print first 2000 characters (to avoid overload)
        st.text_area("Extracted Text", text[:2000], height=400)
    else:
        st.warning("Please upload a PDF file first.")
