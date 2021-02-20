#!/bin/python3

# https://www.hackerrank.com/challenges/lisa-workbook/problem

import math
import os
import random
import re
import sys

def calcSpecialProblems(array):
    count: int = 0
    for c in range(len(array)):
        count += 1 if  c in array[c] else 0
    return count


# Complete the workbook function below.
def workbook(n, k, arr):
    chapterPages: list = []
    for chapter in arr:
        totalProblems = chapter
        pages = int(chapter / k) + 1 if chapter / k > int(chapter / k) else int(chapter / k)
        chapPageArr: list = []
        while totalProblems:
            for j in range(k):
                chapPageArr.append(chapter - totalProblems if totalProblems else 0)
                totalProblems += -1
                # if j == k - 1:
                #     if len(chapPageArr):
                        
                if not(totalProblems):
                    break
            chapterPages.append(chapPageArr)
            chapPageArr = []
            if not(totalProblems):
                break
        # chapterPages.append(chapPageArr)
    print(chapterPages)
    return calcSpecialProblems(chapterPages)
    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("F:\hackerRankPython\Lisa_Workbook\\Output.txt", 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
