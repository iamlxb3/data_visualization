import seaborn as sns
import numpy as np
import pandas as pd
import sys
import random
import matplotlib.pyplot as plt


sns.set_style('whitegrid')
array1 = np.array([[random.randint(0,100) for x in range(10)],[random.randint(0,100) for x in range(10)]])
df1 = pd.DataFrame({ 'A' : [random.randint(0,100) for x in range(10)],
                     'B' : [random.randint(0,100) for x in range(10)] })
print (df1)
print (set(df1.keys()))
ax = sns.boxplot(data=df1)
ax.set_xlabel('common xlabel')
plt.show()