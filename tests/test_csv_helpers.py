import os
import unittest
from helpers.csv_helpers import *

SCRIPT_DIR = os.path.dirname(__file__)

class CSVHelperTests(unittest.TestCase):
    def test_whenCSVIsReadIntoNestedList_thenTheDimensionsAndContentsOfTheListAreCorrect(self):
        nested_list = read_csv_into_nested_list(f'{SCRIPT_DIR}/../fixtures/sample_dht22.csv') 
        self.assertEqual(len(nested_list), 10)
        for l in nested_list:
            self.assertEqual(len(l), 3)
        self.assertListEqual(nested_list[0], ['time', 'temperature', 'humidity'])
        self.assertListEqual(nested_list[4], [1668210604, 19.1, 68.7])

    def test_whenCSVIsReadIntoListOfDataPointDicts_thenTheDimensionsAndContentsOfTheListAreCorrect(self):
        data_points_list = read_csv_into_list_of_data_point_dicts(f'{SCRIPT_DIR}/../fixtures/sample_dht22.csv')
        self.assertEqual(len(data_points_list), 9)
        self.assertDictEqual(data_points_list[0], {'time': 1668209041, 'temperature': 19.1, 'humidity': 69.2})
        
