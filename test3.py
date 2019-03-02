#import seaborn as sns
import numpy as np
import pandas as pd
import sys
import random
import matplotlib.pyplot as plt
import os
import pickle
import re
import collections

df1 = pd.read_csv('hyper_parameter_df.csv')



from .data_visualizer import DataVisualizer
data_visualizer1 = DataVisualizer()
target_metric = 'avg_accuracy'
plot_features = ['learning_rate_init', 'hidden_layer_1_size', 'alpha', 'max_n_gram', 'validation_fraction', 'max_features']

data_visualizer1.feature_attribution_plot(data=df1, target_metric=target_metric, plot_features=plot_features)