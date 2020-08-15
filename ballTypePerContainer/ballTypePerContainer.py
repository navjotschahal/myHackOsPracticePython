#!/bin/python3

import math
import os
import random
import re
import sys
import enum


class possibility(enum.Enum):
   POSSIBLE = 'Possible'
   IMPOSSIBLE = 'Impossible'


# find container ball capacity.
# or
# max number of balls in container.
def containerCapacity(container):
    capacity = 0
    if not(len(container)):
        return capacity
    for ball in container:
        capacity += ball
    return capacity


# Total number of particular ballType , data in array respectively.
def ballTypeTotalArray(container, totalBallTypes):
    res_list = [] 
    ballTypeNumArray = [0]*totalBallTypes
    if not(len(container)):
        return ballTypeNumArray
    for x in container:
        for i in range(0, len(x)): 
            res_list.append(x[i] + ballTypeNumArray[i]) 
        ballTypeNumArray = res_list
        res_list = []
    return ballTypeNumArray


# Complete the organizingContainers function below.
def organizingContainers(container):

    numOfContainers = len(container)
    totalBallTypes = len(container[0] if numOfContainers else [])
    containerBallCapacity = []

    for cont in container:
        containerBallCapacity.append(containerCapacity(cont))

    ballTypeNumArray = ballTypeTotalArray(container, totalBallTypes)

    print('BallTypeNumberArray : ', ballTypeNumArray)
    print('Container capacityOfBalls : ', containerBallCapacity)
    print('numOfContainers, Total Ball Types : ', numOfContainers, totalBallTypes)

    ballTypeNumArray.sort()
    containerBallCapacity.sort()

    if (ballTypeNumArray == containerBallCapacity):
        return possibility.POSSIBLE.value

    print('ballArray, contArray :', ballTypeNumArray, containerBallCapacity)

    return possibility.IMPOSSIBLE.value


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('F:\hackerRankPython\\ballTypePerContainer\output.txt', 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
