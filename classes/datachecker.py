'''
Kommentar
'''

class DataChecker:
    def __init__(self, data_frame):
        self.__data_frame = data_frame

    # TODO necessary?
    def get_data_frame(self):
        return self.__data_frame
    
    # TODO necessary?
    def set_creator(self, df):
        self.__data_frame = df

    def check_for_missing_values(self):
        return self.__data_frame.isnull().sum().sum() == 0
    
    def check_for_datatype(self):
        print(len(self.__data_frame.axes[1]))
        print(self.__data_frame.dtypes[self.__data_frame.dtypes == 'float64'])
    
    def check(self):
        return self.check_for_missing_values()

