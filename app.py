# Importing required modules for handling prompts, AI interactions, environment variables, 
# PDF generation, and using predefined conversation text.
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from prompts import sentiment_prompt, soap_note_prompt, clinical_report_template
from dotenv import load_dotenv
from example_conversation import convo as conversation  
from convert_to_pdf import render_markdown_to_pdf  # Converting generated text to a PDF format

# Loading environment variables to configure API keys or settings.
load_dotenv()

# Initializing the AI model with specified parameters for generating tailored responses.
# - Temperature (0 - 1) and towards 1 describes more creativity
# - model: llm used
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)

# Creating templates for predefined tasks to structure AI prompts.
sentiment_template = ChatPromptTemplate.from_template(sentiment_prompt)  # For sentiment analysis
soap_template = ChatPromptTemplate.from_template(soap_note_prompt)  
clinical_report = ChatPromptTemplate.from_template(clinical_report_template) 

# Main function for interacting with the user and generating outputs.
def main():
    # Providing options for users to select a task to perform.
    print("Select an option:")
    print("1. Sentiment Analysis")
    print("2. SOAP Notes")
    print("3. Clinical Report")
    
    # Taking user input to determine the task to execute.
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice == "1":
        print("Generating Sentiment Analysis...")
        chain = sentiment_template | llm | StrOutputParser()  # Setting up the chain for sentiment analysis
        allow_pdf = False  
    elif choice == "2":
        print("Generating SOAP Notes...")
        chain = soap_template | llm | StrOutputParser()  # Setting up the chain for SOAP notes
        allow_pdf = True  
    elif choice == "3":
        print("Generating Clinical Report...")
        chain = clinical_report | llm | StrOutputParser()  # Setting up the chain for clinical reports
        allow_pdf = True  
    else:
        print("Invalid choice.")
        return
    
    # Generating the output using the selected chain and displaying it.
    result = chain.invoke(input=conversation)
    print("\nGenerated Text:")
    print(result)
    
    # Offering the option to save the result as a PDF if allowed for the chosen task.
    if allow_pdf:
        save_pdf = input("\nDo you want to save the result as a PDF? (yes/no): ").strip().lower()
        if save_pdf == "yes":
            render_markdown_to_pdf(result, output_filename="output.pdf")  # Generating the PDF
            print("PDF generated: output.pdf")
        else:
            print("PDF not generated.")

# Ensuring the script runs the main function when executed.
if __name__ == "__main__":
    main()
