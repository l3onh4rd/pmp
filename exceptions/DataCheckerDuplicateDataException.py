'''
TODO Kommentare
'''

from exceptions.DataCheckerException import DataCheckerException


class DataCheckerDuplicateDataException(DataCheckerException):
    def __init__(self, data_name):
        # more detailed exceptions
        print(f'\n Initial data checks failed... \n Duplicate values in {data_name}. \n')