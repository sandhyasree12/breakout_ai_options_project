# tests/test_data.py
import unittest
from main import get_option_chain_data, calculate_margin_and_premium

class TestOptionFunctions(unittest.TestCase):
    def test_get_option_chain_data(self):
        df = get_option_chain_data("NIFTY", "2024-11-30", "CE")
        self.assertIn("instrument_name", df.columns)
        self.assertIn("strike_price", df.columns)
        self.assertIn("side", df.columns)
        self.assertIn("bid/ask", df.columns)

    def test_calculate_margin_and_premium(self):
        sample_data = get_option_chain_data("NIFTY", "2024-11-30", "PE")
        result = calculate_margin_and_premium(sample_data)
        self.assertIn("margin_required", result.columns)
        self.assertIn("premium_earned", result.columns)

if __name__ == "__main__":
    unittest.main()
