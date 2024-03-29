# for funcitons to interact with the OS
from os import listdir, sep, walk, remove, rmdir, path
# for interfacing with the Grobid server
from grobid_client.grobid_client import GrobidClient
# for data visualization
import matplotlib.pyplot as plt
from collections import Counter
# for parsing HTML and XML documents
from bs4 import BeautifulSoup

# Initialize Grobid client
client = GrobidClient(config_path="./config.json")

def process_article(pdf_path, output_dir):
    # Process article using Grobid, function to process a PDF article using Grobid and save the output to the specified output directory
    # consolidate_citations is set to true for Grobid to attempt to identify and organize citation references within the text
    # tei_coordinates is set to true for Grobid to include information about the positioning of text elements in the output
    # force is set to true for Grobid to overwrite existing output files without prompting for confirmation
    client.process("processFulltextDocument", pdf_path, output=output_dir, consolidate_citations=True, tei_coordinates=True, force=True)

def count_figures(pdf_path):
    with open(pdf_path, 'rb') as file:
        # Count figures from TEI XML
        tei_xml = client.process("processFulltextDocument", file.read(), consolidate_citations=True, tei_coordinates=True, force=True)
        soup = BeautifulSoup(tei_xml, 'xml')
        # the library BeautifulSoup allows to use the method find_all for the extraction of all the figure's occurrences
        figures = soup.find_all('figure')
        # returns the count 
        return len(figures)

if __name__ == "__main__":
    # Initialize Grobid client
    client = GrobidClient(config_path="./config.json")
    # List of PDFs
    
    
    pdf_path = "~/pdfs"
    output_dir = "./resources"

    # Process each PDF in ./pdfs directory    
    client.process(service="processFulltextDocument", input_path=pdf_path, output=output_dir, consolidate_citations=True, tei_coordinates=True, force=True)

    for xml in listdir(output_dir):
        # Count figures
        num_figures = count_figures(pdf_path)
        print(f"Number of figures: {num_figures}")

        print("\n") 

    #Cleanup output directories
    for root, dirs, files in walk(output_dir, topdown=False):
        for name in files:
            remove(path.join(root, name))
        for name in dirs:
            rmdir(path.join(root, name))
