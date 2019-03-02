from .data_visualizer import DataVisualizer
from .plt_processor import PltProcessor


def scatter_plot():
    npy_dir = '/Users/jiashupu/playground/docker/fengyanWSD/data/kaola/arr_train3'
    label_csv_path = '/Users/jiashupu/playground/docker/fengyanWSD/data/kaola/train3.csv'
    feature_names = ['f1', 'f2']

    plt_processor = PltProcessor()
    data_visualizer1 = DataVisualizer()
    df = plt_processor.tsne_reduction(npy_dir, label_csv_path, feature_names)
    data_visualizer1.scatter_plot(data=df, plot_margin_ajust=(0, 0, 1, 1),
                                  x_label=feature_names[0], y_label=feature_names[1], title=None)


if __name__ == '__main__':
    # scatter_plot
    scatter_plot()
    #
