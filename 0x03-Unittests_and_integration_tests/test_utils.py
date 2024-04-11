#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from utils import access_nested_map
from parameterized import parameterized
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

    # # def test_access_nested_map_exception(self):
    # #     """test function"""
    # #     self.assertRaises(ValueError)
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test function for exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
