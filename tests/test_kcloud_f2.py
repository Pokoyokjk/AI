import unittest
from main import extract_abstract

class TestExtractAbstract(unittest.TestCase):

    def test_extract_abstract_exists(self):
        # Path to a sample XML file containing an abstract
        xml_with_abstract_path = "path/to/file_with_abstract.xml"
        
        # Call the function to extract the abstract
        abstract = extract_abstract(xml_with_abstract_path)
        
        # Verify if the abstract was extracted correctly
        self.assertIsNotNone(abstract, "The abstract could not be extracted from the file.")

    def test_extract_abstract_not_exists(self):
        # Path to a sample XML file without an abstract
        xml_without_abstract_path = "path/to/file_without_abstract.xml"
        
        # Call the function to extract the abstract
        abstract = extract_abstract(xml_without_abstract_path)
        
        # Verify that no abstract exists
        self.assertIsNone(abstract, "An abstract was extracted from a file that should not have one.")

if __name__ == '__main__':
    unittest.main()
