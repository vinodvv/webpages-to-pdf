import pdfkit

file_path = "files/urls.txt"

with open(file_path, 'r') as file:
    urls = [line.strip() for line in file.readlines()]

for url in urls:
    filename = url.translate(str.maketrans({":": "_", "/": "_", ".": "_"})) + ".pdf"
    output_file = f"output/{filename}"
    pdfkit.from_url(url, output_file)
    print(f"Webpage saved as PDF: {filename}")
