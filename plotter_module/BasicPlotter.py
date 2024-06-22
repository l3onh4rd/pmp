'''
TODO
class plot basic functions
main purpose is to exclude the code from the main script
'''

import matplotlib.pyplot as plt

class BasicPlotter:
    def __init__(self, ideal, train, test):
        self.__ideal = ideal
        self.__train = train
        self.__test = test

    def plot_basics(self):
        self.plot_ideal()
        self.plot_groups_of_ideal()
        self.plot_train()
        self.plot_test()
    
    def plot_train(self):
        for i in range(1,self.__train.shape[1]):
            plt.plot(self.__train['x'], self.__train['y' + str(i)])
            plt.savefig('./export/train_plots_single/train' + str(i) + '.pdf')
            plt.clf()

    def plot_test(self):
        sorted_df = self.__test.sort_values(by='x', ascending=True)
        plt.scatter(sorted_df['x'], sorted_df['y'])
        plt.savefig('./export/test_plots_single/test.pdf')
        plt.clf()

        

    def plot_ideal(self):
        for i in range(1,self.__ideal.shape[1]):
            plt.plot(self.__ideal['x'], self.__ideal['y' + str(i)])
            plt.savefig('./export/ideal_plots_single/ideal' + str(i) + '.pdf')
            plt.clf()

    def plot_groups_of_ideal(self):
        # sort dataframe columns by first row
        df_ideal_columns_sorted = self.__ideal[self.__ideal.iloc[0].sort_values().index]

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
                plt.plot(self.__ideal['x'], self.__ideal[func])
            # save the combined plot as pdf
            plt.savefig('./export/ideal_plots_multiple/multiple' + str(idx) + '.pdf')
            plt.clf()
