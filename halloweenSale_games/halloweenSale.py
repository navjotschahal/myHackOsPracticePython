#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
# https://www.hackerrank.com/challenges/halloween-sale/problem
def howManyGames(p, d, m, s):
    gameCounter = 0
    while (p - d > m or p > m) :
        if s <= p:
            return gameCounter
        s -= p
        p -= d
        gameCounter += 1
    # if s > p - d:
    #     p -= d
    #     s -= p
    #     gameCounter += 1
    while s >= m:
        s -= m
        gameCounter += 1
    # Return the number of games you can buy
    return gameCounter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open("F:\hackerRankPython\halloweenSale_games\gamesBought.txt", 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
