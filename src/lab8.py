import sys
import argparse

import numpy as np

from .utils.eigenvalue import power, symmetric_power, inverse_power, householder_qr


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prob', type=int, default=1)
    parser.add_argument('--method', default='power')
    parser.add_argument('--iter-num', type=int, default=30)
    parser.add_argument('--tol', type=float, default=1e-5)
    return parser.parse_args()


def main():

    np.set_printoptions(suppress=True, precision=2)

    args = get_args()
    a = np.array(([4, -1, 1], [-1, 3, -2], [1, -2, 3]))

    if args.prob == 1:
        if args.method == 'power':
            x, mu = power(a, np.ones(3), tol=args.tol, iter_num=args.iter_num)
            print("使用幂法, 求得最大特征值为%.3f, 特征向量为%r" % (mu, list(x)))

        if args.method == 'inverse':
            x, mu = inverse_power(a, np.array([1, -0.2, 3]), tol=args.tol, iter_num=args.iter_num)
            print("使用反幂法, 求得最大特征值为%.3f, 特征向量为%r" % (mu, list(x)))

        if args.method == 'symmetric':
            x, mu = symmetric_power(a, np.ones(3), tol=args.tol, iter_num=args.iter_num)
            print("使用对称幂法, 求得最大特征值为%.3f, 特征向量为%r" % (mu, list(x)))

    if args.prob == 2:
        a = np.array([[1, -1, 1.], [1, -0.5, 0.25], [1, 0, 0], [1., 0.5, 0.25], [1, 1., 1.]])
        b = np.array([1., 0.5, 0., 0.5, 2.])
        h_list = householder_qr(a, b)
        for i, h in enumerate(h_list):
            print("H_%d is:\n%r" % (i, h))


if __name__ == '__main__':
    print(sys.argv)
    main()










