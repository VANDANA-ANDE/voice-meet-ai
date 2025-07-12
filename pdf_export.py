from fpdf import FPDF
from io import BytesIO

def export_to_pdf(transcript, summary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, "Transcript:\n" + transcript)
    pdf.ln()
    pdf.multi_cell(0, 10, "Summary:\n" + summary)

    # Get PDF as bytes
    pdf_output = BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin-1')  # Get string, encode as bytes
    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)  # Rewind the buffer

    return pdf_output
