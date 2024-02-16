'''
Startpunkt
'''
# import external libraries 
import pandas as pd
import matplotlib.pyplot as plt

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

'''
check and cleanup data
'''

# check
train_data_checker = DataChecker(df_train_import, 'Train Data')
test_data_checker = DataChecker(df_test_import, 'Test Data')
ideal_data_checker = DataChecker(df_ideal_import, 'Ideal Data')

for checker in [train_data_checker, test_data_checker, ideal_data_checker]:
    checker.check()
    print(f'Data Check Status - Success {checker.get_check_status()} for {checker.get_data_name()}')

# plot single
for i in range(1,df_ideal_import.shape[1]):
    plt.plot(df_ideal_import['x'], df_ideal_import['y' + str(i)])
    plt.savefig('./export/ideal_plots_single/ideal' + str(i) + '.pdf')
    plt.clf()

# plot multiple together
    # Is it possible to plot everything in one plot?
    # Sort all y datas columnwise
    # plot sets with nearly equal values
        # like 0 -10, 10 to 100, 1000 to 10000

# sort dataframe columns by first row
df_ideal_columns_sorted = df_ideal_import[df_ideal_import.iloc[0].sort_values().index]
# print(df_ideal_columns_sorted)

plt.plot(df_ideal_import['x'], df_ideal_import['y25'])
plt.plot(df_ideal_import['x'], df_ideal_import['y24'])
plt.plot(df_ideal_import['x'], df_ideal_import['y30'])
plt.plot(df_ideal_import['x'], df_ideal_import['y28'])
plt.plot(df_ideal_import['x'], df_ideal_import['y21'])
plt.plot(df_ideal_import['x'], df_ideal_import['y29'])
plt.plot(df_ideal_import['x'], df_ideal_import['y26'])

plt.plot(df_ideal_import['x'], df_ideal_import['y23'])
plt.plot(df_ideal_import['x'], df_ideal_import['y22'])
plt.plot(df_ideal_import['x'], df_ideal_import['y27'])
plt.show()

'''
setup
'''