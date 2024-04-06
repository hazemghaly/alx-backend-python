#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
import utils
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """function"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


class TestAccessNestedMap (unittest.TestCase):
    """ class testing
    """
    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test function"""
        result = access_nested_map(nested_map, path)
        self.assertRaises(KeyError, result)
