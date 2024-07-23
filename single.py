import pdfkit

# Define the URL and the output file path
url = "https://en.wikipedia.org/wiki/Elephant"

filename = url.translate(str.maketrans({":": "_", "/": "_", ".": "_"})) + ".pdf"
output_file = f"output/{filename}"

# Convert the URL to a PDF
pdfkit.from_url(url, output_file)

print(f"Webpage saved as PDF: {filename}")
