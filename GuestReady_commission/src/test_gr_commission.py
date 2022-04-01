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

if __name__ == "__main__":
    unittest.main()