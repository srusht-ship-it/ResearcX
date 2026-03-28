import streamlit as st
import sys
import json
import re
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

        # -------------------- CLEAN + PARSE JSON --------------------
        try:
            cleaned_output = re.sub(r"```json|```", "", final_output).strip()
            data = json.loads(cleaned_output)
        except Exception as e:
            st.error("⚠ JSON parsing failed. Showing raw output below:")
            st.text(cleaned_output)
            st.stop()

        st.success("✅ Analysis Complete!")

        # Safe access
        papers = data.get("papers", [])
        comparison = data.get("comparison", {})
        gaps = data.get("research_gaps", [])

        # ====================================================
        # 📄 PAPER-WISE ANALYSIS
        # ====================================================
        st.markdown("## 📄 Paper-wise Analysis")

        if papers:
            for paper in papers:
                with st.expander(f"Paper {paper.get('paper_number', '?')}"):
                    st.markdown(f"**Problem:** {paper.get('problem', 'N/A')}")
                    st.markdown(f"**Methodology:** {paper.get('methodology', 'N/A')}")
                    st.markdown(f"**Results:** {paper.get('results', 'N/A')}")
                    st.markdown(f"**Limitations:** {paper.get('limitations', 'N/A')}")
        else:
            st.warning("No paper data found.")

        # ====================================================
        # 🔎 CROSS PAPER INSIGHTS
        # ====================================================
        st.markdown("## 🔎 Cross-Paper Insights")

        st.markdown(f"**Recurring Weaknesses:** {comparison.get('recurring_weaknesses', 'N/A')}")
        st.markdown(f"**Common Limitations:** {comparison.get('common_limitations', 'N/A')}")
        st.markdown(f"**Overlaps:** {comparison.get('overlaps', 'N/A')}")

        # ====================================================
        # 🚀 RESEARCH GAPS & INNOVATION EVALUATION
        # ====================================================
        st.markdown("## 🚀 Research Gaps & Innovation Evaluation")

        if gaps:
            for gap in gaps:
                st.markdown(f"### {gap.get('gap_title', 'Untitled Gap')}")

                st.markdown(f"**Description:** {gap.get('description', 'N/A')}")
                st.markdown(f"**Reason:** {gap.get('reason', 'N/A')}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Novelty Score", gap.get("novelty_score", "N/A"))

                with col2:
                    st.metric("Impact Level", gap.get("impact_level", "N/A"))

                st.markdown(f"**Justification:** {gap.get('justification', 'N/A')}")
                st.markdown(f"**Research Question:** {gap.get('research_question', 'N/A')}")
                st.markdown(f"**Suggested Methodology:** {gap.get('suggested_methodology', 'N/A')}")
                
                st.markdown("---")
        else:
            st.warning("No research gaps found.")

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