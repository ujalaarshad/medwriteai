# Healthcare Text Analysis Project Documentation

## `main.py`

**Purpose**: `main.py` builds a user-friendly Streamlit web application that facilitates healthcare text analysis using AI. Users can upload text files or manually input conversation data, and the app generates results such as Sentiment Analysis, SOAP Notes, or Clinical Reports. The output can be downloaded as a PDF if desired.

### Key Features:

- **Input Options**: File upload or manual text input.
- **Task Options**: Sentiment Analysis, SOAP Notes, and Clinical Reports.
- **PDF Generation**: Optional PDF generation for results.
- **Interactive UI**: Built using Streamlit for real-time interaction.

### Flow:

1. Load environment variables.
2. Configure the AI model with `ChatGoogleGenerativeAI`.
3. Define templates for each task (sentiment analysis, SOAP notes, and clinical reports).
4. Provide input options (file upload or text area).
5. Process the input and allow task selection.
6. Generate results using LangChain and display them on the UI.
7. Optionally render the result into a downloadable PDF.

## `app.py`

**Purpose**: `app.py` offers a terminal-based alternative to `main.py`, providing the same functionality of healthcare text analysis without requiring a graphical interface.

### Key Features:

- **Task Options**: Sentiment Analysis, SOAP Notes, and Clinical Reports.
- **PDF Option**: Available for SOAP Notes and Clinical Reports.
- **Interactive CLI**: Users select tasks and inputs directly via the command line.

### Flow:

1. Load environment variables.
2. Configure the AI model and task templates.
3. Prompt the user to select a task.
4. Use preloaded conversation data from `example_conversation.py`.
5. Generate and display results.
6. Optionally save results as a PDF.

## `convert_to_pdf.py`

**Purpose**: A utility script for converting Markdown-like text into a professional-looking PDF using the `ReportLab` library.

### Key Features:

- Supports Markdown elements (headers, bullet points, and bold text).
- Adds a timestamp to the PDF.
- Customizes font styles and layout.

### Flow:

1. Parse the Markdown-like text into styled elements.
2. Add a timestamp to the document.
3. Convert text into paragraphs and structure the layout.
4. Save the generated PDF file.

## `example_conversation.py`

**Purpose**: Stores predefined example conversations, simulating patient-doctor interactions, to be used for testing and generating analysis outputs.
