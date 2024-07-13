'''
TODO
class to determine which ideal functions fits best
'''

import statistics as stat
from sklearn.metrics import mean_squared_error

class FunctionDeterminer:
    def __init__(self, functions, ideal_functions):
        self.__functions = functions
        self.__ideal_functions = ideal_functions

    def determine_best_fit(self):
        # drop x value column of the data frames from the imports
        alt_ideal = self.__ideal_functions.drop(columns=['x'])
        alt_train = self.__functions.drop(columns=['x'])

        column_count = len(alt_train.columns)
        all_least_sq_errors_min = []
        all_least_sq_errors_idx = []

        print("\nStart to find the best fitting functions...\n")

        # iterate over all train function (4 functions)
        for idx_train, train_column in enumerate(alt_train.columns):
            all_least_sq_errors = []

            # iterate over all ideal function (50 functions) - for every test function iterate over all ideal functions
            for ideal_column in alt_ideal.columns:
                # get the current column (function) of train function (first for loop)
                train_column_temp = alt_train[train_column]
                # get the current column (function) of ideal function (second for loop)
                ideal_column_temp = alt_ideal[ideal_column]
                # list for all squared errors (each comparism between all points)
                least_sq_errors = []

                # iterate over all points (400 points for each column)
                for element_train, element_ideal in zip(train_column_temp, ideal_column_temp):
                    # calculate squared error for each point and save them in a list
                    least_sq_errors += [mean_squared_error([element_ideal],[element_train])]

                # for each ideal function compared to the train function (400 points -> 400 least_sq_errors) save the mean calculated over the 400 points
                all_least_sq_errors += [stat.mean(least_sq_errors)]

            # for each train function the loop calucalted all squared errors compared to each ideal function and for all points
            # now the mean for all squared errors is available as a list
            # the lowest value shows the best fitting ideal function to the current train function
            min_least_sq_error = min(all_least_sq_errors)
            # save all lowest least squared erros as list (for each train function one min value)
            all_least_sq_errors_min += [min_least_sq_error]
            # save all lowest least squared erros as list (for each train function one min value)
            all_least_sq_errors_idx += [all_least_sq_errors.index(min_least_sq_error)]

            # print progress in percent
            print(f"{int(((idx_train + 1)/column_count)*100)} % progress...")

        # print which function fits to which ideal function
        for idx_of_list, idx in enumerate(all_least_sq_errors_idx):
            print('Function ' + alt_train.columns[idx_of_list] + ' fits best to ' + alt_ideal.columns[idx])