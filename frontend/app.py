import streamlit as st
import sys
import json
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.llm_engine import analyze_multiple_papers
from backend.pdf_parser import extract_text_from_pdf

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="ResearcX AI", layout="centered")

st.title("🧠 ResearcX AI – Research Gap Finder")
st.markdown("""
AI-powered system for:
- Multi-document reasoning  
- Research gap detection  
- Innovation scoring  
- Research question generation  
""")
st.markdown("---")

# -------------------- FILE UPLOAD --------------------
uploaded_files = st.file_uploader(
    "📂 Upload Research Papers (PDF)",
    type="pdf",
    accept_multiple_files=True
)

# -------------------- ANALYZE BUTTON --------------------
if st.button("🚀 Analyze Papers"):

    if uploaded_files:

        all_texts = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            all_texts.append(text)

        with st.spinner("🔎 Performing multi-document reasoning..."):
            final_output = analyze_multiple_papers(all_texts)

        # -------------------- PARSE JSON --------------------
        try:
            data = json.loads(final_output)
        except:
            st.error("⚠ Model output formatting error. Try again.")
            st.stop()

        st.success("✅ Analysis Complete!")

        # ====================================================
        # 📄 PAPER-WISE ANALYSIS
        # ====================================================
        st.markdown("## 📄 Paper-wise Analysis")

        for paper in data["papers"]:
            with st.expander(f"Paper {paper['paper_number']}"):
                st.markdown(f"**Problem:** {paper['problem']}")
                st.markdown(f"**Methodology:** {paper['methodology']}")
                st.markdown(f"**Results:** {paper['results']}")
                st.markdown(f"**Limitations:** {paper['limitations']}")

        # ====================================================
        # 🔎 CROSS PAPER INSIGHTS
        # ====================================================
        st.markdown("## 🔎 Cross-Paper Insights")

        st.markdown(f"**Recurring Weaknesses:** {data['comparison']['recurring_weaknesses']}")
        st.markdown(f"**Common Limitations:** {data['comparison']['common_limitations']}")
        st.markdown(f"**Overlaps:** {data['comparison']['overlaps']}")

        # ====================================================
        # 🚀 RESEARCH GAPS & INNOVATION EVALUATION
        # ====================================================
        st.markdown("## 🚀 Research Gaps & Innovation Evaluation")

        for gap in data["research_gaps"]:
            st.markdown(f"### {gap['gap_title']}")

            st.markdown(f"**Description:** {gap['description']}")
            st.markdown(f"**Reason:** {gap['reason']}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Novelty Score", gap["novelty_score"])

            with col2:
                st.metric("Impact Level", gap["impact_level"])

            st.markdown(f"**Justification:** {gap['justification']}")
            st.markdown(f"**Research Question:** {gap['research_question']}")
            st.markdown(f"**Suggested Methodology:** {gap['suggested_methodology']}")

            st.markdown("---")

        # ====================================================
        # 📥 DOWNLOAD BUTTON
        # ====================================================
        st.download_button(
            label="📥 Download Full Analysis (JSON)",
            data=json.dumps(data, indent=4),
            file_name="research_gap_analysis.json",
            mime="application/json"
        )

    else:
        st.warning("⚠ Please upload at least one PDF.")
