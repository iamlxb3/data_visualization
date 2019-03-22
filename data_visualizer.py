'''
A data visualizer
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.plotting import radviz
from pandas.plotting import parallel_coordinates

__author__ = ''
__version__ = ''


def _check_df(data):
    '''check whether the data is pandas dataframe'''

    if not isinstance(data, pd.DataFrame):
        raise Exception("Error! data must be pandas data frame!")


def _set_x_y_label(ax, x_label, y_label):
    '''set x and y label'''
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)


def _set_title(ax, title):
    '''set title'''
    if title:
        ax.set_title(title)


class DataVisualizer(object):
    '''
    A visualizer for analysing and plotting data used for Machine Learning purpose.
    It can be viewed as a matplotlib and seaborn wrapper.
    '''

    def __init__(self):
        pass

    def box_plot(self,
                 data=None,
                 x=None,
                 y=None,
                 x_label=None,
                 y_label=None,
                 x_label_rotation=None,
                 bottom_room=None,
                 title=None,
                 linewidth=1,
                 orient='v',
                 plot_margin_ajust=(0, 1, 1, 0),
                 save_path=None,
                 is_show=True):
        # TODO (1.) add hue https://seaborn.pydata.org/generated/seaborn.boxplot.html
        # TODO (2.) incorporate orient
        # TODO (3.) explore col in sns.boxplot
        # TODO (4.) check plot_margin_ajust

        """wrapper for seaborn box_plot
        args:
        plot_margin_ajust: left=None, bottom=None, right=None, top=None
        x

        Example:
        --------------------------BASIC--------------------------
        >>> v1 = DataVisualizer()
        >>> v1.box_plot(data=data, x='feature1', y='target_value')


        """
        _check_df(data)

        if (x is None and y is not None) or (y is None and x is not None):
            raise Exception("You must input x and y at the same time!")
        # (1.) when x and y are constrained
        elif x and y:
            # check validation of x,y
            keys = set(data.keys())
            if x not in keys:
                raise Exception("please check x! x should be the key of the DataFrame")
            if y not in keys:
                raise Exception("please check y! y should be the key of the DataFrame")
            ax = sns.boxplot(x=x, y=y, data=data, linewidth=linewidth, orient=orient)
        # (2.) x -> all original attributors of data frame, y -> values of attributors
        else:
            ax = sns.boxplot(data=data, linewidth=linewidth, orient=orient)

        # x_label_rotation
        if x_label_rotation:
            plt.xticks(rotation=x_label_rotation)
        #

        # adjust margins
        # plt.gcf().subplots_adjust(*plot_margin_ajust)
        #

        # set x_y_label
        _set_x_y_label(ax, x_label, y_label)

        # set title
        _set_title(ax, title)

        if save_path:
            plt.savefig(save_path)

        if is_show:
            plt.show()

    def histogram_plot(self, data=None, single_attributor=None, is_split_plot=True,
                       x_label=None, y_label=None, title=None):
        '''wrapper for seaborn distplot'''

        def _single_plot(data, attributor, is_split_plot):
            # check the type of the df
            attr_data = data[attributor]
            if is_numeric_dtype(attr_data):
                ax = sns.distplot(data[attributor])
                plt.xlabel(attributor)
                if is_split_plot:
                    plt.show()
                return ax
            else:
                raise Exception("Attributor {} is not valid for histogram plot".format(attributor))

        # TODO, add is_single_attributor
        if single_attributor:
            ax = _single_plot(data, single_attributor, True)

        if not single_attributor:
            _check_df(data)
            for attributor in data:
                # TODO set x,y labels, title for each histogram plot
                ax = _single_plot(data, attributor, is_split_plot)

            if not is_split_plot:
                # set x_y_label
                _set_x_y_label(ax, x_label, y_label)

                # set title
                _set_title(ax, title)

                plt.show()

    def scatter_plot(self, data=None, plot_margin_ajust=(0, 0, 1, 1),
                     x_label=None, y_label=None, title=None, hue='label'):
        """wrapper for seaborn pairplot
        Normally it will take a long time to produce output
        kwargs:
        diag_kind : {'hist', 'kde'}
        """
        # TODO (1.) fix labels overlap
        palette = sns.color_palette("bright", len(set(data['label'].values)))
        ax = sns.scatterplot(x=x_label, y=y_label, hue=hue, data=data, palette=palette, legend="full")
        plt.gcf().subplots_adjust(*plot_margin_ajust)

        # set x_y_label
        _set_x_y_label(ax, x_label, y_label)

        # set title
        _set_title(ax, title)

        plt.show()

    def radial_plot(self, data=None, labels=None, x_label=None, y_label=None, title=None):
        '''wrapper for pandas radviz'''
        # TODO set title, labels

        fig = radviz(data, labels, color=sns.color_palette())

        plt.show()

    def pcoord_plot(self, data=None, labels=None):
        '''wrapper for pandas parallel coordinate, observe samples in classfication tasks'''

        fig = parallel_coordinates(data, labels, color=sns.color_palette())
        plt.show()

    def heatmap_plot(self, data=None):
        """

        Example 1
        >>> flights = sns.load_dataset("flights")
        >>> flights = flights.pivot("month", "year", "passengers")
        >>> ax = sns.heatmap(flights)

        Example 2
        >>> data2 = pd.read_csv('example.csv')
        >>> data_pivot = data2.pivot_table(index="feature1", columns="feature2", values="target_value")
        >>> data_visualizer1 = DataVisualizer()
        >>> data_visualizer1.heatmap_plot(data_pivot)

        :param data:
        :return:
        """
        # TODO Y axes is too crowded

        # https://seaborn.pydata.org/generated/seaborn.heatmap.html
        ax = sns.heatmap(data)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=45, fontsize=8)
        plt.show()

    def correlation_matrix_plot(self):
        # TODO
        # https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/
        pass

    def pie_chart_plot(self, data, attributor):
        '''pie chart plot for dataframe
        values of attributor should be discrete
        possbible attributor: gender, date
        '''
        # TODO: https://stackoverflow.com/questions/31499033/how-do-i-plot-a-pie-chart-using-pandas-with-this-data

        _check_df(data)
        data[attributor].value_counts().plot.pie(autopct='%.2f')
        plt.show()

    def date_bar_chart_plot(self, data, attributor):
        '''bar chart plot for dataframe
        values of attributor should be discrete
        possbible attributor: gender, date
        return the date count of (year, month)
        '''
        # TODO https://stackoverflow.com/questions/27365467/can-pandas-plot-a-histogram-of-dates
        # TODO add title, x_label, y_label
        _check_df(data)
        data[attributor].groupby([data[attributor].dt.year, data[attributor].dt.month]).count().plot(kind="bar")
        plt.gcf().subplots_adjust(bottom=0.2)
        plt.show()

    def feature_attribution_plot(self, data=None, target_metric=None, plot_features=None):
        sns.reset_orig()
        _check_df(data)

        metric_values = data[target_metric].values
        for feature in plot_features:
            f1, (ax1) = plt.subplots(1, sharex=True, sharey=True)
            feature_values = data[feature].values
            ax1.plot(feature_values, metric_values, 'rx')
            ax1.legend()
            x_label = feature
            y_label = target_metric
            _set_x_y_label(ax1, x_label, y_label)
            plt.show()
