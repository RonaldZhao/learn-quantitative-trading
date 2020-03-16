import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(0.5, 7.5, 1000)
    y = np.sin(x)

    plt.figure(figsize=(12, 8))
    plt.plot(x, y, '--g', lw=2, label='sin(x)')
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.xticks(np.arange(0, 10, 2), ['2015-07-02', '2015-08-02', '2015-09-02', '2015-10-02', '2015-11-02'], rotation=45)
    plt.yticks(np.arange(-1, 1.5, 1), ['最小值', '零值', '最大值'])
    plt.grid(True, ls=':', color='r', alpha=0.5)
    plt.title('Functional Programming')
    plt.legend(loc='upper right')
    # 添加sin(x)的最高点注释
    plt.annotate('max sell',
                 xy=(np.pi / 2, 1),
                 xytext=(np.pi / 2, 1.3),
                 weight='regular',
                 color='g',
                 fontsize=15,
                 arrowprops={
                     'arrowstyle': '->',
                     'connectionstyle': 'arc3',
                     'color': 'g'
                 })
    # 添加sin(x)的最低点注释
    plt.annotate('min buy', xy=(np.pi * 3 / 2, -1), xytext=(np.pi * 3 / 2, -1.3), weight='regular', color='r',
                 fontsize=15,
                 arrowprops={
                     'arrowstyle': '->',
                     'connectionstyle': 'arc3',
                     'color': 'r'
                 })
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号
    plt.show()
