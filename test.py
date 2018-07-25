import unittest
import tocamelcase

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(tocamelcase.convet("non_camel_case"), "NonCamelCase")

if __name__ == '__main__':
    unittest.main()
