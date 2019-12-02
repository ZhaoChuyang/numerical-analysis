import sys
import argparse
from math import sin, cos, pi, exp

from .utils.misc import bisection, newton, secant, false_position


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=int, choices=[1, 2, 3])
    parser.add_argument('--a', type=float)
    parser.add_argument('--b', type=float)
    parser.add_argument('--tol', type=float, default=0.00001)
    parser.add_argument('--n', type=int, default=200, help='max iteration num')
    parser.add_argument('--p0', type=float)
    parser.add_argument('--p1', type=float)
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
        print("使用二分法求解：")
        print('方程的根为%f，需要的迭代次数为%d，误差为%f' % (root, iternum, error))

    if args.mode == 2:
        f = lambda x: 1/2 + 1/4*x**2 - x*sin(x) - 1/2*cos(2*x)

        seq_p0 = [pi/2, 5*pi, 10*pi]

        print("使用牛顿法求解：")
        for index, p0 in enumerate(seq_p0):
            root, iternum, error = newton(f, p0, args.tol, args.n)

            print('当初始值为%f时，求得的根为%f，迭代次数为%d，误差为%f' % (p0, root, iternum, error))

    if args.mode == 3:
        f = lambda x: 5 * x - exp(x)
        a = args.a
        b = args.b
        p0 = args.p0
        p1 = args.p1
        tol = args.tol
        n = args.n

        # using bisection method
        root, iternum, error = bisection(f, a, b, tol, n)
        print('使用二分法求解，根为%.4f，迭代次数为%d，误差为%f' % (root, iternum, error))

        # using newton's method
        root, iternum, error = newton(f, p0, tol, n)
        print('使用牛顿法求解，根为%.4f，迭代次数为%d，误差为%f' % (root, iternum, error))

        # using secant method
        root, iternum, error = secant(f, p0, p1, tol, n)
        print('使用割线法求解，根为%.4f，迭代次数为%d，误差为%f' % (root, iternum, error))

        # using false position method
        root, iternum, error = false_position(f, p0, p1, tol, n)
        print('使用错位法求解，根为%.4f，迭代次数为%d，误差为%f' % (root, iternum, error))


if __name__ == '__main__':
    print(sys.argv)
    main()
