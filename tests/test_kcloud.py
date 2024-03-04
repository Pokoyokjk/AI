# for process_article ()
import unittest
from os.path import isfile
from main import process_article

class TestProcessArticle(unittest.TestCase):

    def test_process_article_output(self):
        # Path de un archivo PDF de prueba
        pdf_path = "ruta/al/archivo.pdf"
        # Directorio de salida para los archivos generados por Grobid
        output_dir = "ruta/al/directorio/output"
        
        # Llamar a la función para procesar el artículo
        process_article(pdf_path, output_dir)
        
        # Verificar si se generó el archivo de salida
        output_file_path = f"{output_dir}/archivo.tei.xml"
        self.assertTrue(isfile(output_file_path), "El archivo de salida no se generó correctamente.")

if __name__ == '__main__':
    unittest.main()
