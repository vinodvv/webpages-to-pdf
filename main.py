import pdfkit


def read_urls_from_file(file_path):
    """
    Read URLs from a given file.
    :param file_path: The path to the file Containing URLs.
    :return: list: A list of URLs read from the file.
    """
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    return urls


def convert_url_to_safe_filename(url):
    """
    Contert a URL to a safe filename by replacing certain characters with underscores.
    :param url: The URL to convert
    :return: The safe filename.
    """
    return url.translate(str.maketrans({":": "_", "/": "_", ".": "_"})) + ".pdf"


def save_webpage_as_pdf(url, output_dir='output'):
    """
    Save a webpage as a PDF file.
    :param url: The URL of the webpage to save.
    :param output_dir: The directory to save the PDF file. Default is 'output'.
    :return: The filename of the saved PDF.
    """
    filename = convert_url_to_safe_filename(url)
    output_file = f"{output_dir}/{filename}"
    pdfkit.from_url(url, output_file)
    return filename


def main():
    """
    Main function to read URLs from a file and save each webpage as a separate PDF.
    """
    file_path = "files/urls.txt"
    urls = read_urls_from_file(file_path)

    for url in urls:
        saved_filename = save_webpage_as_pdf(url)
        print(f"Webpage saved as PDF: {saved_filename}")


if __name__ == "__main__":
    main()
