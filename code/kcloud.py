# for funcitons to interact with the OS
from os import listdir, sep, walk, remove, rmdir, path
# for interfacing with the Grobid server
from grobid_client.grobid_client import GrobidClient
from wordcloud import WordCloud
# for data visualization
import matplotlib.pyplot as plt
from collections import Counter
# for parsing HTML and XML documents
from bs4 import BeautifulSoup




def process_article(pdf_path, output_dir):
    # Process article using Grobid, function to process a PDF article using Grobid and save the output to the specified output directory
    # consolidate_citations is set to true for Grobid to attempt to identify and organize citation references within the text
    # tei_coordinates is set to true for Grobid to include information about the positioning of text elements in the output
    # force is set to true for Grobid to overwrite existing output files without prompting for confirmation
    
    client.process("processFulltextDocument", pdf_path, output=output_dir, consolidate_citations=True, tei_coordinates=True, force=True)

def extract_abstract(pdf_path_xml_path):
    try:
        # Abrir el archivo PDF en modo binario
        with open(pdf_path_xml_path, 'rb') as file:
            # Obtener el TEI XML utilizando Grobid
            tei_xml = file.read()
            
            # Parsear el XML utilizando BeautifulSoup
            soup = BeautifulSoup(tei_xml, 'xml')
            
            # Encontrar el elemento 'abstract' en el XML
            abstract_tag = soup.find('abstract')
            
            # Verificar si se encontró el resumen
            if abstract_tag:
                abstract = abstract_tag.get_text()
                return abstract  # Devolver el resumen como una cadena de texto
            
            else:
                print(f"No se encontró el resumen en el archivo {pdf_path_xml_path}.")
                return None
    except Exception as e:
        print(type(e))
        print(f"Error al procesar el archivo {pdf_path}: {e}")
        return None

def draw_keyword_cloud(text):
    # Verificar si el texto es de tipo bytes-like
    if isinstance(text, (bytes, bytearray)):
        # Si es bytes-like, decodificarlo a una cadena de texto utilizando UTF-8
        text = text.decode('utf-8')
    
    # Generar el word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    # Tamaño de la figura en pulgadas
    plt.figure(figsize=(10, 5))
    # Interpolación bilineal para una mejor definición de la imagen
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Initialize Grobid client
    client = GrobidClient(config_path="./config.json")
    # List of PDFs
    
    
    pdf_path = "~/pdfs"
    output_dir = "./resources"
    
    # Process each PDF in ./pdfs directory    
    client.process(service="processFulltextDocument", input_path=pdf_path, output=output_dir, consolidate_citations=True, tei_coordinates=True, force=True)
    
    for xml in listdir(output_dir):

        print(f"Extracting abstract from {xml}...")
        # Extract abstract
        path_xml = f"{output_dir}{sep}{xml}"
        abstract = extract_abstract(path_xml)
        print(abstract)
        
        if abstract:
            print("Generating keyword cloud...")
            draw_keyword_cloud(abstract)
            print("\n")       

    #Cleanup output directories
    
    for root, dirs, files in walk(output_dir, topdown=False):
        for name in files:
            remove(path.join(root, name))
        for name in dirs:
            rmdir(path.join(root, name))
    
