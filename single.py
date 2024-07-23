import pdfkit


def convert_url_to_pdf(url, output_dir="output"):
    """
    Convert a given URL to a PDF file.

    :param url: The URL of the webpage to convert.

    :param output_dir: The directory to ave the output PDF file. Default is 'output'.

    :return: The filename of the saved PDF.
    """
    # Generate a safe filename by replacing certain characters with underscores
    filename = url.translate(str.maketrans({":": "_", "/": "_", ".": "_"})) + ".pdf"
    output_file = f"{output_dir}/{filename}"

    # Convert the URL to a PDF and save it.
    pdfkit.from_url(url, output_file)

    return filename


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Elephant"
    saved_filename = convert_url_to_pdf(url)
    print(f"Webpage saved as PDF: {saved_filename}")
