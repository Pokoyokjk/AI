# for count_figures
import unittest
from unittest.mock import patch, MagicMock
from main import count_figures

class TestCountFigures(unittest.TestCase):

    @patch('main.GrobidClient')
    def test_count_figures(self, mock_grobid_client):
        # Mock GrobidClient.process method to return sample TEI XML with figures
        mock_process = MagicMock(return_value='<tei><figure></figure><figure></figure></tei>')
        mock_grobid_client.return_value.process = mock_process

        # Call the function to count figures
        num_figures = count_figures("sample.pdf")

        # Verify if the count is correct
        self.assertEqual(num_figures, 2, "Incorrect number of figures counted")

if __name__ == '__main__':
    unittest.main()
