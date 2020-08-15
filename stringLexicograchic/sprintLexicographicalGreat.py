#!/bin/python3

import math
import os
import random
import re
import sys

# Check for no answer. and finds `pivot1`
def checkNoAnswer(w: str):
    i = len(w) - 1
    d: dict = {"noAnswer": False}
    while i > 0 and w[i-1] >= w[i]:
        i -= 1
    d['pivot1'] = i
    if i <= 0 :
        d['noAnswer'] = True
    return d


# find sucsessor to pivot OR pivot2   from Suffix
def findSecondPivot(w: str, pivot1: int):
    # Find successor to pivot from Suffix   E.g. [_._.Prefix_._._``pivot1 - 1``_._._Suffix_._._]
    j = len(w) - 1
    while w[j] <= w[pivot1 - 1]:
        j -= 1
    return j


# Swap thre pivot1-1 with pivot2    in list of input String   and return the swapped list.
def swapWthePivots(w: str, pivot1: int, pivot2: int):
    l: list = list(w)
    l[pivot1 - 1], l[pivot2] = l[pivot2], l[pivot1 - 1]
    return l


# Reverse the suffix in list of input w String and return reversedSuffix list l.
def reverseSuffix(l: list, pivot1):
    l[pivot1 : ] = l[len(l) - 1 : pivot1 - 1 : -1]
    return l


# Complete the biggerIsGreater function below.
def biggerIsGreater(w: str):
    strWdata: dict = checkNoAnswer(w)
    # print(strWdata['pivot1'])
    pivot1: int = strWdata['pivot1']
    if strWdata['noAnswer'] :
        return 'no answer'
    pivot2 = findSecondPivot(w, pivot1)
    return ''.join(reverseSuffix(swapWthePivots(w, pivot1, pivot2), pivot1))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # fptr = open('F:\hackerRankPython\stringLexicograchic\sringLexicalgreaterResult.txt', 'w')
    fptr1 = sys.stdin
    fptr2 = sys.stdout

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
