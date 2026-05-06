import streamlit as st
import pandas as pd

from pdf_ocr import pdf_to_text
from cleaner import clean_text
from parser import extract_invoices

# ---------------- UI ----------------
st.title("📄 Smart Invoice OCR System")
st.write("Upload a PDF invoice and extract structured data automatically")

# ---------------- Upload ----------------
uploaded_file = st.file_uploader("Upload PDF invoice", type=["pdf"])

# ---------------- Processing ----------------
if uploaded_file is not None:

    # Save file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing invoice...")

    # Pipeline
    raw_text = pdf_to_text("temp.pdf")
    clean = clean_text(raw_text)
    data = extract_invoices(clean)

    st.success("Done extracting data!")

    # ---------------- JSON ----------------
    st.subheader("📦 JSON Output")
    st.json(data)

    # ---------------- TABLE ----------------
    st.subheader("📊 Extracted Data")
    df = pd.DataFrame(data)
    st.dataframe(df)

    # ---------------- EXCEL DOWNLOAD ----------------
    st.subheader("📥 Export")

    excel_file = "invoices.xlsx"
    df.to_excel(excel_file, index=False)

    with open(excel_file, "rb") as f:
        st.download_button(
            label="Download Excel",
            data=f,
            file_name="invoices.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )