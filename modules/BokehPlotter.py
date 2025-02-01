'''
BokehPlotter class

- processes bokeh plots
- handles creation and export of the bokeh plots
'''

from bokeh.models import CustomJS, ColumnDataSource, Select, Column
from bokeh.plotting import figure, save, show
from bokeh.io import output_file
import numpy as np

class BokehPlotter:
    def __init__(self, df_ideal, df_train, df_sq_error, show):
        # set data frame variables and drop x value column of the data frames immediately as it is not needed
        self.__df_ideal = df_ideal.drop(columns=['x'])
        self.__df_train = df_train.drop(columns=['x'])
        self.__df_sq_error = df_sq_error.drop(columns=['x'])
        # variable to show the plots during execution of the script or not (avoid opening the browser tabs)
        self.__show = show

    # call function to create the plots, save to exports and show them if necessary
    def generate_plots(self):
        # ideal functions
        output_file("./export/bokeh_plots/ideal_functions_bokeh_plot.html", mode="inline")
        ideal_bokeh_plot = self.generate_ideal_bokeh_plot()
        save(ideal_bokeh_plot)
        # train functions
        output_file("./export/bokeh_plots/train_functions_bokeh_plot.html", mode="inline")
        train_bokeh_plot = self.generate_train_bokeh_plot()
        save(train_bokeh_plot)
        # squared errors for best fitting functions
        output_file("./export/bokeh_plots/sq_errors_functions_bokeh_plot.html", mode="inline")
        error_bokeh_plot = self.generate_sq_error_bokeh_plot()
        save(error_bokeh_plot)
        # show the plots in the browser if cmd flag is set
        if self.__show:
            show(ideal_bokeh_plot)
            show(train_bokeh_plot)
            show(error_bokeh_plot)

    # generate bokeh plot for ideal functions
    def generate_ideal_bokeh_plot(self):
        ideal_bokeh_plot = figure(title="Ideal Functions", y_axis_label="y-Values", x_axis_label="x-Values", width=1000)
        # generate x values for the plot
        x = self.generate_x_values(-20, 20, 400)
        # data for plot
        data_dict = {}
        # columns of the data frame
        columns_list = self.__df_ideal.columns.to_list()

        # create an entry in the data dict for each column with its values, set the correct key
        for col in columns_list:
            data_dict[f'Funktion - {col}'] = {"x": x, "y": self.__df_ideal[col].to_list()}

        # rename columns for better readability
        for idx, col_el in enumerate(columns_list): columns_list[idx] = f'Funktion - {col_el}'

        # create chart and select first element of the dictionary
        source = ColumnDataSource(data_dict['Funktion - y1'])
        # set first element as line plot
        ideal_bokeh_plot.line('x', 'y', line_width = 4, source = source)

        # callback for updating the selected element from the dictionary - changes the y-values (function) depending on dropdown selection
        callback = CustomJS(args = {'source': source, 'data': data_dict},
        code = """source.data = data[cb_obj.value]; """)

        # create dropdown and link callback
        select = Select(title = 'Choose', value = 'Funktion - y1', options = columns_list, width=1000)
        select.js_on_change('value', callback)

        # return plot element with dropdown and plot (as column layout)
        return Column(select, ideal_bokeh_plot)

    # generate bokeh plot for train functions
    def generate_train_bokeh_plot(self):
        train_bokeh_plot = figure(title="Train Functions", y_axis_label="y-Values", x_axis_label="x-Values", width=1000)
        # generate x values for the plot
        x = self.generate_x_values(-20, 20, 400)
        # data for plot
        data_dict = {}
        # columns of the data frame
        columns_list = self.__df_train.columns.to_list()

        # create an entry in the data dict for each column with its values, set the correct key
        for col in columns_list:
            data_dict[f'Funktion - {col}'] = {"x": x, "y": self.__df_train[col].to_list()}

        # rename columns for better readability
        for idx, col_el in enumerate(columns_list): columns_list[idx] = f'Funktion - {col_el}'

        # create chart and select first element of the dictionary
        source = ColumnDataSource(data_dict['Funktion - y1'])
        # set first element as line plot
        train_bokeh_plot.line('x', 'y', line_width = 4, source = source)

        # callback for updating the selected element from the dictionary - changes the y-values (function) depending on dropdown selection
        callback = CustomJS(args = {'source': source, 'data': data_dict},
        code = """source.data = data[cb_obj.value]; """)

        # create dropdown and link callback
        select = Select(title = 'Choose', value = 'Funktion - y1', options = columns_list, width=1000)
        select.js_on_change('value', callback)

        # return plot element with dropdown and plot (as column layout)
        return Column(select, train_bokeh_plot)

    # generate bokeh plot for squared errors of best fitting functions
    def generate_sq_error_bokeh_plot(self):
        sq_error_bokeh_plot = figure(title="Squared Errors", y_axis_label="y-Values", x_axis_label="x-Values", width=1000)
        # generate x values for the plot
        x = self.generate_x_values(-20, 20, 400)
        # data for plot
        data_dict = {}
        # columns of the data frame
        columns_list = self.__df_sq_error.columns.to_list()

        # create an entry in the data dict for each column with its values, set the correct key
        for col in columns_list:
            data_dict[f'Funktion - {col}'] = {"x": x, "top": self.__df_sq_error[col].to_list()}

        # rename columns for better readability
        for idx, col_el in enumerate(columns_list): columns_list[idx] = f'Funktion - {col_el}'

        # create chart and select first element of the dictionary
        source = ColumnDataSource(data_dict['Funktion - y1'])
        # set first element as bar plot
        sq_error_bokeh_plot.vbar('x', 'top', width=0.9, source = source)

        # callback for updating the selected element from the dictionary - changes the y-values (function) depending on dropdown selection
        callback = CustomJS(args = {'source': source, 'data': data_dict},
        code = """source.data = data[cb_obj.value]; """)

        # create dropdown and link callback
        select = Select(title = 'Choose', value = 'Funktion - y1', options = columns_list, width=1000)
        select.js_on_change('value', callback)

        # return plot element with dropdown and plot (as column layout)
        return Column(select, sq_error_bokeh_plot)

    # generate an np array with a start and end values, steps defines the equally distrubuted amount of values
    # return python list
    def generate_x_values(self, start, end, steps):
        return np.linspace(start, end, steps).tolist()