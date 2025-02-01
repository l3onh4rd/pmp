# import external libraries 
import pandas as pd
import sys
import matplotlib.pyplot as plt

# import own modules
from modules.BokehPlotter import BokehPlotter
from modules.DatabaseHandler import DatabaseHandler
from modules.FunctionDeterminer import FunctionDeterminer
from modules.basic_plotter_module.BasicPlotter import BasicPlotter
import utils as utility
from modules.datachecker_module.DataChecker import DataChecker

EXPORT_CMD_STR = '--export'
BACKUP_CMD_STR = '--backup'
BOKEH_CMD_STR = '--show-bokeh'
CMD_ARGUMENTS = sys.argv[1:]

# check for required export and backup directory
utility.check_for_dirs()

# first copy the latest export to a backup folder (overwriting existing ones), delete the latest export
if (BACKUP_CMD_STR in CMD_ARGUMENTS):
    utility.remove_latest_backup()
    utility.backup_latest_export()
    print('\nLOG INFO: Latest export saved as backup...\n')

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
    print(f'LOG INFO: Data Check Status - Success {checker.get_check_status()} for {checker.get_data_name()}')

# plot basic data
if (EXPORT_CMD_STR in CMD_ARGUMENTS):
    basic_plotter = BasicPlotter(df_ideal_import, df_train_import, df_test_import)
    basic_plotter.plot_basics()
    print('\nLOG INFO: Basic plots plotted')

# save train and ideal to sqlite database
database_handler = DatabaseHandler('./database/pmp.db')
database_handler.save_df(df_train_import, 'train_data')
database_handler.save_df(df_ideal_import, 'ideal_data')

# determine best fitting function
determiner = FunctionDeterminer(df_train_import, df_ideal_import)
best_fitting, sq_error_df, avg_delta_df = determiner.determine_best_fit()
# save all squared errors for best fitting functions to sqlite
database_handler.save_df(sq_error_df, 'squared_errors_for_best_fitting_functions')
# save all average deltas for best fitting functions to sqlite
database_handler.save_df(avg_delta_df, 'avg_delta')

utility.create_result_csv(best_fitting)
print('\nLOG INFO: Result csv file created')

# print database meta information
print('\nDATABASE INFO:')
for table_info in database_handler.get_amount_of_table_columns_and_rows(): print('\t' + table_info)
# close database connection
database_handler.close_connection()

# create bokeh plots
bokeh_plotter = BokehPlotter(df_ideal_import, df_train_import, sq_error_df, BOKEH_CMD_STR in CMD_ARGUMENTS)
bokeh_plotter.generate_plots()

print('LOG INFO: Bokeh plots created')
print('LOG INFO: Finished')
