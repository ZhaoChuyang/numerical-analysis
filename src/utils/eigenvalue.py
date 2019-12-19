import numpy as np


def power(a, x0, tol=1e-5, iter_num=20):

    x = x0.copy()
    c = 0

    for it in range(iter_num):
        y = np.matmul(a, x)
        c = np.max(y)

        if np.max(x - y) < tol:
            break

        y /= c
        x = y

    return x, c


def symmetric_power(a, x0, tol=1e-5, iter_num=20):

    x = x0.copy()
    mu = 0

    def euclidean_norm(x):
        return np.sqrt(np.sum(x ** 2))

    for it in range(iter_num):
        y = np.matmul(a, x)
        mu = np.matmul(x.T, y)

        if euclidean_norm(y) == 0:
            raise Exception("A的特征值为0, 请重新选择A和x")

        err = euclidean_norm(x - y / euclidean_norm(y))
        x = y / euclidean_norm(y)

        if err < tol:
            break

    return x / np.max(x), mu


def inverse_power(a, x0, tol=1e-5, iter_num=20):

    n = len(x0)
    x = x0.copy()

    mu = 0

    for iteration in range(iter_num):
        q = np.matmul(np.matmul(x.T, a), x) / np.matmul(x.T, x)

        try:
            y = np.linalg.solve(a - q * np.eye(n), x)

        except Exception:
            mu = np.max(y)
            mu = (1 / mu) + q
            return x, mu

        yp = np.max(y)
        mu = yp

        err = np.max(x - y / yp)
        x = y / yp

        if err < tol:
            mu = (1 / mu) + q

    return x, mu


def householder_qr(a, b):
    n_row = a.shape[0]
    n_col = a.shape[1]

    h_list = []
    h = np.zeros(shape=(n_row, n_row))

    for i in range(n_col):
        temp = a[:, i]
        alpha = np.sqrt(np.sum(temp**2))
        sign = 1
        if temp[i] > 0:
            sign = -1
        temp_v = np.zeros(len(temp))
        temp_v[i] = sign * alpha
        v = temp - temp_v

        h = np.eye(n_row) - 2 * np.matmul(v.reshape(n_row, 1), v.reshape(1, n_row)) / np.matmul(v.T, v)

        a = np.matmul(h, a)

        h_list.append(h)

    return h_list





