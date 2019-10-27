import sys
import argparse

import numpy as np

from .utils.matrix import gaussian_elimination, lu_factorization


def main():

    np.set_printoptions(suppress=True, precision=2)
    # a = np.array([(4, -1, 1, 7), (4, -8, 1, -21), (-2, 1, 5, 15)], dtype=float)
    a = np.random.random((9, 9))
    a1 = gaussian_elimination(a)
    l, u = lu_factorization(a)

    print(a)
    print(np.matmul(l, u))


if __name__ == '__main__':
    print(sys.argv)
    main()
