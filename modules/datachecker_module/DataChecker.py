'''
DataChecker class

- class to validate the data
- The class is initialized with a data frame. The class can perform certain checks on the data frame.
- If the data is valid the attribute check_status is set to true. Defaul is false.
'''

from modules.datachecker_module.DataCheckerDuplicateDataException import DataCheckerDuplicateDataException
from modules.datachecker_module.DataCheckerException import DataCheckerException
from modules.datachecker_module.DataCheckerMissingDataException import DataCheckerMissingDataException


class DataChecker:
    def __init__(self, data_frame, data_name):
        self.__data_frame = data_frame
        self.__data_name = data_name
        self.__check_status = False

    def get_data_frame(self):
        return self.__data_frame

    def set_data_frame(self, df):
        self.__data_frame = df

    def get_data_name(self):
        return self.__data_name

    def set_data_name(self, name):
        self.__data_name = name

    def get_check_status(self):
        return self.__check_status
    
    def set_check_status(self, stat):
        self.__check_status = stat

    # check data frame for missing values (null values) - 0 missing values equlas no missing data values
    def check_for_missing_values(self):
        missing_values = self.__data_frame.isnull().sum().sum()
        if missing_values != 0:
            raise DataCheckerMissingDataException(self.get_data_name())
        return missing_values == 0
    
    # checks for duplicate data (duplicate rows) - 0 duplicates equals no duplicate rows
    def check_for_duplicate_values(self):
        # checks only for duplicate rows
        duplicate_row = self.__data_frame.duplicated().sum()
        if duplicate_row != 0:
            raise DataCheckerDuplicateDataException(self.get_data_name())
        return self.__data_frame.duplicated().sum() == 0
    
    # performs checks for duplicates and missing values
    def check(self):
        self.set_check_status(self.check_for_missing_values() and self.check_for_duplicate_values())
        if not self.get_check_status():
            raise DataCheckerException(self.get_data_name())
        

