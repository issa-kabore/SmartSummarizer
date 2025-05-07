from fpdf import FPDF

# Create a sample English PDF file
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

long_text = (
    "Climate change is undeniably one of the most significant global challenges of our time. "
    "Its effects are being felt across the globe, from rising sea levels to more frequent and intense natural disasters. "
    "Governments, businesses, and individuals must take immediate and sustained action to reduce greenhouse gas emissions. "
    "Investing in renewable energy, promoting sustainable transportation, and encouraging conservation are essential steps. "
    "The science is clear: if we do not act now, the consequences will be irreversible and catastrophic."
)

pdf.multi_cell(0, 10, long_text)
pdf.output("tests/sample_en.pdf")
print("✅ PDF created at: tests/sample_en.pdf")
