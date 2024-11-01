import unittest
import IPV4
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
address = "103.21.244.0"
class IPV_4_test(unittest.TestCase):
    def test_IPV_4_pattern(self):
        if not self.assertRegex(address,pattern)


if __name__ == '__main__':
    unittest.main()
