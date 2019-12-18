import numpy as np


def euler(f, a, b, ya, M):

    h = (b-a) / M
    T = np.linspace(a, b, M+1)
    Y = np.zeros(M+1)

    Y[0] = ya
    for i in range(0, M):
        Y[i+1] = Y[i] + h * f(T[i], Y[i])

    return T, Y


def heum(f, a, b, ya, M):

    h = (b-a) / M
    T = np.linspace(a, b, M+1)
    Y = np.zeros(M+1)
    Y[0] = ya

    for i in range(0, M):
        k1 = f(T[i], Y[i])
        k2 = f(T[i+1], Y[i] + h * k1)
        Y[i+1] = Y[i] + (h / 2) * (k1 + k2)

    return T, Y


def runge_kutta_4(f, a, b, ya, M):

    h = (b-a) / M
    T = np.linspace(a, b, M+1)
    Y = np.zeros(M+1)
    Y[0] = ya

    for i in range(0, M):
        k1 = h * f(T[i], Y[i])
        k2 = h * f(T[i] + h / 2, Y[i] + k1 / 2)
        k3 = h * f(T[i] + h / 2, Y[i] + k2 / 2)
        k4 = h * f(T[i] + h, Y[i] + k3)
        Y[i+1] = Y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return T, Y


def runge_kutta_4_2(f1, f2, a, b, f1a, f2a, M):

    h = (b-a)/M
    x = np.linspace(a, b, M+1)
    Y = np.zeros(shape=(2, M+1))
    Y[0][0] = f1a
    Y[1][0] = f2a

    for i in range(0, M):
        k11 = h * f1(x[i], Y[0][i], Y[1][i])
        k21 = h * f2(x[i], Y[0][i], Y[1][i])
        k12 = h * f1(x[i] + h / 2, Y[0][i] + k11 / 2, Y[1][i] + k21 / 2)
        k22 = h * f2(x[i] + h / 2, Y[0][i] + k11 / 2, Y[1][i] + k21 / 2)
        k13 = h * f1(x[i] + h / 2, Y[0][i] + k12 / 2, Y[1][i] + k22 / 2)
        k23 = h * f2(x[i] + h / 2, Y[0][i] + k12 / 2, Y[1][i] + k22 / 2)
        k14 = h * f1(x[i], Y[0][i] + k13 / 2, Y[1][i] + k23)
        k24 = h * f2(x[i], Y[0][i] + k13 / 2, Y[1][i] + k23)
        Y[0][i + 1] = Y[0][i] + (k11 + 2 * k12 + 2 * k13 + k14) / 6
        Y[1][i + 1] = Y[1][i] + (k21 + 2 * k22 + 2 * k23 + k24) / 6

    return x, Y










