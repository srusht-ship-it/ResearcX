import streamlit as st
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.llm_engine import analyze_multiple_papers
from backend.pdf_parser import extract_text_from_pdf

st.title("📄 Research Paper Analyzer")
st.set_page_config(page_title="ResearcX AI", layout="centered")

st.title("🧠 ResearcX AI – Research Gap Finder")
st.markdown("""
AI-powered system for:
- Multi-document reasoning  
- Research gap detection  
- Hypothesis generation  
""")
st.markdown("---")


uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if st.button("Analyze Papers"):
    if uploaded_files:

        all_texts = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            all_texts.append(text)

        with st.spinner("🔎 Performing multi-document reasoning..."):
         final_output = analyze_multiple_papers(all_texts)


        final_output = analyze_multiple_papers(all_texts)

        st.markdown("## 📊 Complete Research Analysis")
        st.markdown("---")
        st.markdown(final_output)
        st.download_button(
    label="📥 Download Research Analysis",
    data=final_output,
    file_name="research_gap_analysis.txt",
    mime="text/plain"
)


        with st.expander("📄 Paper-wise Analysis"):
            st.markdown(final_output)

        with st.expander("🔎 Research Gaps"):
            st.markdown(final_output)

    else:
        st.warning("Please upload at least one PDF.")
