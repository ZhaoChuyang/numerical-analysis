from math import fabs


def bisection(f, a, b, tol, n):
    i = 1
    fa = f(a)

    while i <= n:
        p = (a + b) / 2
        fp = f(p)

        if fp == 0 or (b - a)/2 < tol:
            return [p, i, (b - a)/2]

        if fa * fp > 0:
            a = p
        else:
            b = p

        i += 1

    return -1


def newton(f, p0, tol, n, delta=0.00001):
    i = 1
    d_f = lambda x: (f(x+delta) - f(x))/delta

    while i <= n:
        p = p0 - f(p0) / d_f(p0)

        if fabs(p-p0) < tol:
            return [p, i, fabs(p-p0)]

        i += 1
        p0 = p

    return -1


def secant(f, p0, p1, tol, n):
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= n:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        if fabs(p - p1) < tol:
            return [p, i, fabs(p - p1)]

        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)

    return -1


def false_position(f, p0, p1, tol, n):
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= n:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        if fabs(p - p1) < tol:
            return [p, i, fabs(p - p1)]

        i += 1
        q = f(p)

        if q * q1 < 0:
            # 注意赋值的顺序
            p0 = p1
            q0 = q1
            p1 = p
            q1 = q
        else:
            p1 = p
            q1 = q

    return -1
