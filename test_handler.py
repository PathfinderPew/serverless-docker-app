import unittest
from handler import hello

class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        event = {}
        context = {}
        result = hello(event, context)
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('message', result['body'])

if __name__ == '__main__':
    unittest.main()