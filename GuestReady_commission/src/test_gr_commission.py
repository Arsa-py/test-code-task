import unittest
from unittest.mock import patch
from gr_commission import get_commission

@patch('gr_commission.print')
class TestGetCommission(unittest.TestCase):
    
    @patch('gr_commission.input', return_value='2012-06-07')
    def test_high_season_commission(self, mock_print, mock_input):
        self.assertEqual(get_commission('2012-06-07'), 0.15)

    @patch('gr_commission.input', return_value='2012-10-07')
    def test_low_season_commission(self, mock_print, mock_input):
        self.assertEqual(get_commission('2012-10-07'), 0.10)

    @patch('gr_commission.input', return_value='2012-12-25')
    def test_xmas_dec_commission(self, mock_print, mock_input):
        self.assertEqual(get_commission('2012-12-25'), 0.12)

    @patch('gr_commission.input', return_value='2012-01-07')
    def test_xmas_jan_commission(self, mock_print, mock_input):
        self.assertEqual(get_commission('2012-01-07'), 0.13)

if __name__ == "__main__":
    unittest.main()