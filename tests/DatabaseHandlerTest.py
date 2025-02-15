'''
DatabaseHandlerTest class

- unit tests for DatabaseHandler class
'''
import unittest
import sys

sys.path.append('../pmp')
from modules.DatabaseHandler import DatabaseHandler

class DatabaseHandlerTest(unittest.TestCase):

    def setUp(self):
        self.database_handler = DatabaseHandler('./database/pmp.db')
    
    def tearDown(self):
        print('Close Database Connnection')
        self.database_handler.close_connection()

    def test_get_amount_of_table_columns_and_rows(self):
        self.assertEqual(self.database_handler.get_amount_of_table_columns_and_rows(), ['Table train_data has 5 columns and 400 rows.', 'Table ideal_data has 51 columns and 400 rows.', 'Table squared_errors_for_best_fitting_functions has 5 columns and 400 rows.', 'Table avg_delta has 4 columns and 4 rows.'])
        self.assertListEqual(self.database_handler.get_amount_of_table_columns_and_rows(), ['Table train_data has 5 columns and 400 rows.', 'Table ideal_data has 51 columns and 400 rows.', 'Table squared_errors_for_best_fitting_functions has 5 columns and 400 rows.', 'Table avg_delta has 4 columns and 4 rows.'])

if __name__ == '__main__':
    unittest.main()
