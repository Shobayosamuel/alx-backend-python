#!/usr/bin/env python3
"""class to test the access to nested map"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
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
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """_summary_

    Args:
                    unittest (_type_): _description_
    """
    def test_memoize(self):
        """_summary_

        Returns:
                _type_: _description_
        """
        class TestClass:
            """_summary_
            """
            def a_method(self):
                """Returns 42"""
                return 42

            @memoize
            def a_property(self):
                """__sumary__: return amethod"""
                return self.a_method()
        new_obj = TestClass()
        with patch.object(new_obj, "a_method") as mock_method:
            mock_method.return_value = 42
            result_1 = new_obj.a_property
            result_2 = new_obj.a_property
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
