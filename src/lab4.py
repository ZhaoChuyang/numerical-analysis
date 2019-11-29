import sys
import argparse
from math import exp

import numpy as np

from .utils.interpolation import natural_cubic_spline
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print(sys.argv)

    x = np.array([0,1,2,3])
    a = np.zeros(len(x))
    for i in range(len(x)):
        a[i] = exp(x[i])

    a, b, c, d = natural_cubic_spline(len(x)-1, x, a)

    temp_x = np.linspace(x[0], x[3], 1000)
    temp_y = np.exp(temp_x)

    plt.plot(temp_x, temp_y, label="exp(x)")

    for i in range(0, 3):
        start = x[i]
        end = x[i+1]
        temp_x = np.linspace(start, end, 1000)
        temp_y = a[i] + b[i]*(temp_x - x[i]) + c[i]*(temp_x - x[i])**2 + d[i]*(temp_x - x[i])**3
        plt.plot(temp_x, temp_y, "-.", label="cubic spline")
    plt.legend()
    plt.show()

