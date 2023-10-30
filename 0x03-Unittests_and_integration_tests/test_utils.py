#!/usr/bin/env python3
"""class to test the access to nested map"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
from parameterized import parameterized
import requests


class TestAccessNestedMap(unittest.TestCase):
    """class to test the cases"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test Access nested map with key path."""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test to raise keyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """_summary_

    Args:
                    unittest (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test the json response"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            #requests.get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
