import unittest
from unittest.mock import patch, mock_open
import os

# Предполагаем, что ваш класс IPValidator определен в файле ip_validator.py
from IPV4 import IPValidator


class TestIPValidator(unittest.TestCase):

    def test_valid_IPV_4(self):
        self.assertTrue(IPValidator.valid_IPV_4("192.168.1.1"))
        self.assertTrue(IPValidator.valid_IPV_4("0.0.0.0"))
        self.assertTrue(IPValidator.valid_IPV_4("255.255.255.255"))
        self.assertFalse(IPValidator.valid_IPV_4("256.100.100.100"))
        self.assertFalse(IPValidator.valid_IPV_4("192.168.1."))
        self.assertFalse(IPValidator.valid_IPV_4("192.168.1.1.1"))
        self.assertFalse(IPValidator.valid_IPV_4("abc.def.ghi.jkl"))

    @patch('builtins.open', new_callable=mock_open, read_data='192.168.1.1\n256.100.100.100\n')
    def test_valid_file(self, mock_file):
        valid_ips, invalid_count = IPValidator.valid_file('dummy_file.txt')
        self.assertEqual(valid_ips, ["192.168.1.1"])
        self.assertEqual(invalid_count, 1)

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.input', side_effect=["192.168.1.1"])
    def test_input_and_save_ip(self, mock_input, mock_file):
        IPValidator.input_and_save_ip('test_file.txt')
        mock_file().write.assert_called_once_with("192.168.1.1\n")

    @patch('builtins.open', new_callable=mock_open, read_data='192.168.1.1\n')
    @patch('builtins.print')
    def test_display_menu_valid_ip(self, mock_print, mock_file):
        with patch('builtins.input', side_effect=["1", "test_file.txt", "192.168.1.1", "3"]):
            validator = IPValidator()
            validator.display_menu()
            mock_print.assert_any_call("Адрес 192.168.1.1 сохранен в файл.")
            mock_print.assert_any_call("Выход из программы.")



if __name__ == '__main__':
    unittest.main()
