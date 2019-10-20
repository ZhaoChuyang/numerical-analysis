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


def newton():
