#!/usr/bin/env python3
"""class to test the access to nested map"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


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


if __name__ == '__main__':
    unittest.main()
