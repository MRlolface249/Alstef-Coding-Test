import unittest
import io
from unittest.mock import patch
from Alstef import main, readPersistedNumber, persistCurrentNumber

class MyTestCase(unittest.TestCase):

    # tests for issue #2, tests were modified to fit issue #4

    @patch('builtins.input', side_effect=["0"])
    def test_zero(self, mock_input):
        with open('number.txt', 'w') as file:
            file.write('0')
        expected_output = "Your Total Number is:  0\n"
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
        with open('number.txt', 'w') as file:
            file.write('0')
        expected_output = "Your Total Number is:  50\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["152"])
    def test_on_range(self, mock_input):
        with open('number.txt', 'w') as file:
            file.write('0')
        expected_output = "Your Total Number is:  152\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["153"])
    def test_over_range(self, mock_input):
        with open('number.txt', 'w') as file:
            file.write('0')
        expected_output = "Your Total Number is:  1\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["304"])
    def test_on_range_double(self, mock_input):
        with open('number.txt', 'w') as file:
            file.write('0')
        expected_output = "Your Total Number is:  152\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["305"])
    def test_over_range_double(self, mock_input):
        with open('number.txt', 'w') as file:
            file.write('0')
        expected_output = "Your Total Number is:  1\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            self.assertEqual(fake_out.getvalue(), expected_output)

    # tests for issue #3

    def test_read_previous_number(self):
        fileName = 'testNumber.txt'
        with open(fileName, 'w') as file:
            file.write("100")
        persistedNumber = readPersistedNumber(fileName)
        self.assertEqual(persistedNumber, 100)

    def test_read_previous_number_non_existent_file(self):
        fileName = 'nonExistentFile.txt'
        persisted_number = readPersistedNumber(fileName)
        self.assertEqual(persisted_number, 0)

    def test_save_current_number(self):
        fileName = 'testNumber.txt'
        persistCurrentNumber(fileName, 50)
        with open(fileName, 'r') as file:
            content = file.read()
        self.assertEqual(content, "50")

    def reset(self):
        fileName = 'testNumber.txt'
        if os.path.exists(fileName):
            os.remove(fileName)

    # tests for issue #4

    @patch('builtins.input', return_value='50')
    def test_main(self, mock_input):
        with open('number.txt', 'w') as file:
            file.write('100')
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            main()
            expected_output = "Your Total Number is:  150\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
