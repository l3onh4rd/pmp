'''
TODO Kommentare
'''

class DataCheckerException(Exception):
    def __init__(self, data_name):
        # more detailed exceptions
        print(f'\n Initial data checks failed for {data_name}. \n No further information avaialble. \n')