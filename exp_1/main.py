import numpy as np
import matplotlib.pyplot as plt


def find_root_1():
    X = []
    N = 10
    for i in range(0, N):
        X.append(0)
    X[0] = 2
    for k in range(0, N - 1):
        X[k + 1] = 15 - X[k] ** 2
    K = range(0, N)

    # plot
    plt.plot(K, X, 'ro')
    plt.xlabel("K")
    plt.ylabel("X")
    plt.show()


def find_root_2():
    N = 50
    K = np.arange(N)
    X = [0. for i in range(N)]
    X[0] = 2
    for k in range(0, N-1):
        X[k + 1] = 15/(2*X[k] + 1)

    #plot
    plt.plot(K, X, 'ro')
    plt.xlabel("K")
    plt.ylabel("X")
    plt.show()


def find_root_3():
    N = 20
    K = np.arange(N)
    X = [0. for i in range(N)]
    X[0] = 2
    for k in range(0, N-1):
        X[k+1] = X[k] - (2*X[k]**2 + X[k] - 15)/(4*X[k]+1)

    #plot
    plt.plot(K, X, 'ro')
    plt.xlabel("K")
    plt.ylabel("X")
    plt.show()


find_root_3()