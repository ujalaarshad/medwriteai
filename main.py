# Importing necessary libraries and modules for building the app, handling prompts, 
# generating AI responses, and converting outputs to PDF.
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from prompts import sentiment_prompt, soap_note_prompt, clinical_report_template
from convert_to_pdf import render_markdown_to_pdf
from dotenv import load_dotenv

# Loading environment variables to configure secure API keys or settings.
load_dotenv()

# Setting up the AI model with the chosen configuration for response generation.
# - Temperature (0 - 1) and towards 1 describes more creativity
# - model: llm used

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)

# Creating reusable templates for predefined healthcare-related prompts.
sentiment_template = ChatPromptTemplate.from_template(sentiment_prompt)
soap_template = ChatPromptTemplate.from_template(soap_note_prompt)
clinical_report = ChatPromptTemplate.from_template(clinical_report_template)

# Building the Streamlit UI for user interaction.
st.title("Healthcare Analysis Tool")

# Providing input options for the user: upload a file or manually enter text.
uploaded_file = st.file_uploader("Upload a conversation file (txt format):", type=["txt"])
text_input = st.text_area("Or enter conversation text:")

# Handling the input to create the conversation text.
conversation = ""
if uploaded_file:
    conversation = uploaded_file.read().decode("utf-8")  # Decoding file content to text.
elif text_input:
    conversation = text_input  # Assigning text input directly.

# Processing the conversation text if provided and enabling task selection.
if conversation:
    st.subheader("Select an option:")
    option = st.radio("Choose the type of text to generate:", 
                      ["Sentiment Analysis", "SOAP Notes", "Clinical Report"])
    
    # Optional checkbox to generate a downloadable PDF of the output.
    generate_pdf = st.checkbox("Generate PDF", value=False)
    
    # Triggering the AI model to generate results based on the selected option.
    if st.button("Generate"):
        st.write(f"**Generating {option}...**")
        
        # Dynamically selecting the appropriate prompt template for the chosen task.
        if option == "Sentiment Analysis":
            chain = sentiment_template | llm | StrOutputParser()
        elif option == "SOAP Notes":
            chain = soap_template | llm | StrOutputParser()
        else:
            chain = clinical_report | llm | StrOutputParser()
        
        # Invoking the AI model to process the input and generate results.
        result = chain.invoke(input=conversation)
        st.subheader("Results:")
        st.markdown(f"<div style='font-size:18px; font-weight:bold;'>{result}</div>", unsafe_allow_html=True)
        
        # Generating and allowing download of a PDF file if the option is selected.
        if generate_pdf:
            pdf_filename = "output.pdf"
            render_markdown_to_pdf(result, output_filename=pdf_filename)  # Rendering Markdown to PDF.
            with open(pdf_filename, "rb") as file:
                st.download_button("Download PDF", file, file_name=pdf_filename)
