import seaborn as sns
import numpy as np
import pandas as pd
import sys
import random
import matplotlib.pyplot as plt
import os
import pickle
import re
import collections

# # ----------------------------------------------------------------------------------------------------------------------
# # convert to df
# # ----------------------------------------------------------------------------------------------------------------------
# current_dir = os.path.dirname(os.path.abspath(__file__))
# data_name = 'dow_jones_index_extended_labeled'
# data_dir = os.path.join(current_dir, data_name)
# file_name_list = os.listdir(data_dir)
# file_path_list = [os.path.join(data_dir, x) for x in file_name_list]
#
# dict1 = collections.defaultdict(lambda :[])
# for file_path in file_path_list:
#     with open (file_path, 'r') as f:
#         f_basename = os.path.basename(file_path)
#         stock_name = re.findall(r'_([A-Za-z]+)_[A-Za-z]+.txt',f_basename)[0]
#         readline_list = f.readlines()[0].strip().split(',')
#         attributor_list = readline_list[::2]
#         value_list = readline_list[1::2]
#         value_list = [float(x) for x in value_list]
#         for i, attributor in enumerate(attributor_list):
#             dict1[attributor].append(value_list[i])
#         dict1['stock_name'].append(stock_name)
#
# df1 = pd.DataFrame(dict1)
# pickle.dump(df1, open('df1', 'wb'))
# sys.exit()
# #df1 = df1.drop('stock_name', 1)
# print (df1)
# # ----------------------------------------------------------------------------------------------------------------------



df1= pickle.load(open('df1', 'rb'))
df1 = df1.drop('stock_name', 1)
df1 = df1.drop('days_to_next_dividend', 1)
df1 = df1.drop('percent_return_next_dividend', 1)
df1 = df1.drop('percent_change_price', 1)
df1 = df1.drop('previous_week_percent_change_next_weeks_price', 1)
df1 = df1.drop('previous_week_percent_change_price', 1)

#df1 = df1.drop('previous_week_highLowChange', 1)
#df1 = df1.drop('previous_week_closeOpenChange', 1)




from data_visualizer import DataVisualizer

data_visualizer1 = DataVisualizer()
# data_visualizer1.box_plot(data=df1, x='stock_name', y='candlePos', x_label_rotation=30, bottom_room=0.3,
#                           x_label='attributors', y_label='stock', title='title')
data_visualizer1.histogram_plot(data=df1, is_split_plot=False)