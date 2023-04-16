import unittest
import json
from app import app

class TestTextAnalysisServices(unittest.TestCase):

    def test_analyze_text_valid_word_count(self):
        with app.test_client() as client:
            # Test with valid input
            payload = {"service": "word-count", "text": "This is a test."}
            response = client.post('/analyze-text', data=json.dumps(payload), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn('result', json.loads(response.data))

    def test_analyze_text_valid_bigram(self):
        with app.test_client() as client:
            # Test with valid input
            payload = {"service": "bigram", "text": "This is a test."}
            response = client.post('/analyze-text', data=json.dumps(payload), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn('result', json.loads(response.data))

    def test_analyze_text_missing_text(self):
        with app.test_client() as client:
            # Test with missing text
            payload = {"service": "word-count"}
            response = client.post('/analyze-text', data=json.dumps(payload), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', json.loads(response.data))

    def test_analyze_text_missing_service(self):
        with app.test_client() as client:
            # Test with missing service
            payload = {"text": "This is a test."}
            response = client.post('/analyze-text', data=json.dumps(payload), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', json.loads(response.data))

    def test_analyze_text_invalid_service(self):
        with app.test_client() as client:
            # Test with invalid service
            payload = {"service": "invalid_service", "text": "This is a test."}
            response = client.post('/analyze-text', data=json.dumps(payload), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', json.loads(response.data))
    
    def test_analyze_text_invalid_text(self):
        with app.test_client() as client:
            # Test with invalid text
            payload = {"service": "bigram", "text": 8127489302}
            response = client.post('/analyze-text', data=json.dumps(payload), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertIn('error', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()