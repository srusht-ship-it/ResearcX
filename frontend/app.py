import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.pdf_parser import extract_text_from_pdf
from backend.llm_engine import analyze_paper, compare_papers

st.title("📚 AI Research Gap Finder")

uploaded_files = st.file_uploader(
    "Upload 2-3 Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze Papers"):
    if uploaded_files:

        all_analyses = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            analysis = analyze_paper(text)
            all_analyses.append(analysis)

            st.markdown(f"## 📄 Analysis: {file.name}")
            st.write(analysis)

        comparison = compare_papers(all_analyses)

        st.markdown("## 🔎 Cross-Paper Comparison")
        st.write(comparison)

    else:
        st.warning("Please upload at least one PDF.")