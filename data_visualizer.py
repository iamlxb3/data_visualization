'''
A data visualizer
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pandas.tools.plotting import radviz
from pandas.tools.plotting import parallel_coordinates



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

    def box_plot(self, data=None, x=None, y=None, x_label=None, y_label=None, x_label_rotation=None,
                 bottom_room=None, title=None, linewidth=1, orient='v',
                 plot_margin_ajust = (0, 1, 1, 0)):
        # TODO (1.) add hue https://seaborn.pydata.org/generated/seaborn.boxplot.html
        # TODO (2.) incorporate orient
        # TODO (3.) explore col in sns.boxplot

        '''wrapper for seaborn box_plot
        args:

        plot_margin_ajust: left=None, bottom=None, right=None, top=None
        x
        '''
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
        plt.gcf().subplots_adjust(*plot_margin_ajust)
        #

        # set x_y_label
        _set_x_y_label(ax, x_label, y_label)

        # set title
        _set_title(ax, title)

        plt.show()

    def histogram_plot(self, data=None, is_single_attributor=False, is_split_plot=True,
                       x_label=None, y_label=None, title=None):
        '''wrapper for seaborn distplot'''

        if is_single_attributor:
            pass
        if not is_single_attributor:
            _check_df(data)
            for attributor in data:
                attr_data = data[attributor]
                # TODO set x,y labels, title for each histogram plot
                # check the type of the df
                if is_numeric_dtype(attr_data):
                    ax = sns.distplot(data[attributor])
                    plt.xlabel(attributor)
                    if is_split_plot:
                        plt.show()
                else:
                    raise Exception("Attributor {} is not valid for histogram plot".format(attributor))
            if not is_split_plot:
                # set x_y_label
                _set_x_y_label(ax, x_label, y_label)

                # set title
                _set_title(ax, title)

                plt.show()

    def scatter_plot(self, data=None, diag_kind='kde', plot_margin_ajust=(0, 0, 1, 1), marker_size=5,
                     x_label=None, y_label=None, title=None):
        '''wrapper for seaborn pairplot
        Normally it will take a long time to produce output
        kwargs:
        diag_kind : {‘hist’, ‘kde’}
        '''
        # TODO (1.) fix labels overlap
        ax = sns.pairplot(data, diag_kind='kde', plot_kws={"s": marker_size})
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
        ''''''
        # TODO Y axes is too crowded

        # https://seaborn.pydata.org/generated/seaborn.heatmap.html
        ax = sns.heatmap(data)
        ax.set_yticklabels(ax.get_yticklabels(), rotation=45, fontsize=8)
        plt.show()

    def correlation_matrix_plot(self):
        # TODO
        # https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/
        pass
        
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