'''
Startpunkt
'''
# import external libraries 
import pandas as pd
import sys

# import own modules
from function_module.FunctionDeterminer import FunctionDeterminer
from plotter_module.BasicPlotter import BasicPlotter
import utils as utility
from datachecker_module.DataChecker import DataChecker

# start with a clean up

'''
first copy the latest results to a backup folder (overwrite existing ones)
delete the latest export
'''
EXPORT_CMD_STR = '--export'
BACKUP_CMD_STR = '--backup'
CMD_ARGUMENTS = sys.argv[1:]
if (len(sys.argv[1:]) >= 1):
    if (BACKUP_CMD_STR in CMD_ARGUMENTS):
        utility.remove_latest_backup()
        utility.backup_latest_export()
        print('Latest export saved as backup...')

'''
import data
'''

# test data import
df_test_import = pd.read_csv('./data/test.csv')
# train data import
df_train_import = pd.read_csv('./data/train.csv')
# ideal data import
df_ideal_import = pd.read_csv('./data/ideal.csv')

# check and cleanup data
train_data_checker = DataChecker(df_train_import, 'Train Data')
test_data_checker = DataChecker(df_test_import, 'Test Data')
ideal_data_checker = DataChecker(df_ideal_import, 'Ideal Data')

for checker in [train_data_checker, test_data_checker, ideal_data_checker]:
    checker.check()
    print(f'Data Check Status - Success {checker.get_check_status()} for {checker.get_data_name()}')

# plot basic data
if (EXPORT_CMD_STR in CMD_ARGUMENTS):
    basic_plotter = BasicPlotter(df_ideal_import, df_train_import, df_test_import)
    basic_plotter.plot_basics()
    print('Basic plots plotted')

# determine best fit function

determiner = FunctionDeterminer(df_train_import, df_ideal_import)
determiner.determine_best_fit()
