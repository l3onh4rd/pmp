'''
Startpunkt
'''
# import external libraries 
import pandas as pd
import matplotlib.pyplot as plt

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

# calculate the 'Steigung' of each ideal function and train function
    # from point to point -> leads to progress of the value
        # by that you can classify the functions
# calculate the 'Steigung' of each train function

def calculate_m(df_m):
    data_with_m = {}

    for column in df_m.columns:
        if column == 'x':
            continue
        length_column = len(df_m[column])
        m_list = []
        for idx in range(0, length_column):
            if idx == 0:
                continue
                
            delta_y = df_m.loc[idx, column] - df_m.loc[idx - 1, column]
            delta_x = df_m.loc[idx, 'x'] - df_m.loc[idx - 1, 'x']
            m = delta_y / delta_x
            m_list += [m]
        data_with_m[column] = m_list

    return pd.DataFrame(data_with_m)

# 'steigung' of each point
df_m_ideal = calculate_m(df_ideal_import)
df_m_train = calculate_m(df_train_import)

def generate_subset(df_source):
    data_subset = {}
    for column in df_source.columns:
        subset_list = []
        for idx in [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 398]:
            subset_list += [df_source.loc[idx, column]]
        data_subset[column] = subset_list
    
    return pd.DataFrame(data_subset)

# only 10 examples of 'steigung' points
df_subset_ideal = generate_subset(df_m_ideal)
df_subset_train = generate_subset(df_m_train)

# transpose -> each row is now an entry and each column in a feature

df_subset_ideal_T = df_subset_ideal.T
df_subset_train_T = df_subset_train.T

print(df_subset_ideal_T)
print(df_subset_train_T)
