'''
Unit Test class to test FunctionDeterminer class
'''

import unittest
import sys
import pandas as pd

sys.path.append('../pmp')
from function_module.FunctionDeterminer import FunctionDeterminer


class TestDataChecker(unittest.TestCase):

    def setUp(self):
        self.function_determiner = FunctionDeterminer(pd.read_csv('./tests/data/test_train.csv'), pd.read_csv('./tests/data/test_ideal.csv'))
    
    def test_print_best_fitting_function(self):
        self.assertEqual(self.function_determiner.print_best_fitting_function(1, 4, "y2", "y5"), "(2/4 - 50%) Function y2 fits best to y5")

if __name__ == '__main__':
    unittest.main()