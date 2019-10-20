import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import argparse
import sys
import math


def calc_y(x):
    return 2-3*x-math.sin(x)


def calc_yy(x):
    return 5*x - math.exp(x)


def bisection_method(prob):
    N0 = 1000
    TOL = 0.0005
    it = 1
    a = 0
    b = 1
    if prob == 2:
        FA = calc_y(a)
    elif prob == 3:
        FA = calc_yy(a)

    while it < N0:
        p = a + (b-a)/2
        if prob == 3:
            FP = calc_yy(p)
        elif prob == 2:
            FP = calc_y(p)
        if FP == 0 or (b-a)/2<TOL:
            if prob == 2:
                print("找到的根为："+str(p)+"\t误差小于："+str((b-a)/2)+"\t迭代次数为："+str(it))
            if prob == 3:
                print("找到的根为："+str(round(p, 4)))
            return
        elif FP*FA > 0:
            a = p
            FA = FP
        else:
            b = p
        it += 1


def calc_y2(x):
    return 1/2 + 1/4*x**2 - x*math.sin(x) - 1/2*math.cos(2*x)


def calc_diff2(x):
    dx = 0.0001
    return (calc_y2(x+dx)-calc_y2(x))/dx

def calc_diff3(x):
    dx = 0.0001
    return (calc_yy(x+dx)-calc_yy(x))/dx

def newton_method(x0, prob):
    it = 1
    N0 = 1000
    TOL = 1e-5

    p0 = x0
    while it < N0:
        if prob == 2:
            p = p0 - calc_y2(p0)/calc_diff2(p0)
        elif prob == 3:
            p = p0 - calc_yy(p0)/calc_diff3(p0)
        if math.fabs(p-p0) < TOL:
            if prob == 2:
                print("找到的根为："+str(p)+"\t"+"误差小于："+str(math.fabs(p-p0))+"\t"+"迭代次数为："+str(it))
            if prob == 3:
                print("找到的根为: "+str(round(p, 4)))
            return
        it += 1
        p0 = p


if __name__=='__main__':
    parser = argparse.ArgumentParser('Choose bisection or newton\'s method')
    parser.add_argument('-p', '--problem', type=int)
    parser.add_argument('-m', '--method')
    parser.add_argument('-i', '--init')


    args = '--method newton -i pi*10'.split()
    args1 = '-p 3 -m bisection'.split()
    args2 = '-p 3 -m newton'.split()
    args = parser.parse_args(args2)

    method = args.method

    if args.problem == 3:
        if args.method == 'bisection':
            bisection_method(3)
        elif args.method == 'newton':
            newton_method(0, 3)


    else:
        if method == 'bisection':
            bisection_method(2)
        else:
            if args.init == 'pi/2':
                newton_method(math.pi / 2, 2)
            elif args.init == 'pi*5':
                newton_method(math.pi * 5, 2)
            elif args.init == 'pi*10':
                newton_method(math.pi * 10, 2)

