import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 正态分布直方图
    plt.hist(np.random.normal(loc=0.0, scale=1.0, size=1000), bins=30)
    plt.show()
