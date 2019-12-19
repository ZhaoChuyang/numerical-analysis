import sys
import argparse

import numpy as np
import matplotlib.pyplot as plt

from .utils.approximation import ls_poly, get_poly_norm


def main():

    x = np.array([-2, -1, 0, 1, 2])
    y = np.array([0, 1, 2, 1, 0])

    a, b = get_poly_norm(x, y)
    A, B, C = ls_poly(x, y)

    print("该最小二乘拟合模型的正则方程组如下:\n%r\n%r" % (a, np.transpose(b)))

    print("方程组的解为: A = %f, B = %d, C = %f" % (A, B, C))

    f = lambda x: A * x**2 + B * x + C
    xs = np.linspace(-3, 3, 30)

    plt.plot(x, y, 'o', label="given data points")
    plt.plot(xs, f(xs), '-', label="least squared polynomial")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    print(sys.argv)
    main()












