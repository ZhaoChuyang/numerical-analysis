def composite_trapezoidal(fn, a, b, M):

    h = (b-a) / M
    s = 0

    for k in range(1, M):
        x = a + h * k
        s += h * fn(x)

    s += h / 2 * (fn(a) + fn(b))

    return s


def composite_simpson(fn, a, b, M):

    h = (b-a) / (2*M)
    s1 = 0
    s2 = 0

    for k in range(1, M):
        x = a + 2*h*k
        s1 += fn(x)

    for k in range(1, M+1):
        x = a + h * (2*k-1)
        s2 += fn(x)

    s1 *= 2*h/3
    s2 *= 4*h/3

    return s1 + s2 + h / 3 * (fn(a) + fn(b))
