# for process_article ()
import unittest
from unittest.mock import patch, MagicMock
from main import process_article

class TestProcessArticle(unittest.TestCase):

    @patch('main.GrobidClient')
    def test_process_article(self, mock_grobid_client):
        # Mock GrobidClient.process method
        mock_process = MagicMock()
        mock_grobid_client.return_value.process = mock_process

        # Call the function to process the article
        process_article("sample.pdf", "./output")

        # Verify if GrobidClient.process method was called with correct arguments
        mock_process.assert_called_once_with("processFulltextDocument", "sample.pdf", output="./output", consolidate_citations=True, tei_coordinates=True, force=True)

if __name__ == '__main__':
    unittest.main()
