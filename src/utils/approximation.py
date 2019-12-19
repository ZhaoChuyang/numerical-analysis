import numpy as np


def get_line_norm(X, Y):

    n = len(X)
    a = np.zeros(shape=(2, 2))
    b = np.zeros(2)

    a[0][0] = np.sum(X**2)
    a[0][1] = np.sum(X)
    a[1][0] = np.sum(X)
    a[1][1] = n

    for i in range(n):
        b[0] += X[i] * Y[i]
        b[1] += Y[i]

    return a, b


def ls_line(X, Y):

    a, b = get_line_norm(X, Y)

    A, B = np.linalg.solve(a, b)

    return A, B


def get_poly_norm(X, Y):

    n = len(X)
    a = np.zeros(shape=(3, 3))
    b = np.zeros(3)

    a[0][0] = np.sum(X**4)
    a[0][1] = np.sum(X**3)
    a[0][2] = np.sum(X**2)
    a[1][0] = np.sum(X**3)
    a[1][1] = np.sum(X**2)
    a[1][2] = np.sum(X)
    a[2][0] = np.sum(X**2)
    a[2][1] = np.sum(X)
    a[2][2] = n

    b[0] = np.sum(Y * (X**2))
    b[1] = np.sum(X * Y)
    b[2] = np.sum(Y)

    return a, b


def ls_poly(X, Y):

    a, b = get_poly_norm(X, Y)

    A, B, C = np.linalg.solve(a, b)

    return A, B, C



