import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.pdf_parser import extract_text_from_pdf
from backend.llm_engine import analyze_paper

st.title("📚 AI Research Gap Finder")

uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type=["pdf"])

if st.button("Analyze Paper"):
    if uploaded_file is not None:

        # Extract text
        text = extract_text_from_pdf(uploaded_file)

        st.info("Generating summary... please wait ⏳")

        # Get summary from LLM
        analysis = analyze_paper(text)


        st.success("Summary Generated Successfully!")

        st.markdown("## 📌 Paper Analysis")
        st.write(analysis)

    else:
        st.warning("Please upload a PDF file first.")
