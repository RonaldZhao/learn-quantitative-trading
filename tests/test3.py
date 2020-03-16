from timeit import timeit
import random
import numpy as np


def list_test():
    walk = []
    for _ in range(1000000):
        walk.append(random.normalvariate(0.0, 1.0))


def ndarray_test():
    np.random.normal(loc=0.0, scale=1.0, size=1000000)


if __name__ == '__main__':
    t1 = timeit('list_test()', 'from __main__ import list_test', number=1)
    t2 = timeit('ndarray_test()', 'from __main__ import ndarray_test', number=1)

    print('list: {}'.format(t1))
    print('ndarray: {}'.format(t2))
