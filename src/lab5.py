import sys
import argparse
from math import sqrt, pi, exp, fabs

import matplotlib.pyplot as plt
from scipy import integrate

from .utils.numerical_integration import composite_trapezoidal, composite_simpson


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', type=float, default=0)
    parser.add_argument('--b', type=float, default=1)
    parser.add_argument('--method', default='cs')
    parser.add_argument('--h', type=float, default=0.01, help='步长')
    parser.add_argument('--tol', type=float)
    return parser.parse_args()


def main():

    args = get_args()
    a = args.a
    b = args.b

    fn = lambda x: 1 / sqrt(2 * pi) * exp(-(x**2)/2)
    real_val = integrate.quad(fn, 0, 1)[0]

    if args.tol not in [None]:
        tol = args.tol

        for M in range(1, 100):
            if fabs(composite_trapezoidal(fn, a, b, M) - real_val) < tol:
                print("使用复合梯形公式计算, 当精度为1e-4时, h=%f, n=%d" % ((b-a)/M, M))
                break

        for M in range(1, 100):
            if fabs(composite_simpson(fn, a, b, M) - real_val) < tol:
                print("使用复合辛普森公式计算, 当精度为1e-4时, h=%f, n=%d" % ((b-a)/(2*M), M))
                break

    elif args.method == 'cs':

        M = int((b-a) / (2 * args.h))

        answer = composite_simpson(fn, a, b, M)
        print("使用复合辛普森公式计算的结果为: %f, 误差为: %.15f" % (answer, fabs(real_val-answer)))

    elif args.method == 'ct':

        M = int((b-a)/args.h)

        answer = composite_trapezoidal(fn, a, b, M)
        print("使用复合梯形公式计算的结果为: %f, 误差为: %.15f" % (answer, fabs(real_val-answer)))


if __name__ == '__main__':
    print(sys.argv)
    main()
