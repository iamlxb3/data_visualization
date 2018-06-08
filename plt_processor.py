import numpy as np
import collections


class PltProcessor:
    """
    Process data before plot
    """

    def __init__(self):
        pass

    def format_by_bin(self, data, key=None, bin_num=None, f_min=None, f_max=None):
        """
        corase implementation of converting into bin
        bin value is the avarage of bin head and bin tail
        e.g. for values [0.1, 0.2, 0.3, 0.33 0.4] -> range(0.1, 0.41)
        if bin set to 2, bins = [(0.1, 0.25), (0.25, 0.4)] -> [0.175, 0.325] (average)
        The bin values would be [0.175, 0.175, 0.325, 0.325, 0.325]

        :param data: panda dataframe
        :param key: the key you want to convert to bin, has to be continuous number
        :param bin_num: how many bins to split into
        :return:
        Example
        -------------------------------------------
        >>> plt_processor1 = PltProcessor()
        >>> f_min, f_max = 0.5, 0.85 # min and max of the feature range
        >>> data = plt_processor1.format_by_bin(data, 'feature1', 10, f_min=None, f_max=None)

        """
        values = data[key].values
        if f_min:
            min_value = f_min
        else:
            min_value = min(values)
        if f_max:
            max_value = f_max
        else:
            max_value = max(values)

        bin_unit = (max_value - min_value) / bin_num
        bins = []
        for i in range(bin_num):
            if i == bin_num - 1:
                bin_start = min_value + bin_unit * i
                bin_end = max_value
            else:
                bin_start = min_value + bin_unit * i
                bin_end = bin_start + bin_unit
            bins.append((bin_start, bin_end))

        bin_values = []
        for i, row in data.iterrows():
            target_value = row[key]
            bin_value = None
            for bin in bins:
                if bin[0] <= target_value <= bin[1]:
                    bin_value = np.average(bin)
                    break
            if not bin_value:
                raise Exception("UNknown error! invalid target_value: {}".format(target_value))
            data.at[i, key] = float("{:.3f}".format(bin_value))
            bin_values.append(bin_value)

        print(sorted(collections.Counter(bin_values).items()))
        return data
