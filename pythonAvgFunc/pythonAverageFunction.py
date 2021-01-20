#!/bin/python3

import math
import os
import random
import re
import sys


# avg function
def avg(number: list):
    return sum(number)/len(number)

# write your code here
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('F:\hackerRankPython\pythonAvgFunc\output.txt', 'w')
    
    nums = list(map(int, input().split()))
    res = avg(nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()