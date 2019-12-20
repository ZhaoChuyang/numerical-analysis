import numpy as np
from .matrix import gauss_seidel


def cubic_spline(n, x, a, boundary='natural', f1a=0, f1b=0):
    """
    determine the parameters of a cubic spline function
    :param n: number of intervals, equals points number - 1
    :param x: The given data points. array_like, shape (n+1,)
    :param a: value of f(x). array_like, shape (n+1, )
    :param boundary: type {'natural', 'clamped', 'periodic'}
    :return: parameters a, b, c, d
    """
    h = np.zeros(n+1)
    b = np.zeros(n+1)
    d = np.zeros(n+1)
    for i in range(n):
        h[i] = x[i+1] - x[i]

    A = np.zeros(shape=(n+1, n+1))
    if boundary in ["natural"]:
        A[0][0] = 1
        A[n][n] = 1
    elif boundary in ["clamped"]:
        A[0][0] = 2 * h[0]
        A[0][1] = h[0]
        A[n][n-1] = h[n-1]
        A[n][n] = 2 * h[n-1]
        b[0] = 3 / h[0] * (a[1] - a[0]) - 3 * f1a
        b[n] = 3 * f1b - 3 / h[n-1] * (a[n] - a[n-1])

    elif boundary in ['periodic']:
        A[0][0] = 2 * (h[0] + h[n-1])
        A[0][1] = h[0]
        A[0][n-1] = h[n-1]
        A[n][0] = 1
        A[n][n] = -1
        b[0] = 3 / h[0] * (a[1]-a[0]) - 3 / h[n-1] * (a[n] - a[n-1])

    elif boundary in ['extrapolated']:
        A[0][0] = -1 / h[0]
        A[0][1] = 1 / h[0] + 1 / h[1]
        A[0][2] = -1 / h[1]
        A[n][n-2] = -1 / h[n-2]
        A[n][n-1] = 1 / h[n-2] + 1 / h[n-1]
        A[n][n] = -1 / h[n-1]

    for row in range(1, n):
        col_1 = row - 1
        A[row][col_1] = h[col_1]
        A[row][col_1+1] = 2 * (h[col_1] + h[col_1+1])
        A[row][col_1+2] = h[col_1+1]

    for i in range(1, n):
        b[i] = 3 / h[i] * (a[i+1] - a[i]) - 3 / h[i-1] * (a[i] - a[i-1])

    c = gauss_seidel(A, b)[1]  # use gauss_seidel method to solve LES

    # we need to solve totally (n * 4) variables
    for i in range(n-1, -1, -1):
        b[i] = (a[i+1] - a[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
        d[i] = (c[i+1] - c[i])/3*h[i]

    return a, b, c, d



