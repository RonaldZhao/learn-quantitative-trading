import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    stock_data = np.random.normal(loc=10.0, scale=1.0, size=1000)
    # print(stock_data)
    stock_data_format = np.around(stock_data, 2)
    # print(stock_data_format)

    pct_change = np.around((stock_data - np.roll(stock_data, 1)) - np.roll(stock_data, 1), 2)
    pct_change[0] = np.nan
    # print(pct_change)
    plt.hist(pct_change, bins=30)
    plt.show()
