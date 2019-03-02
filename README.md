# data_visualization
This is a long-term project, aiming to provide easy-to-use plot api for machine-learning projects.
It is split into 2 parts. One aims to visualise the data, the other one is to visualise the ML results. In the future, 
visualising the process of learning may be incorparated.

### scatter plot
```python
from pjs_ml_visual import DataVisualizer
from pjs_ml_visual import PltProcessor

npy_dir = '/Users/jiashupu/playground/docker/fengyanWSD/data/kaola/arr_train3'
label_csv_path = '/Users/jiashupu/playground/docker/fengyanWSD/data/kaola/train3.csv'
feature_names = ['f1', 'f2']

plt_processor = PltProcessor()
data_visualizer1 = DataVisualizer()
df = plt_processor.tsne_reduction(npy_dir, label_csv_path, feature_names)
data_visualizer1.scatter_plot(data=df, plot_margin_ajust=(0, 0, 1, 1),
                              x_label=feature_names[0], y_label=feature_names[1], title=None)

```
