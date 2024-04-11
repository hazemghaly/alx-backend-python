#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ class testing
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test function"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test function for exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class json"""

    @parameterized.expand([
        ('http://example.com', {'key': 'value'}),
        ('https://example.com/api/info', {'info_key': 'info_value'}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # mock_response = {'key': 'value'}
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
