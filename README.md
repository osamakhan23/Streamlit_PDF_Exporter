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
