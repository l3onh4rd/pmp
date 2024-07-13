'''
DatabaseHandler class
'''

import sqlite3

class DatabaseHandler:
    def __init__(self, database_location):
        self.__databse_location = database_location
        self.__conn = sqlite3.connect(self.__databse_location)
    
    def save_df(self, df, table_name):
        df.to_sql(table_name, self.__conn, if_exists='replace', index=False)
    
    def get_amount_of_table_columns_and_rows(self):
        cursor = self.__conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns_count = len(cursor.fetchall())
            print(f"Table '{table_name}' has {columns_count} columns and {row_count} rows.")
    
    def close_connection(self):
        self.__conn.close()

    
