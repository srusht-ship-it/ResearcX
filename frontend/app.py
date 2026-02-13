import streamlit as st

# Page Title
st.set_page_config(page_title="AI Research Gap Finder", layout="centered")

st.title("📚ResearcX")
st.write("Upload research papers and analyze research gaps.")

# File Upload Section
uploaded_files = st.file_uploader(
    "Upload 2-3 Research Papers (PDF only)",
    type=["pdf"],
    accept_multiple_files=True
)

# Analyze Button
if st.button("Analyze Papers"):
    
    if not uploaded_files:
        st.warning("Please upload at least one PDF file.")
    else:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

        # Just display file names for now
        for file in uploaded_files:
            st.write("📄", file.name)

        st.info("Analysis will be implemented next...")
