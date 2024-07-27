'''
Unit Test class to test DataChecker class
'''

import unittest
import pandas as pd
import sys

sys.path.append('../pmp')
from modules.datachecker_module.DataChecker import DataChecker
from modules.datachecker_module.DataCheckerMissingDataException import DataCheckerMissingDataException
from modules.datachecker_module.DataCheckerDuplicateDataException import DataCheckerDuplicateDataException

class TestDataChecker(unittest.TestCase):

    def setUp(self):
        self.test_duplicate_data = pd.read_csv('./tests/data/duplicate.csv')
        self.test_missing_data = pd.read_csv('./tests/data/missing.csv')
        self.test_valid_data = pd.read_csv('./tests/data/valid.csv')
        self.test_data_checker_valid = DataChecker(self.test_valid_data, 'Test Valid Data')
        self.test_data_checker_missing = DataChecker(self.test_missing_data, 'Test Missing Data')
        self.test_data_checker_duplicate = DataChecker(self.test_duplicate_data, 'Test Duplicate Data')
    
    def test_valid_data_duplicate(self):
        self.assertEqual(self.test_data_checker_valid.check_for_duplicate_values(), True)

    def test_valid_data_missing(self):
        self.assertEqual(self.test_data_checker_valid.check_for_missing_values(), True)
    
    def test_valid_data_check_status(self):
        self.test_data_checker_valid.check()
        self.assertEqual(self.test_data_checker_valid.get_check_status(), True)

    def test_missing_value_exception(self):
        with self.assertRaises(DataCheckerMissingDataException) as test_context:
            self.test_data_checker_missing.check_for_missing_values()
        self.assertEqual(str(test_context.exception), 'Test Missing Data')

    def test_duplicate_value_exception(self):
        with self.assertRaises(DataCheckerDuplicateDataException) as test_context:
            self.test_data_checker_duplicate.check_for_duplicate_values()
        self.assertEqual(str(test_context.exception), 'Test Duplicate Data')

if __name__ == '__main__':
    unittest.main()