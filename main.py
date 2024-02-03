'''
Startpunkt
'''
# import external libraries 
import pandas as pd

# import own modules
import utils as utility
from classes.datachecker import DataChecker

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

print(df_train_import.isnull().sum().sum())

'''
check and cleanup data
'''

# check
train_data_checker = DataChecker(df_train_import)
print(train_data_checker.check())
train_data_checker.check_for_datatype()

'''
setup
'''