# Healthcare Analysis Tool

## Overview

The Healthcare Analysis Tool provides an easy-to-use interface for analyzing healthcare-related conversations using AI. It offers both a web-based interface (Streamlit) and a terminal-based interface for flexibility. The tool supports tasks like **Sentiment Analysis**, **SOAP Notes**, and **Clinical Reports**, with an option to download results as a PDF.

---

## Features

- **Multiple Interfaces**: Choose between a web-based UI and terminal CLI.
- **AI-Powered**: Uses advanced AI models for healthcare text analysis.
- **Task-Specific Outputs**:
  - Sentiment Analysis
  - SOAP Notes
  - Clinical Reports
- **PDF Export**: Save generated outputs in PDF format.

---

## Installation

### Prerequisites

- Python 3.8 or above
- Required libraries listed in `requirements.txt`

### Steps

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables:
   Create a `.env` file.
   Add your API keys and configurations.

### Usage

#### Streamlit Web App

    Run the app:

```bash
streamlit run main.py
```

    #### Use the web UI to:
        - Upload a file or input text manually.
        - Select a task to analyze.
        - View results and download as PDF (if required).

#### Terminal App

    Run the app:

```bash
python app.py
```

    #### Follow the prompts:
        - Choose a task.
        - View the result in the terminal.
        - Save the result as a PDF (optional).

### File Descriptions

`main.py`: Streamlit app for interactive text analysis.
`app.py`: Terminal-based app for text analysis.
`convert_to_pdf.py`: Utility for converting text outputs into PDF files.
`example_conversation.py`: Predefined patient-doctor conversation for testing.
