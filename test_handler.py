import unittest
import json
from handler import hello

class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        event = {}
        context = {}
        result = hello(event, context)
        self.assertEqual(result['statusCode'], 200)
        body = json.loads(result['body'])  # Deserialize the JSON string to a Python dict
        self.assertIn('message', body)
        self.assertEqual(body['message'], "Go Serverless v4.0! Your function executed successfully!")

if __name__ == '__main__':
    unittest.main()
