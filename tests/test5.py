import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    stock_data = np.random.normal(loc=10.0, scale=1.0, size=1000)
    pct_change = np.around((stock_data - np.roll(stock_data, 1)) - np.roll(stock_data, 1), 2)
    pct_change[0] = np.nan

    # 生成以天为单位的时间序列
    dd = pd.date_range('2010-01-01', freq='D', periods=1000)
    # print(dd)
    # print(type(dd))
    # print(dir(dd))

    df_stock = pd.DataFrame({'close': stock_data, 'price_range': pct_change}, index=dd)
    # print('股票交易数据：\n{}', df_stock.head())

    # 绘制收盘价
    df_stock.close[100:150].plot(c='b')
    plt.legend(['Close'], loc='best')
    plt.show()
