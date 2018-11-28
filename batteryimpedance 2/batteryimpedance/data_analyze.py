#!/usr/bin/env python3
"""
data_proc.py
Demo including:
 - calculating the value of resistance from real and imaginary impedance

"""

from __future__ import print_function

import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import unittest
import sys
import argparse



def parse_cmdline(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-csvx', '--cy', help="CSV for x", default='./examplex.csv')
    parser.add_argument('-csvy', '--cx', help="CSV for y", default='./exampley.csv')
    args = parser.parse_args(argv)
    return args


def main(argv=None):
    args = parse_cmdline(argv)
    x=np.genfromtxt(args.cx, delimiter=',')
    y=np.genfromtxt(args.cy, delimiter=',')



    xx = np.multiply(x, x)
    yy = np.multiply(y, y)
    xy = np.multiply(x, y)
    n = x.size
    A = np.array([[np.sum(x), np.sum(y), n], [np.sum(xy), np.sum(yy), np.sum(y)], [np.sum(xx), np.sum(xy), np.sum(x)]])
    B = np.array([[np.sum(xx + yy)], [np.sum(xx * y + yy * y)], [np.sum(xx * x + xy * y)]])
    a = np.linalg.solve(A, B)
    R = np.sqrt((a.item(0) ** 2 + a.item(1) ** 2) * 0.25 - a.item(2))
    plt.plot(x, y)
    plt.xlabel('Z (ohms)')
    plt.ylabel('Z''(ohms)')
    plt.title('Nyquist plot of the impedance spectra')
    plt.grid(True)
    plt.show()
    print("R=", R)

    return R


if __name__ == "__main__":
    status = main()
