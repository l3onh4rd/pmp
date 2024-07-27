'''
Unit Test class to test DatabaseHandler class
'''

import unittest
import sys
import pandas as pd

sys.path.append('../pmp')
from modules.DatabaseHandler import DatabaseHandler

class FunctionDeterminerTest(unittest.TestCase):

    def setUp(self):
        self.database_handler = DatabaseHandler('./database/pmp.db')
    
    def tearDown(self):
        print('Close Database Conmnection')
        self.database_handler.close_connection()

    def test_get_amount_of_table_columns_and_rows(self):
        self.assertEqual(self.database_handler.get_amount_of_table_columns_and_rows(), ['Table train_data has 5 columns and 400 rows.', 'Table ideal_data has 51 columns and 400 rows.'])

if __name__ == '__main__':
    unittest.main()