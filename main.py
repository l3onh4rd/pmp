'''
Startpunkt
'''
# import external libraries 
import pandas as pd

# import own modules
import utils as utility
from classes.datachecker import DataChecker
from exceptions.datacheckexception import DataCheckerError

print('Hello from my Hausarbeit')

# start with a clean up

'''
first copy the latest results to a backup folder (overwrite existing ones)
delete the latest export
'''
# utility.remove_latest_backup()
# utility.backup_latest_export()

'''
import data
'''

# test data import
df_test_import = pd.read_csv('./data/test.csv')
# train data import
df_train_import = pd.read_csv('./data/train.csv')
# ideal data import
df_ideal_import = pd.read_csv('./data/ideal.csv')

'''
check and cleanup data
'''

# check
train_data_checker = DataChecker(df_test_import)
test_data_checker = DataChecker(df_train_import)
ideal_data_checker = DataChecker(df_ideal_import)

for checker in [train_data_checker, test_data_checker, ideal_data_checker]:
    if not checker.check():
        raise DataCheckerError()

'''
setup
'''