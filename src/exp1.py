import sys
import argparse

import matplotlib.pyplot as plt


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=int, choices=[1, 2, 3])
    parser.add_argument('--x0', type=float)
    parser.add_argument('--n', type=int)
    parser.add_argument('--k', type=int)
    return parser.parse_args()


def calculate(mode, x0, n=10):
    f = lambda x: 2 * x ** 2 + x - 15
    seq = [x0]

    if mode == 1:
        for i in range(n):
            nextx =  15 - seq[i] ** 2
            seq.append(nextx)
    if mode == 2:
        for i in range(n):
            nextx = 15 / (2 * seq[i] + 1)
            seq.append(nextx)
    if mode == 3:
        for i in range(n):
            nextx = seq[i] - (2 * seq[i] ** 2 + seq[i] - 15) / (4 * seq[i] + 1)
            seq.append(nextx)

    return seq


def output(mode, seq, k = 10, n = 10):
    answer = ''

    for i in [b for b in range(k) if k - b <= 10]:
        answer = answer + 'x%d的值为%f ' % (i, seq[i])

    print(answer)

    for i in range(n):
        plt.plot(i, seq[i], 'bo')

    plt.xlabel('xi')
    plt.ylabel('y')
    plt.title('figure of mode %d' % mode)

    plt.show()


def main():
    args = get_args()

    seq = calculate(args.mode, args.x0, args.n)
    output(args.mode, seq, args.k, args.n)


if __name__ == '__main__':
    print(sys.argv)
    main()
