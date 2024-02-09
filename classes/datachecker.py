'''
TODO Kommentar
'''

class DataChecker:
    def __init__(self, data_frame):
        self.__data_frame = data_frame

    # TODO necessary?
    def get_data_frame(self):
        return self.__data_frame
    
    # TODO necessary?
    def set_data_frame(self, df):
        self.__data_frame = df

    def check_for_missing_values(self):
        # TODO explain comment
        return self.__data_frame.isnull().sum().sum() == 0
    
    def check_for_duplicate_values(self):
        # TODO explain comment
        # checks only for duplicate rows
        return self.__data_frame.duplicated().sum() == 0
    
    def check(self):
        return self.check_for_missing_values() and self.check_for_duplicate_values()

