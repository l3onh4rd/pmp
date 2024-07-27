'''
BasicPlotter class

- class holds dataframes (pandas) from all data sets
- with that the class can plot all functions or points fromt the data
- creates plots in the export folder
'''

import matplotlib.pyplot as plt

class BasicPlotter:
    def __init__(self, ideal, train, test):
        self.__ideal = ideal
        self.__train = train
        self.__test = test

    TRAIN_EXPORT_FOLDER = './export/train_plots_single/train'
    TEST_EXPORT_FILE = './export/test_plots_single/test.pdf'
    IDEAL_EXPORT_FOLDER = './export/ideal_plots_single/ideal'
    IDEAL_GROUPS_EXPORT_FOLDER = './export/ideal_plots_multiple/multiple'

    '''
        Executes all plots
    '''
    def plot_basics(self):
        self.plot_ideal()
        self.plot_groups_of_ideal()
        self.plot_train()
        self.plot_test()
    
    '''
        Takes all columns (functions) of the train data and plots it.
        Additionally it saves all plots in the export folder as pdf files.
    '''
    def plot_train(self):
        for i in range(1,self.__train.shape[1]):
            plt.plot(self.__train['x'], self.__train['y' + str(i)])
            plt.savefig(self.TRAIN_EXPORT_FOLDER + str(i) + '.pdf')
            # clears plot figure
            plt.clf()

    '''
        Takes all points of the test data and plots it as scatter plot.
        Additionally it saves it in the export folder as pdf file.
    '''
    def plot_test(self):
        sorted_df = self.__test.sort_values(by='x', ascending=True)
        plt.scatter(sorted_df['x'], sorted_df['y'])
        plt.savefig(self.TEST_EXPORT_FILE)
        # clears plot figure
        plt.clf()

    '''
        Takes all columns (functions) of the ideal data and plots it.
        Additionally it saves all plots in the export folder as pdf files.
    '''
    def plot_ideal(self):
        for i in range(1,self.__ideal.shape[1]):
            plt.plot(self.__ideal['x'], self.__ideal['y' + str(i)])
            plt.savefig(self.IDEAL_EXPORT_FOLDER + str(i) + '.pdf')
            # clears plot figure
            plt.clf()

    '''
        To get a better overview of all ideal functions it plots all functions grouped by its scale. Some ideal functions scale their y values from 0 to 1 but others from 20k to -20k.
        The lowest scales are just not visible if you put all ideal functions togethe in one plot.
        For a better compareability masks are created to group function with similiar scale
    '''
    def plot_groups_of_ideal(self):
        # sort dataframe columns by first row
        df_ideal_columns_sorted = self.__ideal[self.__ideal.iloc[0].sort_values().index]

        # create masks to access only columns with a specific range of values like bigger or lower than 1000 or -1000
        # by that the functions are comparable visually in a plot with multiple functions of the same scale
        mask_list = [
            ((df_ideal_columns_sorted.loc[0] <= 1) & (df_ideal_columns_sorted.loc[0] >= 0)) | ((df_ideal_columns_sorted.loc[0] >= -1) & (df_ideal_columns_sorted.loc[0] <= 0)),
            ((df_ideal_columns_sorted.loc[0] <= 5) & (df_ideal_columns_sorted.loc[0] > 1)) | ((df_ideal_columns_sorted.loc[0] >= -5) & (df_ideal_columns_sorted.loc[0] < 1)),
            ((df_ideal_columns_sorted.loc[0] <= 50) & (df_ideal_columns_sorted.loc[0] > 5)) | ((df_ideal_columns_sorted.loc[0] >= -50) & (df_ideal_columns_sorted.loc[0] < -5)),
            ((df_ideal_columns_sorted.loc[0] < 1000) & (df_ideal_columns_sorted.loc[0] > 50)) | ((df_ideal_columns_sorted.loc[0] > -1000) & (df_ideal_columns_sorted.loc[0] < -50)), 
            (df_ideal_columns_sorted.loc[0] > 1000) | (df_ideal_columns_sorted.loc[0] < -1000)
        ]

        # iterate over each mask and then each column to combine plots
        for idx, mask in enumerate(mask_list):
            # convert to mask (pandas Series) to data frame and tranpose it
            mask_transpose = mask.to_frame().T
            # use the mask to get the fitting column name (like y25 or y44)
            column_list = [col for col in mask_transpose.columns if (mask_transpose[col]).all()]
            # for each fitting column print the row into a plot
            for func in column_list:
                plt.plot(self.__ideal['x'], self.__ideal[func])
            # save the combined plot as pdf
            plt.savefig(self.IDEAL_GROUPS_EXPORT_FOLDER + str(idx) + '.pdf')
            # clears plot figure
            plt.clf()
