#!/bin/python3

import math
import os
import random
import re
import sys


# Check if number is kaprekar
def checkKaprekarNumber(num: int):
    numStr = str(num)
    d = len(numStr)
    numSqr = num*num
    numSqrStr = str(numSqr)
    dSqr = len(numSqrStr)
    rPart = numSqrStr[(dSqr - d):] if dSqr>1 else dSqr
    lPrt = numSqrStr[0:(dSqr - d)] if dSqr>1 else '0'
    # print('lpart is ' + lPrt + ' rpart is ' + rPart)
    return ( int(lPrt) + int(rPart) == num )


# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p: int, q: int):
    result: str = ''
    invalidRange: bool = True
    for i in range(p, q+1, 1):
        if checkKaprekarNumber(i):
            invalidRange = False
            result += str(i) + ' '
    print(result if not(invalidRange) else 'INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
