import sys
import argparse
from math import tan, pi

import numpy as np
import matplotlib.pyplot as plt

from .utils.ODE import euler, heum, runge_kutta_4, runge_kutta_4_2


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prob', type=int, default=1)
    parser.add_argument('--method', type=str, default='euler')
    parser.add_argument('--a', type=float, default=0)
    parser.add_argument('--b', type=float, default=pi/3)
    parser.add_argument('--ya', type=float, default=0)
    parser.add_argument('--M', type=int, default=10)
    return parser.parse_args()


def main():

    args = get_args()
    if args.prob == 1:

        fn = lambda t, y: 1 + y*y
        X, y_euler = euler(fn, args.a, args.b, args.ya, args.M)
        X, y_heum = heum(fn, args.a, args.b, args.ya, args.M)
        X, y_runge = runge_kutta_4(fn, args.a, args.b, args.ya, args.M)
        y_real = np.tan(X)

        plt.plot(X, y_real, 'c-', label='true value')
        plt.plot(X, y_euler, 'bo', label='euler')
        plt.plot(X, y_heum, 'mo', label='heum')
        plt.plot(X, y_runge, 'go', label='runge kutta')
        plt.legend()
        plt.show()

    if args.prob == 2:
        mus = [0.01, 0.1, 1]
        for mu in mus:
            vander_pol_1 = lambda t, y1, y2: y2
            vander_pol_2 = lambda t, y1, y2: mu * (1 - y1**2) * y2 - y1

            x, Y = runge_kutta_4_2(vander_pol_1, vander_pol_2, args.a, args.b, 0, 1, args.M)
            plt.plot(x, Y[0], label='mu is %.2f' % mu)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    print(sys.argv)
    main()
