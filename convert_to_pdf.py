from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import re

def render_markdown_to_pdf(markdown_text, output_filename="report.pdf"):
    # Create a PDF document
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add date and time to the report
    now = datetime.now()
    timestamp = now.strftime("%B %d, %Y - %H:%M:%S")
    date_style = styles["BodyText"]
    date_style.fontSize = 10
    date_style.textColor = "gray"
    elements.append(Paragraph(f"Generated on: {timestamp}", date_style))
    elements.append(Spacer(1, 20))  # Add spacing after the timestamp

    # Parse each line of the Markdown-like text
    for line in markdown_text.splitlines():
        line = line.strip()

        if line.startswith("# "):  # H1
            style = styles["Heading1"]
            elements.append(Paragraph(line[2:], style))
        elif line.startswith("## "):  # H2
            style = styles["Heading2"]
            elements.append(Paragraph(line[3:], style))
        elif line.startswith("- "):  # Bullet points
            style = styles["BodyText"]
            # Handle bold text within bullet points
            formatted_line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line[2:])
            elements.append(Paragraph(f"&bull; {formatted_line}", style))
        elif "**" in line:  # Handle inline bold text
            style = styles["BodyText"]
            formatted_line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
            elements.append(Paragraph(formatted_line, style))
        elif line:  # Normal text
            style = styles["BodyText"]
            elements.append(Paragraph(line, style))

        elements.append(Spacer(1, 12))  # Add spacing between lines

    # Build the PDF
    doc.build(elements)
    print(f"PDF has been successfully generated as '{output_filename}'.")
