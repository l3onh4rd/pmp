'''
DatabaseHandler class
- initialize a sqlite connection
- saves data to database (.db) file
'''

import sqlite3
import pandas as pd

class DatabaseHandler:
    def __init__(self, database_location):
        self.__databse_location = database_location
        self.__conn = sqlite3.connect(self.__databse_location)
    
    # takes data frame and saves it to the local sqlite db file
    def save_df(self, df: pd.DataFrame, table_name):
        df.to_sql(table_name, self.__conn, if_exists='replace', index=False)
    
    # return a list of strings with table name, rows and columns amount
    def get_amount_of_table_columns_and_rows(self):
        output_list = []
        cursor = self.__conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # for each table get the amount of columns and rows
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns_count = len(cursor.fetchall())
            output_list += [f"Table {table_name} has {columns_count} columns and {row_count} rows."]
        
        return output_list
    
    def close_connection(self):
        self.__conn.close()
