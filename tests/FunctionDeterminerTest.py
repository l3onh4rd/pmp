'''
FunctionDeterminerTest class

- unit tests for FunctionDeterminer class
'''
import unittest
import sys
import pandas as pd

sys.path.append('../pmp')
from modules.FunctionDeterminer import FunctionDeterminer

class FunctionDeterminerTest(unittest.TestCase):

    def setUp(self):
        self.function_determiner = FunctionDeterminer(pd.read_csv('./tests/data/test_train.csv'), pd.read_csv('./tests/data/test_ideal.csv'), pd.read_csv('./tests/data/b_test.csv'))
    
    def test_print_best_fitting_function(self):
        self.assertEqual(self.function_determiner.print_best_fitting_function(1, 4, "y2", "y5", 0.35), "PROCESSING INFO: (2/4 - 50%) Function y2 fits best to y5 (Data set B compare rate: 35.0%)")

    def test_calc_least_sq_errors_for_points(self):
        self.assertEqual(self.function_determiner.calc_least_sq_errors_for_points([1,2,3,4,5],[6,3,8,5,9]), [25.0,1.0,25.0,1.0,16.0])

    def test_determine_best_fit(self):
        self.assertEqual(self.function_determiner.determine_best_fit()[0], [('y1', 'y2', 0.0),('y2', 'y1', 1.0)])

if __name__ == '__main__':
    unittest.main()
