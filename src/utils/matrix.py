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

    n = np.size(a, 0)
    mat_l = np.eye(n)
    mat_u = np.zeros((n, n))

    def mat_mul(i, j):
        sum = 0
        # for k range from i to n-1 the val of l[i, k] is 0
        for k in range(n): # or in range(n)
            sum += mat_l[i, k] * mat_u[k, j]
        return sum

    # Step 1
    mat_u[0, 0] = a[0, 0] / mat_l[0, 0]
    if mat_u[0, 0] == 0:
        raise Exception('不存在LU分解')

    # Step 2
    for j in range(0, n):
        mat_u[0, j] = a[0, j]
        mat_l[j, 0] = a[j, 0] / mat_u[0, 0]

    # Step 3
    for i in range(1, n-1):
        # Step 4
        mat_u[i, i] = a[i, i] - mat_mul(i, i)
        if mat_u[i, i] == 0:
            raise Exception('不存在LU分解')
        # Step 5
        for j in range(i+1, n):
            mat_u[i, j] = a[i, j] - mat_mul(i, j)
            mat_l[j, i] = a[j, i] - mat_mul(j, i)

    # Step 6
    mat_u[n-1, n-1] = a[n-1, n-1] - mat_mul(n-1, n-1)

    return mat_l, mat_u


