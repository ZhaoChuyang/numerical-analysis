import sys
import argparse

import numpy as np

from .utils.interpolation import cubic_spline
import matplotlib.pyplot as plt


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--points-num', type=int, default=21)
    parser.add_argument('--periodic', type=bool, default=False)
    return parser.parse_args()


def plot_spline(plt, a, b, c, d, x, y, title):
    plt.plot(x, y, '.')
    for i in range(len(x)-1):
        start = x[i]
        end = x[i+1]
        X = np.linspace(start, end, 50)
        Y = a[i] + b[i] * (X - x[i]) + c[i] * (X - x[i]) ** 2 + d[i] * (X - x[i]) ** 3
        plt.plot(X, Y)
    plt.set_title(title)


def main():
    np.set_printoptions(suppress=True, precision=2)
    args = get_args()
    if args.periodic is True:
        x = np.linspace(0, 2 * np.pi, args.points_num)
        y = np.sin(x)
        fig, axes = plt.subplots(2, 2,constrained_layout=True)

        a, b, c, d = cubic_spline(len(x) - 1, x, y, boundary='natural')
        plot_spline(axes[0][0], a, b, c, d, x, y, title='natural')

        a, b, c, d = cubic_spline(len(x) - 1, x, y, boundary='clamped', f1a=1, f1b=1)
        plot_spline(axes[0][1], a, b, c, d, x, y, title='clamped')

        a, b, c, d = cubic_spline(len(x) - 1, x, y, boundary='periodic')
        plot_spline(axes[1][0], a, b, c, d, x, y, title='periodic')

        a, b, c, d = cubic_spline(len(x)-1, x, y, boundary='extrapolated')
        plot_spline(axes[1][1], a, b, c, d, x, y, title='extrapolated')

        plt.show()

    if args.periodic is False:
        x = np.linspace(0, np.pi, args.points_num)
        y = np.sin(x)
        fig, axes = plt.subplots(2, 2,constrained_layout=True)

        a, b, c, d = cubic_spline(len(x) - 1, x, y, boundary='natural')
        plot_spline(axes[0][0], a, b, c, d, x, y, title='natural')

        a, b, c, d = cubic_spline(len(x) - 1, x, y, boundary='clamped', f1a=1, f1b=-1)
        plot_spline(axes[0][1], a, b, c, d, x, y, title='clamped')

        a, b, c, d = cubic_spline(len(x) - 1, x, y, boundary='periodic')
        plot_spline(axes[1][0], a, b, c, d, x, y, title='periodic')

        a, b, c, d = cubic_spline(len(x)-1, x, y, boundary='extrapolated')
        plot_spline(axes[1][1], a, b, c, d, x, y, title='extrapolated')

        plt.show()


if __name__ == '__main__':

    print(sys.argv)
    main()


