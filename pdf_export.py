from fpdf import FPDF
from io import BytesIO

def export_to_pdf(transcript, summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Meeting Transcript & Summary", ln=True, align="C")
    pdf.ln(10)

    # Transcript Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Transcript", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, transcript)
    pdf.ln(5)

    # Summary Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Summary", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, summary)

    # Save to memory
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return pdf_output
