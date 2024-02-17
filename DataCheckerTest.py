'''
TODO Kommentare
'''

import unittest
import pandas as pd

from datachecker_module.DataChecker import DataChecker

class TestDataChecker(unittest.TestCase):

    def setUp(self):
        self.test_duplicate_data = pd.read_csv('./tests/data/duplicate.csv')
        self.test_missing_data = pd.read_csv('./tests/data/missing.csv')
        self.test_valid_data = pd.read_csv('./tests/data/valid.csv')
        self.test_data_checker = DataChecker(self.test_valid_data, 'Test Data')

    # def test_get_data_frame(self):
    #     self.assertEqual(self.test_data_checker.get_data_frame(), self.test_duplicate_data)
    
    def test_duplicate_value(self):
        self.assertEqual(self.test_data_checker.check_for_duplicate_values(), True)

if __name__ == '__main__':
    unittest.main()