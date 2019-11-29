import sys
import argparse

import numpy as np

from .utils.matrix import gaussian_elimination, lu_factorization, backward_substitution, forward_substitution, jacobi, gauss_seidel


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', help='choose from LU, Jacobi and Gauss-Seidel')
    parser.add_argument('--norm', default='euclidean', help='choose from euclidean and maximum')
    return parser.parse_args()


def main():
    args = get_args()
    A = np.array([(4, -1, 1), (4, -8, 1), (-2, 1, 5)])
    y = np.array([7, -21, 15])
    print(f'shape of A is {A.shape}, shape of y is {y.shape}')
    norm = args.norm

    if args.method == 'LU':
        l_mat, u_mat = lu_factorization(A)
        print(f'lower matrix of A is:\n{l_mat}')
        print(f'upper matrix of A is:\n{u_mat}')

        temp = forward_substitution(l_mat, y)
        x = backward_substitution(u_mat, temp)

        print(f"使用LU分解法，求得该线性方程组的解为 {x}")

    if args.method == 'Jacobi':
        x = jacobi(A, y, norm=norm, N=30, tol=1e-4)
        print(f"使用Jacobi方法，求得该线性方程组的解为 {x[1]}，迭代次数为 {x[0]}")

    if args.method == 'Gauss-Seidel':
        x = gauss_seidel(A, y, norm=norm, N=30, tol=1e-4)
        print(f"使用Gauss-Seidel方法，求得该线性方程组的解为 {x[1]}，迭代次数为 {x[0]}")

    if args.method not in ['LU', 'Jacobi', 'Gauss-Seidel']:
        print('请在LU, Jacobi, Gauss-Seidel中选择一种方法求解')


if __name__ == '__main__':
    print(sys.argv)
    main()
