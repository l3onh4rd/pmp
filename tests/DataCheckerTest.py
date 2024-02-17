'''
TODO Kommentare
'''

import unittest
import pandas as pd

from classes.datachecker import DataChecker

class TestDataChecker(unittest.TestCase):

    test_duplicate_data = pd.read_csv('./tests/data/duplicate.csv')
    test_missing_data = pd.read_csv('./tests/data/missing.csv')
    # test_data_checker = DataChecker(test_duplicate_data, 'Test Data')

    # def test_get_data_frame(self):
    #     self.assertEqual(test_data_checker.get_data_frame(), test_duplicate_data)

if __name__ == '__main__':
    unittest.main()