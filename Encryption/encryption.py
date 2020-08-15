#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s_without_spaces: str = ''
    s_l: [str] = []
    for str_val in  s.split(' '):
        s_without_spaces += str_val
    effective_s_len = len(s_without_spaces)
    sqrt_effective_s_len = math.sqrt(effective_s_len)
    floor = int(sqrt_effective_s_len)
    ceil = floor + 1 if sqrt_effective_s_len - floor > 0 else floor
    for i in range(1000):
        if ceil * floor < effective_s_len and ceil > floor:
            floor += 1
        elif ceil * floor < effective_s_len and ceil == floor:
            ceil += 1
        elif ceil * floor >= effective_s_len:
            break
    ini: int = 0
    final = ceil
    resultStr = ''
    for i in range(floor):
        s_l.append(s_without_spaces[ini: final])
        ini = final
        final += ceil
    print('Row * Colum Mat array list : ', s_l)
    for i in range( ceil ):
        for sTemp in s_l:
            try:
                resultStr += sTemp[i]
            except:
                pass
            else:
                pass
        resultStr += ' '
    return resultStr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('F:\hackerRankPython\Encryption\encryptionOutput.txt', 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
