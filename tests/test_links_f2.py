# for extract_links()
import unittest
from unittest.mock import patch, MagicMock
from main import extract_links

class TestExtractLinks(unittest.TestCase):

    @patch('main.GrobidClient')
    def test_extract_links(self, mock_grobid_client):
        # Mock GrobidClient.process method to return sample TEI XML with links
        mock_process = MagicMock(return_value='<tei><ref target="https://example.com"></ref><ref target="https://example.org"></ref></tei>')
        mock_grobid_client.return_value.process = mock_process

        # Call the function to extract links
        links = extract_links("sample.pdf")

        # Verify if the links are extracted correctly
        expected_links = ["https://example.com", "https://example.org"]
        self.assertEqual(links, expected_links, "Incorrect links extracted")

if __name__ == '__main__':
    unittest.main()
