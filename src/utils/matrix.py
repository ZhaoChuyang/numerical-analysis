import numpy as np


def gaussian_elimination(a):
    n = np.size(a, 0)

    for i in range(n-1):
        p = [p for p in range(i, n) if a[p][i]]
        if not p:
            raise Exception('线性方程组不存在非平凡解')

        if p != i:
            a[[p, i]] = a[[i, p]]

        for j in range(i+1, n):
            m = a[j][i] / a[i][i]
            a[[j]] = a[[j]] - m * a[[i]]

    if a[n-1][n-1] == 0:
        raise Exception('线性方程组不存在非平凡解')

    return a


def lu_factorization(a):

    n = len(a)
    mat_l = np.eye(n)
    mat_u = np.zeros((n, n))

    # Step 1
    mat_u[0, 0] = a[0, 0]
    if mat_u[0, 0] == 0:
        raise Exception('不存在LU分解')

    # Step 2
    for j in range(1, n):
        mat_u[0, j] = a[0, j]
        mat_l[j, 0] = a[j, 0] / mat_u[0, 0]

    # Step 3
    for i in range(1, n-1):
        # Step 4
        mat_u[i][i] = a[i][i] - np.matmul(mat_l[i], mat_u[:, i])

        if mat_u[i, i] == 0:
            raise Exception('不存在LU分解')

        # Step 5
        for j in range(i+1, n):
            mat_u[i, j] = a[i, j] - np.matmul(mat_l[i], mat_u[:, j])
            mat_l[j, i] = (a[j, i] - np.matmul(mat_l[j], mat_u[:, i])) / mat_u[i][i]

    # Step 6
    mat_u[n-1, n-1] = a[n-1, n-1] - np.matmul(mat_l[n-1], mat_u[:, n-1])

    return mat_l, mat_u


def backward_substitution(a, y):
    """
    shape of y is (1,n), shape of a is (n,n), shape of x is (1,n)
    """
    n = len(y)
    x = np.zeros(n)

    if a.shape[0] != y.shape[0]:
        raise Exception('矩阵和目标向量行数不相等')

    x[n-1] = y[n-1] / a[n-1, n-1]

    for i in range(n-2, -1, -1):
        temp = 0
        for j in range(n-1, i, -1):
            temp += a[i][j] * x[j]
        x[i] = (y[i] - temp) / a[i][i]

    return x


def forward_substitution(a, y):

    n = a.shape[0]
    x = np.zeros(n)

    x[0] = y[0] / a[0][0]
    for row in range(1, n):
        temp = 0
        for j in range(0, row):
            temp += a[row][j] * x[j]

        x[row] = (y[row] - temp) / a[row][row]

    return x


def jacobi(a, b, xo=None, tol=1e-6, N=100, norm='maximum'):
    """
    :param a: np.array(n, n)
    :param b: np.array(n, 1)
    :param xo: np.array(1, n)
    :param tol: tolerance
    :param N: maximum number of iterations
    :param norm: enum{"euclidean", "maximum"}
    :return: solution x, shape is (n,)
    """
    k = 1
    n = a.shape[1]
    if xo is None:
        xo = np.zeros(n)
    nxt_x = np.zeros(shape=n)
    if norm == 'maximum':
        def norm(a, b):
            return np.max(np.abs(a-b))
    if norm == 'euclidean':
        def norm(a, b):
            return np.sum((a-b) ** 2) ** (1/2)

    while k <= N:

        for i in range(0, n):

            temp = 0
            for j in range(n):
                if i != j:
                    temp += a[i][j] * xo[j]
            nxt_x[i] = (b[i] - temp) / a[i][i]

        if norm(nxt_x, xo) < tol:
            return k, nxt_x

        k += 1
        xo = nxt_x.copy()


def gauss_seidel(a, b, tol=1e-6, xo=None, N=100, norm='euclidean'):
    k = 1
    n = len(b)
    x = np.zeros(n)
    if xo is None:
        xo = np.zeros(n)

    if norm == 'euclidean':
        def norm(x, y):
            return np.sum((x - y) ** 2) ** (1/2)
    if norm == 'maximum':
        def norm(x, y):
            return np.max(np.abs(x - y))

    while k <= N:
        for i in range(n):
            temp = 0
            for j in range(n):
                if j < i:
                    temp += x[j] * a[i][j]
                if j > i:
                    temp += xo[j] * a[i][j]

            x[i] = (b[i] - temp) / a[i][i]

        if norm(x, xo) <= tol:
            return k, x

        k += 1
        xo = x.copy()



