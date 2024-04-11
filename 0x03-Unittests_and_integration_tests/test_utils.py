#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ class testing
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ({}, ("a",), "Key not found: 'a'"),
            ({"a": 1}, ("a", "b"), "Key not found: 'b'")
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test function"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    def test_access_nested_map_exception(self):
        """test function"""
        self.assertRaises(KeyError)
