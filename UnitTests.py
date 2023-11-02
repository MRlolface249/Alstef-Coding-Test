import unittest
import io
from unittest.mock import patch
from Alstef import main

class MyTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=["0"])
    def test_zero(self, mock_input):
        expected_output = "The number you entered is:  0\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["-5"])
    def test_negative(self, mock_input):
        with self.assertRaises(SystemExit) as cm:
            main()
            self.assertEqual(cm.exception.code, 1)

    @patch('builtins.input', side_effect=["50"])
    def test_positive(self, mock_input):
        expected_output = "The number you entered is:  50\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["152"])
    def test_on_range(self, mock_input):
        expected_output = "The number you entered is:  152\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["153"])
    def test_over_range(self, mock_input):
        expected_output = "The number you entered is:  1\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["304"])
    def test_on_range_double(self, mock_input):
        expected_output = "The number you entered is:  152\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["305"])
    def test_over_range_double(self, mock_input):
        expected_output = "The number you entered is:  1\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
