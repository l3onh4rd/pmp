'''
TODO Kommentare
'''

from modules.datachecker_module.DataCheckerException import DataCheckerException

class DataCheckerMissingDataException(DataCheckerException):
    def __init__(self, data_name):
        # more detailed exceptions
        print(f'\n Initial data checks failed... \n Missing values in {data_name}. \n')