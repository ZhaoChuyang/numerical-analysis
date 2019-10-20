import sys
import argparse
from math import sin, cos

from .utils.misc import bisection, newton


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=int, choices=[1, 2, 3])
    parser.add_argument('--a', type=float)
    parser.add_argument('--b', type=float)
    parser.add_argument('--tol', type=float)
    parser.add_argument('--n', type=int, default=200)
    parser.add_argument('--x0', type=float)
    return parser.parse_args()


def main():
    args = get_args()

    if args.mode == 1:
        f = lambda x: 2 - 3 * x - sin(x)
        a = args.a
        b = args.b
        tol = args.tol
        n = args.n

        root, iternum, error = bisection(f, a, b, tol, n)

        print('方程的根为%f，需要的迭代次数为%d，此时的误差为%f' % (root, iternum, error))

    if args.mode == 2:
        f = lambda x: 1/2 + 1/4*x**2 - x*sin(x) - 1/2*cos(2*x)



if __name__ == '__main__':
    print(sys.argv)
    main()
