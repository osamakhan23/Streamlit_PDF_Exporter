import streamlit as st
from PyPDF2 import PdfReader
import io
from io import BytesIO

# Function to highlight text
def highlight_text(page_text, search_query):
    highlighted = page_text.replace(search_query, f"**{search_query}**")
    return highlighted

st.title("PDF Extractor App")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
search_query = st.text_input("Enter text to search in the PDF")

if uploaded_file is not None:
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))

    # Extract All Text from the PDF
    if st.checkbox("Extract text from all pages"):
        all_text = ""
        for page in pdf_reader.pages:
            all_text += page.extract_text() + "\n"
        st.text_area("All Text", all_text, height=300)

    else:
        page_number = st.number_input("Page number", 1, len(pdf_reader.pages), format='%i') - 1
        page = pdf_reader.pages[page_number]
        page_text = page.extract_text()

        # Search functionality
        if search_query:
            page_text = highlight_text(page_text, search_query)

        st.write(page_text)

        # Prepare text for download
        text_io = BytesIO(page_text.encode('utf-8'))  # Convert page text to BytesIO for download

        # Download extracted text
        if st.button("Download Text"):
            st.download_button(label="Download Text as TXT",
                               data=text_io.getvalue(),
                               file_name="extracted_text.txt",
                               mime="text/plain")
