import streamlit as st
import sys
import json
import re
from pathlib import Path

# Add backend path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.llm_engine import analyze_multiple_papers
from backend.pdf_parser import extract_text_from_pdf

# ---------------- UI ----------------
st.set_page_config(page_title="ResearcX AI", layout="centered")

st.title("🧠 ResearcX AI – Research Gap Finder")
st.markdown("""
AI-powered system for:
- Multi-document reasoning  
- Research gap detection  
- Innovation scoring  
""")
st.markdown("---")

uploaded_files = st.file_uploader(
    "📂 Upload Research Papers",
    type="pdf",
    accept_multiple_files=True
)

# ---------------- MAIN ----------------
if st.button("🚀 Analyze Papers"):

    if uploaded_files:

        all_texts = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            all_texts.append(text)

        with st.spinner("🔎 Analyzing..."):
            final_output = analyze_multiple_papers(all_texts)

        # DEBUG (important)
        st.markdown("### 🔍 Raw Output (for debugging)")
        st.text(final_output)

        # Clean JSON
        try:
            cleaned = re.sub(r"```json|```", "", final_output).strip()
            data = json.loads(cleaned)
        except:
            st.error("⚠ JSON parsing failed")
            st.stop()

        # Safe access
        papers = data.get("papers", [])
        comparison = data.get("comparison", {})
        gaps = data.get("research_gaps", [])

        st.success("✅ Analysis Complete!")

        # ---------------- PAPERS ----------------
        st.markdown("## 📄 Paper-wise Analysis")

        for paper in papers:
            with st.expander(f"Paper {paper.get('paper_number')}"):
                st.write("Problem:", paper.get("problem"))
                st.write("Methodology:", paper.get("methodology"))
                st.write("Results:", paper.get("results"))
                st.write("Limitations:", paper.get("limitations"))

        # ---------------- COMPARISON ----------------
        st.markdown("## 🔎 Insights")

        st.write("Recurring Weaknesses:", comparison.get("recurring_weaknesses"))
        st.write("Common Limitations:", comparison.get("common_limitations"))
        st.write("Overlaps:", comparison.get("overlaps"))

        # ---------------- GAPS ----------------
        st.markdown("## 🚀 Research Gaps")

        for gap in gaps:
            st.markdown(f"### {gap.get('gap_title')}")

            st.write("Description:", gap.get("description"))
            st.write("Reason:", gap.get("reason"))

            col1, col2 = st.columns(2)
            col1.metric("Novelty", gap.get("novelty_score"))
            col2.metric("Impact", gap.get("impact_level"))

            st.write("Justification:", gap.get("justification"))
            st.write("Research Question:", gap.get("research_question"))
            st.write("Methodology:", gap.get("suggested_methodology"))

            st.markdown("---")

    else:
        st.warning("Upload at least one PDF")