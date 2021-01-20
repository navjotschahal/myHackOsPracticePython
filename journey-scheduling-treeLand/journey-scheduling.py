#!/bin/python3

#    https://www.hackerrank.com/challenges/journey-scheduling/problem

import os
import sys

# Graph creator method
# Creates Graph for n citys with a list of direct roads between the citys
def graphCreator(n: int, roads: list):
    pathDict: dict = {}
    for city in range(1, n+1):
        pathDict[str(city)] = []
        for j in roads:
            if city == j[0]:
                pathDict[str(city)].append(j[1])
        for j in roads:
            if city == j[1]:
                pathDict[str(city)].append(j[0])
    return pathDict
    
# Distance finder
def distanceFinder(city: int, pathDict: dict, pCity: int):
    print('For city : ', city)
    dArray
    d = 0
    for c in pathDict[str(city)]:
        return 0 if pCity == c else (d + distanceFinder(c, pathDict, city))


#
# Complete the journeyScheduling function below.
#
def journeyScheduling(n, roads, journeys):
    listOfJdist: list = []
    print('Total number of cities :', n)
    print('Roads :', roads)
    print('Journeys :', journeys)

    pathDict: dict = graphCreator(n, roads)
    print(pathDict)

    for j in journeys:
        print(distanceFinder(j[0], pathDict, -1))

    return listOfJdist

if __name__ == '__main__':
    fptr = open('F:\hackerRankPython\journey-scheduling-treeLand\jurneyPlannedDist.txt', 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = input().split()
    nm = '8 7'.split()
    ##

    n = int(nm[0])

    m = int(nm[1])

    roads = []

    for _ in range(n-1):
        # roads.append(list(map(int, input().rstrip().split())))
        continue
        ##

    journeys = []

    for _ in range(m):
        # journeys.append(list(map(int, input().rstrip().split())))
        continue
        ##

    # result = journeyScheduling(n, roads, journeys)
    result = journeyScheduling(
        8,
        [[2, 1], [3, 2], [4, 2], [5, 1], [6, 1], [7, 1], [8, 7]],
        [[4, 6], [3, 4], [6, 3], [7, 6], [4, 6], [7, 1], [2, 6]]
        )
    ##

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
