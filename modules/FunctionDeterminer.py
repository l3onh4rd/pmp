'''
TODO
class to determine which ideal functions fits best
'''

import statistics as stat
import pandas as pd
import sys
from sklearn.metrics import mean_squared_error

from modules.DatabaseHandler import DatabaseHandler
sys.path.append('../pmp')

class FunctionDeterminer:
    def __init__(self, functions, ideal_functions):
        self.__sq_error_dict = {'x': functions['x'].values}
        # drop x value column of the data frames immidiately
        self.__functions = functions.drop(columns=['x'])
        self.__ideal_functions = ideal_functions.drop(columns=['x'])

    def determine_best_fit(self):

        column_count = len(self.__functions.columns)
        all_least_sq_errors_min = []
        all_least_sq_errors_idx = []
        best_fitting_functions = []
        best_fitting_functions_sq_errors_df = pd.DataFrame({'x': [self.__sq_error_dict]})

        print("\nStart to find the best fitting functions...\n")

        # iterate over all train function (4 functions)
        for idx_train, train_column in enumerate(self.__functions.columns):
            all_least_sq_errors = []

            # iterate over all ideal function (50 functions) - for every test function iterate over all ideal functions
            for ideal_column in self.__ideal_functions.columns:
                # get the current column (function) of train function (first for loop)
                train_column_temp = self.__functions[train_column]
                # get the current column (function) of ideal function (second for loop)
                ideal_column_temp = self.__ideal_functions[ideal_column]
                # list for all squared errors (each comparism between all points)
                least_sq_errors = self.calc_least_sq_errors_for_points(train_column_temp, ideal_column_temp)
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

            function = self.__functions.columns[idx_train]
            best_fitting_function = self.__ideal_functions.columns[all_least_sq_errors.index(min_least_sq_error)]

            # save best fitting function to a list
            best_fitting_functions += [(function, best_fitting_function)]

            # save sq errors to database
            sq_errors_for_database = self.calc_least_sq_errors_for_points(self.__functions[function], self.__ideal_functions[best_fitting_function])
            best_fitting_functions_sq_errors_df[function] = [sq_errors_for_database]
            self.__sq_error_dict[function] = sq_errors_for_database

            # print best fitting function and progress
            print(self.print_best_fitting_function(idx_train, column_count, function, best_fitting_function))

        return best_fitting_functions, pd.DataFrame(self.__sq_error_dict)

    @staticmethod
    def print_best_fitting_function(idx, column_count, function, fitting_function):
        return f"({idx + 1}/{column_count} - {int(((idx + 1)/column_count)*100)}%) Function {function} fits best to {fitting_function}"
    
    @staticmethod
    def calc_least_sq_errors_for_points(train_column, ideal_column):
        least_sq_errors = []

        # iterate over all points (400 points for each column)
        for element_train, element_ideal in zip(train_column, ideal_column):
            # calculate squared error for each point and save them in a list
            least_sq_errors += [mean_squared_error([element_ideal],[element_train])]
        
        return least_sq_errors