#!/bin/python3

# https://www.hackerrank.com/challenges/service-lane/problem

import math
import os
import random
import re
import sys


# Complete the serviceLane function below.
def serviceLane(n, cases):
    minWidthArray: list = []
    for case in cases:
        minWidthArray.append(min(n[ case[0] : case[1] + 1 ]))
    return minWidthArray


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("F:\hackerRankPython\Service_Lane\\Output.txt", 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
