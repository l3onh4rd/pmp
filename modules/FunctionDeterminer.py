'''
FunctionDeterminer class

- class to determine best fitting function between input data and ideal functions
'''

from math import sqrt
import statistics as stat
import pandas as pd
import sys
from sklearn.metrics import root_mean_squared_error

sys.path.append('../pmp')

class FunctionDeterminer:
    def __init__(self, functions, ideal_functions, test_functions):
        self.__sq_error_dict = {'x': functions['x'].values}
        # drop x value column of the data frames immediately as it is not needed
        self.__functions = functions.drop(columns=['x'])
        self.__ideal_functions = ideal_functions.drop(columns=['x'])
        self.__x_values = ideal_functions['x']
        self.__test_functions = test_functions

    # determines best for for all functions
    def determine_best_fit(self):

        # amount of input functions
        column_count = len(self.__functions.columns)
        all_least_sq_errors_min = []
        all_least_sq_errors_idx = []
        best_fitting_functions = []
        # prepare df for least squared errors
        best_fitting_functions_sq_errors_df = pd.DataFrame({'x': [self.__sq_error_dict]})

        print("\nLOG INFO: Start to find the best fitting functions...\n")

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

            # validation with test data (B)
            b_compare_rate = self.b_compare_rate(self, best_fitting_function) / self.__test_functions.shape[0]

            # save best fitting function to a list
            best_fitting_functions += [(function, best_fitting_function, b_compare_rate)]

            # save sq errors to database
            sq_errors_for_database = self.calc_least_sq_errors_for_points(self.__functions[function], self.__ideal_functions[best_fitting_function])
            best_fitting_functions_sq_errors_df[function] = [sq_errors_for_database]
            self.__sq_error_dict[function] = sq_errors_for_database

            # print best fitting function and progress
            print(self.print_best_fitting_function(idx_train, column_count, function, best_fitting_function, b_compare_rate))
        
        # create output for avg delta sqlit
        avg_delta_output = {
            "x": self.__functions.columns.tolist(),
            "test_function": [test_function[0] for test_function in best_fitting_functions],
            "delta": all_least_sq_errors_min,
            "best_fitting_function": [best_fitting[1] for best_fitting in best_fitting_functions]
        }
        
        return best_fitting_functions, pd.DataFrame(self.__sq_error_dict), pd.DataFrame(avg_delta_output)

    # print status message
    @staticmethod
    def print_best_fitting_function(idx, column_count, function, fitting_function, b_compare_rate):
        return f"PROCESSING INFO: ({idx + 1}/{column_count} - {int(((idx + 1)/column_count)*100)}%) Function {function} fits best to {fitting_function} (Data set B compare rate: {b_compare_rate * 100}%)"
    
    # returns a list of squared errors for all values of train and ideal function
    @staticmethod
    def calc_least_sq_errors_for_points(train_column, ideal_column):
        least_sq_errors = []
        # iterate over all points (400 points for each column)
        for element_train, element_ideal in zip(train_column, ideal_column):
            # calculate squared error for each point and save them in a list
            least_sq_errors += [root_mean_squared_error([element_ideal],[element_train])**2]
        
        return least_sq_errors
    
    # counts how many point of the best fitting function can be found in the data test set (max error of the point is sqrt(2))
    @staticmethod
    def b_compare_rate(self, best_fitting_function):
        # how many points can be found in the test data set of the best fitting function
        b_compare_point_counter = 0

        for ideal_x, ideal_y in zip(self.__x_values.to_list(), self.__ideal_functions[best_fitting_function].to_list()):
            # only progress, if the ideal_x value can be found in the test functions
            if (ideal_x in self.__test_functions['x'].values):
                # ideal_x value can be found multiple times in the test functions
                # for each match calculate the mean error
                # if the mean error is lower than sqrt(2) the probability is very high that the point of the ideal function is also in the test point set -> increment the counter
                for idx, row in self.__test_functions[self.__test_functions['x'] == ideal_x].iterrows():
                    if (root_mean_squared_error([ideal_y],[row['y']])**2 < sqrt(2)):
                        b_compare_point_counter += 1
            else:
                continue
        
        # if the counter is near 20% or higher the probability is very high the the ideal function is represented by points in the test data set
        return b_compare_point_counter

