import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    walk = []
    for _ in range(1000):
        walk.append(random.normalvariate(0, 1))
    plt.hist(walk, bins=30)  # bins:直方图的柱数
    plt.show()
