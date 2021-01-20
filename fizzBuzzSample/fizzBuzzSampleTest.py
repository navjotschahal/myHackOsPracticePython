#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    fizzBuzz: str = 'FizzBuzz'
    fizz: str = 'Fizz'
    buzz: str = 'Buzz'

    for i in range(1, n + 1):
        n3 = i%3
        n5 = i%5

        if n3 == 0 and n5 == 0:
            print(fizzBuzz)
        else:
            if n3 == 0 and n5 != 0:
                print(fizz)
            elif n5 == 0 and n3 != 0:
                print(buzz)
            else:
                print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
