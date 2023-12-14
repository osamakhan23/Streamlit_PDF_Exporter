---

# Streamlit PDF Extractor App

## Introduction

This project is a Streamlit-based web application designed to extract text from PDF files. It allows users to upload a PDF file, select a page, and view the extracted text directly in the browser. This app is ideal for quickly accessing text from PDF documents without the need for complex PDF readers or text extraction tools.

Certainly! Let's enhance your Streamlit PDF Extractor app by adding two new functionalities:

1. **Text Search within the PDF**: Allow users to search for a specific word or phrase within the PDF and highlight instances where it appears on the selected page.
2. **Download Extracted Text**: Provide an option for users to download the extracted text as a `.txt` file.

### Updated Code for App

Here's how you can implement these features in your `app.py`:

```python
import streamlit as st
from PyPDF2 import PdfReader
import io
import re
from io import StringIO

# Function to highlight text
def highlight_text(page_text, search_query):
    highlighted = page_text.replace(search_query, f"**{search_query}**")
    return highlighted

st.title("PDF Extractor App")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
search_query = st.text_input("Enter text to search in the PDF")

if uploaded_file is not None:
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
    page_number = st.number_input("Page number", 1, len(pdf_reader.pages)) - 1
    page = pdf_reader.pages[page_number]
    page_text = page.extract_text()

    # Search functionality
    if search_query:
        page_text = highlight_text(page_text, search_query)

    st.write(page_text)

    # Download extracted text
    download_button = st.button("Download Text")
    if download_button:
        text_io = StringIO(page_text)
        st.download_button(label="Download Text as TXT", data=text_io, file_name="extracted_text.txt", mime="text/plain")
```

### Updated README

For the README, you can update it to reflect these new features. Here's a template:

---

# Streamlit PDF Extractor App

## Introduction

This Streamlit-based web application allows users to extract and interact with text from PDF files. It's an easy-to-use tool for accessing text in PDF documents without the need for complex software.

## What's New in Version 2.0

- **Text Search Functionality**: Users can now search for specific words or phrases within the PDF. The app highlights all occurrences of the search term on the selected page.
- **Download Extracted Text**: Users have the option to download the extracted text from a page as a `.txt` file, making it easier to save and use the data.

## Features

- Upload and view PDF files in the browser.
- Select and view individual pages.
- Search for text within the PDF.
- Download the extracted text as a `.txt` file.
- User-friendly interface with Streamlit.

## Installation

### Prerequisites

- Python 3.6 or higher.
- pip (Python package installer).

### Setup

1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Navigate to the project directory:
   ```
   cd [project-directory]
   ```
3. Create a virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Linux
   ```
4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the app locally:

1. Navigate to the project directory.
2. Start the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open your web browser and go to `http://localhost:8501`.

## How to Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Streamlit](https://streamlit.io) - The fastest way to build and share data apps.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) - A Python library for reading PDF files.

---
