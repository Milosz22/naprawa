import unittest
from App.app_functions import *
from Christofides.christofides import *


class MyTestCase(unittest.TestCase):
    def test_load_graph_from_file_1(self):
        # Given
        filepath = "test_load_1.txt"
        expected_result = {"0": {"1": 1, "2": 2}, "1": {"0": 1, "2": 2}, "2": {"0": 2, "1": 2}}

        # When
        result = load_graph_from_file(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_load_graph_from_file_2(self):
        # Given
        filepath = "test_load_2.txt"
        expected_result = {"0": {"1": 1, "2": 2, "3": 3}, "1": {"0": 1, "2": 2, "3": 3}, "2": {"0": 2, "1": 2, "3": 3},
                           "3": {"0": 3, "1": 3, "2": 3}}

        # When
        result = load_graph_from_file(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_load_graph_from_file_3(self):
        # Given
        filepath = "test_load_3.txt"
        expected_result = {"0": {"1": 1}, "1": {"0": 1}}

        # When
        result = load_graph_from_file(filepath)

        # Then
        self.assertEqual(expected_result, result)




if __name__ == '__main__':
    unittest.main()
