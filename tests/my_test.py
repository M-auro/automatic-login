import unittest
from unittest.mock import patch, Mock
from main import login_to_website

class TestLoginToWebsite(unittest.TestCase):

    @patch('main.requests.Session.post')
    def test_login_successful(self, mock_post):
        # Mock the response to simulate a successful login
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        session = login_to_website('https://example.com/login', 'valid_username', 'valid_password')
        self.assertIsNotNone(session)
        self.assertTrue(mock_post.called)
        self.assertEqual(mock_post.call_args[1]['data'], {'username': 'valid_username', 'password': 'valid_password'})

    @patch('main.requests.Session.post')
    def test_login_failed(self, mock_post):
        # Mock the response to simulate a failed login
        mock_response = Mock()
        mock_response.status_code = 401
        mock_post.return_value = mock_response

        session = login_to_website('https://example.com/login', 'invalid_username', 'invalid_password')
        self.assertIsNone(session)
        self.assertTrue(mock_post.called)
        self.assertEqual(mock_post.call_args[1]['data'], {'username': 'invalid_username', 'password': 'invalid_password'})

if __name__ == '__main__':
    unittest.main()