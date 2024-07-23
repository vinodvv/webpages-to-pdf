# Webpage to PDF Converter

This project provides a utility to convert webpages (URLs) to PDF files using Python. It supports both single URL conversion and batch export of multiple URLs to PDF.

## Features

- Convert a single URL to a PDF.
- Batch export multiple URLs to PDF from a file.
- Automatically generates safe filenames for URLs by replacing certain characters.

## Requirements

- Python 3.x
- `pdfkit` library
- `wkhtmltopdf` tool

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/vinodvv/webpages-to-pdf.git
   cd webpages-to-pdf-converter

2. Install the required Python package:

pip install pdfkit

Install wkhtmltopdf:

*   For Windows, download the installer from wkhtmltopdf and add the installation directory to your system's PATH.

* For macOS, you can install it using Homebrew:

brew install wkhtmltopdf

* For Linux, you can install it using your package manager:

sudo apt-get install wkhtmltopdf

# Usage
### Single URL to PDF
You can convert a single URL to a PDF by calling the convert_url_to_pdf function.

import pdfkit

      def convert_url_to_pdf(url: str, output_dir: str = "output") -> str:
          """
          Convert a given URL to a PDF file.
      
          Parameters:
          url (str): The URL of the webpage to convert.
          output_dir (str): The directory to save the output PDF file. Default is 'output'.
      
          Returns:
          str: The filename of the saved PDF.
          """
          # Generate a safe filename by replacing certain characters with underscores
          filename = url.translate(str.maketrans({":": "_", "/": "_", ".": "_"})) + ".pdf"
          output_file = f"{output_dir}/{filename}"
      
          # Convert the URL to a PDF and save it
          pdfkit.from_url(url, output_file)
      
          return filename
      
      if __name__ == "__main__":
          url = "https://en.wikipedia.org/wiki/Elephant"
          saved_filename = convert_url_to_pdf(url)
          print(f"Webpage saved as PDF: {saved_filename}")



# Batch Export URLs to PDF
You can convert multiple URLs to PDF by reading them from a file and using the provided script.

1. Create a file named urls.txt inside a directory named files (create the directory if it doesn't exist). Add each URL on a new line.

2. Run the following script:

import pdfkit

      def read_urls_from_file(file_path: str) -> list:
          """
          Read URLs from a given file.
      
          Parameters:
          file_path (str): The path to the file containing URLs.
      
          Returns:
          list: A list of URLs read from the file.
          """
          with open(file_path, 'r') as file:
              urls = [line.strip() for line in file.readlines()]
          return urls

      def convert_url_to_safe_filename(url: str) -> str:
          """
          Convert a URL to a safe filename by replacing certain characters with underscores.
      
          Parameters:
          url (str): The URL to convert.
      
          Returns:
          str: The safe filename.
          """
          return url.translate(str.maketrans({":": "_", "/": "_", ".": "_"})) + ".pdf"

      def save_webpage_as_pdf(url: str, output_dir: str = "output") -> str:
          """
          Save a webpage as a PDF file.
      
          Parameters:
          url (str): The URL of the webpage to save.
          output_dir (str): The directory to save the PDF file. Default is 'output'.
      
          Returns:
          str: The filename of the saved PDF.
          """
          filename = convert_url_to_safe_filename(url)
          output_file = f"{output_dir}/{filename}"
          pdfkit.from_url(url, output_file)
          return filename

      def main():
          """
          Main function to read URLs from a file and save each webpage as a PDF.
          """
          file_path = "files/urls.txt"
          urls = read_urls_from_file(file_path)
          
          for url in urls:
              saved_filename = save_webpage_as_pdf(url)
              print(f"Webpage saved as PDF: {saved_filename}")

      if __name__ == "__main__":
            main()

# License
This project is licensed under the MIT License. See the LICENSE file for details.


      This `README.md` file includes sections for features, requirements, installation, usage (both single URL and batch export), and license. Adjust the `git clone` URL to your repository if necessary.
