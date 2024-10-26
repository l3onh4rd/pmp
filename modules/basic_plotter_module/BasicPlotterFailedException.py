'''
BasicPlotterFailedException class

- Exception to raise if anything fails during the export.
'''

class BasicPlotterFailedException(Exception):
    def __init__(self):
        # more detailed exceptions
        print('\nPlotting and exporting of the data failed.\nMaybe the script was not able to write to your disk. No further information avaialble.\n')