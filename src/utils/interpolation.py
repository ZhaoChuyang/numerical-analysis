import numpy as np
from .matrix import gaussian_elimination, backward_substitution, gauss_seidel


def natural_cubic_spline(n, x, a):
    """
    determine the parameters of a cubic spline function with natural boundary
    :param n: number of intervals
    :param x: The given data points. shape is (n+1,)
    :param a: value of f(x). shape is (n+1, )
    :return: parameters a, b, c, d
    """
    h = np.zeros(n+1)
    b = np.zeros(n+1)
    d = np.zeros(n+1)
    for i in range(n):
        h[i] = x[i+1] - x[i]
    print(f'value of h is {h}')

    A = np.zeros(shape=(n+1, n+1))
    A[0][0] = 1
    A[n][n] = 1

    for row in range(1, n):
        col_1 = row - 1
        A[row][col_1] = h[col_1]
        A[row][col_1+1] = 2 * (h[col_1] + h[col_1+1])
        A[row][col_1+2] = h[col_1+1]
    print(f'value of A is\n {A}')

    b = np.zeros(n+1)
    for i in range(1, n):
        b[i] = 3 / h[i] * (a[i+1] - a[i]) - 3 / h[i-1] * (a[i] - a[i-1])
    print(f'value of b is {b}')

    c = gauss_seidel(A, b)[1]  # use gauss_seidel method to solve LES

    # we need to solve totally (n * 4) variables
    for i in range(n-1, -1, -1):
        b[i] = (a[i+1] - a[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
        d[i] = (c[i+1] - c[i])/3*h[i]

    return a, b, c, d


