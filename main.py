'''
Startpunkt
'''
# import external libraries 
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

# import own modules
import utils as utility
from datachecker_module.DataChecker import DataChecker

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

# check data
train_data_checker = DataChecker(df_train_import, 'Train Data')
test_data_checker = DataChecker(df_test_import, 'Test Data')
ideal_data_checker = DataChecker(df_ideal_import, 'Ideal Data')

for checker in [train_data_checker, test_data_checker, ideal_data_checker]:
    checker.check()
    print(f'Data Check Status - Success {checker.get_check_status()} for {checker.get_data_name()}')

# plot single test
sorted_df = df_test_import.sort_values(by='x', ascending=True)
plt.scatter(sorted_df['x'], sorted_df['y'])
plt.savefig('./export/test_plots_single/test.pdf')
plt.clf()

# plot single train
for i in range(1,df_train_import.shape[1]):
    plt.plot(df_train_import['x'], df_train_import['y' + str(i)])
    plt.savefig('./export/train_plots_single/train' + str(i) + '.pdf')
    plt.clf()

# plot single ideal
for i in range(1,df_ideal_import.shape[1]):
    plt.plot(df_ideal_import['x'], df_ideal_import['y' + str(i)])
    plt.savefig('./export/ideal_plots_single/ideal' + str(i) + '.pdf')
    plt.clf()

# plot multiple ideal

# sort dataframe columns by first row
df_ideal_columns_sorted = df_ideal_import[df_ideal_import.iloc[0].sort_values().index]

# create masks to access only columns with a specific range of values like bigger or lower than 1000 or -1000
# by that the functions are comparable in a plot with multiple functions of the same scale
mask_4 = (df_ideal_columns_sorted.loc[0] > 1000) | (df_ideal_columns_sorted.loc[0] < -1000)
mask_3 = ((df_ideal_columns_sorted.loc[0] < 1000) & (df_ideal_columns_sorted.loc[0] > 50)) | ((df_ideal_columns_sorted.loc[0] > -1000) & (df_ideal_columns_sorted.loc[0] < -50))
mask_2 = ((df_ideal_columns_sorted.loc[0] <= 50) & (df_ideal_columns_sorted.loc[0] > 5)) | ((df_ideal_columns_sorted.loc[0] >= -50) & (df_ideal_columns_sorted.loc[0] < -5))
mask_1 = ((df_ideal_columns_sorted.loc[0] <= 5) & (df_ideal_columns_sorted.loc[0] > 1)) | ((df_ideal_columns_sorted.loc[0] >= -5) & (df_ideal_columns_sorted.loc[0] < 1))
mask_0 = ((df_ideal_columns_sorted.loc[0] <= 1) & (df_ideal_columns_sorted.loc[0] >= 0)) | ((df_ideal_columns_sorted.loc[0] >= -1) & (df_ideal_columns_sorted.loc[0] <= 0))

mask_list = [mask_0, mask_1, mask_2, mask_3, mask_4]

# iterate over each mask and then each column to combine plots
for idx, mask in enumerate(mask_list):
    # convert to mask (pandas Series) to data frame and tranpose it
    mask_transpose = mask.to_frame().T
    # use the mask to get the fitting column name (like y25 or y44)
    column_list = [col for col in mask_transpose.columns if (mask_transpose[col]).all()]
    # for each fitting column print the row into a plot
    for func in column_list:
        plt.plot(df_ideal_import['x'], df_ideal_import[func])
    # save the combined plot as pdf
    plt.savefig('./export/ideal_plots_multiple/multiple' + str(idx) + '.pdf')
    plt.clf()

'''
setup
'''

# alternative calculation

alt_ideal = df_ideal_import.drop(columns=['x'])
alt_train = df_train_import.drop(columns=['x'])

all_least_sq_errors_min = []
all_least_sq_errors_idx = []
# this saves all gaps from all points from each ideal fructions to each train function
all_least_sq_erros_dump = []
for idx_train, train_column in enumerate(alt_train.columns):
    all_least_sq_errors = []
    all_least_sq_erros_dump += [[]]
    for ideal_column in alt_ideal.columns:
        train_column_temp = alt_train[train_column]
        ideal_column_temp = alt_ideal[ideal_column]
        # print(train_column_temp)
        # print(ideal_column_temp)
        least_sq_errors = []
        for element_train, element_ideal in zip(train_column_temp, ideal_column_temp):
            # print(element_train)
            # print(element_ideal)
            # eventuell mit from sklearn.metrics import mean_squared_error
            # mean_squared_error_sklearn = mean_squared_error(actual_values, predicted_values)
            least_sq_errors += [(element_train - element_ideal) ** 2]
            # print(least_sq_errors)
        all_least_sq_errors += [stat.mean(least_sq_errors)]
        all_least_sq_erros_dump[idx_train] += [least_sq_errors]
        # print(all_least_sq_errors)
    all_least_sq_errors_min += [min(all_least_sq_errors)]
    all_least_sq_errors_idx += [all_least_sq_errors.index(min(all_least_sq_errors))]

print('#####')
print(all_least_sq_errors_min)
print(all_least_sq_errors_idx)

for idx_of_list, idx in enumerate(all_least_sq_errors_idx):
    print(alt_ideal.columns[idx])
    # print all squared gaps from the matched function
    # print('+++++')
    # print(all_least_sq_erros_dump[idx_of_list][idx])

print('\n stats for dump')
print(len(all_least_sq_erros_dump))
print(len(all_least_sq_erros_dump[0]))
print(len(all_least_sq_erros_dump[0][0]))
