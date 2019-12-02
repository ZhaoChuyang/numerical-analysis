import sys
import argparse
from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prob', type=int, default=1)
    return parser.parse_args()


def get_root(a, b, c):
    if b < 0:
        return (-b + sqrt(b*b - 4*a*c))/2*a, -2*c/(b - sqrt(b*b - 4*a*c))
    else:
        return -2*c/(b + sqrt(b*b - 4*a*c)), (-b - sqrt(b*b-4*a*c))/2*a


def get_approx():
    # generate {r_n}
    r = [0.994]
    bound = 12
    for n in range(1, bound):
        r.append(1 / 2 * r[-1])
    # generate {p_n}
    p = [1, 0.497]
    for n in range(2, bound):
        p.append(3 / 2 * p[-1] - 1 / 2 * p[-2])
    # generate {q_n}
    q = [1, 0.497]
    for n in range(2, bound):
        q.append(5 / 2 * q[-1] - q[-2])

    return r, p, q


def main():
    args = get_args()

    if args.prob == 1:
        a = [1, 1, 1, 1]
        b = [-1000.001, -10000.0001, -100000.00001, -1000000.000001]
        c = [1, 1, 1, 1]

        for i in range(len(a)):
            x1, x2 = get_root(a[i], b[i], c[i])
            print("x1: %f, x2: %f" % (x1, x2))

    if args.prob == 2:
        r, p, q = get_approx()
        xs = []
        print("以下为各近似项在第i次迭代时的值:")
        for i in range(11):
            xs.append(1/2**i)
            print("第%d次迭代时，x为%f，r为%f，p为%f，q为%f" % (i, 1 / 2 ** i, r[i], p[i], q[i]))
        print("\n以下为各近似项在第i次迭代时的误差:")
        for i in range(11):
            print("第%d次迭代时，x-r为%f，x-p为%f，x-q为%f" % (i, 1 / 2 ** i - r[i], 1 / 2 ** i - p[i], 1 / 2 ** i - q[i]))

        plt.figure(0)
        x = range(1, 11)
        plt.ylabel(r'$x_n-r_n$')
        plt.xlabel(r'$n$')
        plt.plot(x, np.array(xs)[1:11]-np.array(r)[1:11], "bo")

        plt.figure(1)
        plt.ylabel(r'$x_n-p_n$')
        plt.xlabel(r'$n$')
        plt.plot(x, np.array(xs)[1:11]-np.array(p)[1:11], "bo")

        plt.figure(2)
        plt.ylabel(r'$x_n-q_n$')
        plt.xlabel(r'$n$')
        plt.plot(x, np.array(xs)[1:11]-np.array(q)[1:11], "bo")
        plt.show()


if __name__ == '__main__':
    print(sys.argv)
    main()
