'''
class DataCheckerException

- Exception to raise if anything fails during data checks and nor further information is available.
'''

class DataCheckerException(Exception):
    def __init__(self, data_name):
        # more detailed exceptions
        print(f'\nInitial data checks failed for {data_name}.\nNo further information avaialble.\n')