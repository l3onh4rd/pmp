'''
class DataCheckerMissingDataException

- Exception to raise if data is not valid. Exception raises if any data frame has missing values.
'''

from modules.datachecker_module.DataCheckerException import DataCheckerException

class DataCheckerMissingDataException(DataCheckerException):
    def __init__(self, data_name):
        # more detailed exceptions
        print(f'\nInitial data checks failed... \nMissing values in {data_name}.\n')