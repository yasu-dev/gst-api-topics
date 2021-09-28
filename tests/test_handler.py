import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('topicId', result['body'])
        self.assertIn('topicType', result['body'])
        self.assertIn('topicTitle', result['body'])
        self.assertIn('topicBody', result['body'])
        self.assertIn('topicImageUrl', result['body'])
        self.assertIn('publish', result['body'])

if __name__ == '__main__':
    unittest.main()
