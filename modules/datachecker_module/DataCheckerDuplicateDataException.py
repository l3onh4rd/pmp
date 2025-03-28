'''
class DataCheckerDuplicateDataException

- Exception to raise if data is not valid. Exception raises if any duplicate data is part of a data frame.
'''

from modules.datachecker_module.DataCheckerException import DataCheckerException

class DataCheckerDuplicateDataException(DataCheckerException):
    def __init__(self, data_name):
        # more detailed exceptions
        print(f'\nInitial data checks failed...\nDuplicate values in {data_name}.\n')