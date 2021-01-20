#!/bin/python3

# https://www.hackerrank.com/challenges/chocolate-feast/problem

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    bought = 0
    bought = int(n / c)
    # collected = int(bought / m)
    # remaining = bought - (collected * m) if bought - (collected * m) > 0 else 0

    # while int(collected / m) > 0:
    #     collected += collected / m
    return bought + collectedChocos(bought, m)

def collectedChocos(c, m):
    """
    c: Total Wrappers child has collected
    m: Number of wrappers required to reimburse a chocolate
    """
    collected = int(c / m)
    remaining = c - (collected * m)
    if collected + remaining < m :
        return collected
    return collected + collectedChocos(collected + remaining, m)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('F:\hackerRankPython\\Chocolate_Feast\\result.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
