import sys
import argparse
from math import exp

import numpy as np

from .utils.interpolation import cubic_spline
import matplotlib.pyplot as plt


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=11)
    return parser.parse_args()


if __name__ == '__main__':
    print(sys.argv)

    n_points = 21
    x = np.linspace(0, np.pi, n_points)
    fx = np.sin(x)

    a, b, c, d = cubic_spline(n_points-1, x, fx, boundary='clamped')

    temp_x = np.linspace(x[0], x[-1], 10000)
    temp_y = np.sin(temp_x)
    # plt.plot(temp_x, temp_y, label="sin(x)")

    for i in range(0, n_points-1):
        start = x[i]
        end = x[i+1]
        temp_x = np.linspace(start, end, 100)
        temp_y = a[i] + b[i]*(temp_x - x[i]) + c[i]*(temp_x - x[i])**2 + d[i]*(temp_x - x[i])**3
        plt.plot(temp_x, temp_y, "-.", label="cubic spline")

    # plt.legend()
    plt.show()

