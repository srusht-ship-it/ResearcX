import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.pdf_parser import extract_text_from_pdf
from backend.llm_engine import analyze_multiple_papers


st.title("📚 AI Research Gap Finder")

uploaded_files = st.file_uploader(
    "Upload 2-3 Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)


if st.button("Analyze Papers"):
    if uploaded_files:

        all_texts = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            all_texts.append(text)

        st.info("Analyzing papers... please wait ⏳")

        final_output = analyze_multiple_papers(all_texts)

        st.markdown("## 📊 Complete Research Analysis")
        st.write(final_output)

    else:
        st.warning("Please upload at least one PDF.")
