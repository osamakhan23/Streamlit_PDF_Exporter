import streamlit as st
from PyPDF2 import PdfReader
import io

st.title("PDF Extractor App")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    # Updated to use PdfReader instead of PdfFileReader
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
    st.write("Number of pages:", len(pdf_reader.pages))
    page_number = st.number_input("Page number", 1, len(pdf_reader.pages)) - 1
    page_contents = pdf_reader.pages[page_number].extract_text()
    st.write(page_contents)
