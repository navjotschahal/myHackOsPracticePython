#!/bin/python3

import math
import os
import random
import re
import sys
import enum


class time_numerals_to_words(enum.Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    eleven= 11
    twelve = 12
    thirteen = 13
    fourteen = 14
    quarter = 15
    sixteen = 16
    seventeen = 17
    eighteen = 18
    nineteen = 19
    twenty = 20
    thirty = 30
    fourty = 40
    fifty = 50

    oClock = "o' clock"
    past = 'past'
    to = 'to'
    half_past = 'half past'

# Complete the timeInWords function below.
def timeInWords(h, m):
    time_word = ""
    if m == 0:
        time_word = time_numerals_to_words(h).name + " " + time_numerals_to_words.oClock.value
    elif m <= 30 and m >= 1:
        if m == 1:
            time_word = time_numerals_to_words(m).name + " minute past " + time_numerals_to_words(h).name
        elif m == 15:
            time_word = time_numerals_to_words(m).name + " " + "past " + time_numerals_to_words(h).name
        elif m == 30:
            time_word = time_numerals_to_words.half_past.value + " " + time_numerals_to_words(h).name
        elif m > 20:
            pastNum = m - m%10
            time_word = time_numerals_to_words(pastNum).name + " " + time_numerals_to_words(m%10).name + " minutes past " + time_numerals_to_words(h).name
        else:
            time_word = time_numerals_to_words(m).name + " minutes past " + time_numerals_to_words(h).name
    elif m > 30:
        m = 60 - m
        if m > 20:
            pastNum = m - m%10
            time_word = time_numerals_to_words(pastNum).name + " " + time_numerals_to_words(m%10).name + " minutes to " + time_numerals_to_words(h + 1).name
        elif m == 15:
            time_word = time_numerals_to_words(m).name + " to " + time_numerals_to_words(h + 1).name
        else:
            time_word = time_numerals_to_words(m).name + " minutes to " + time_numerals_to_words(h + 1).name
    else:
        pass
    return time_word

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('F:\hackerRankPython\\theTimeInWords\\theTimeInWords.txt', 'w')

    h = 0
    while h < 1 or h > 12:
        h = int(float(input("Enter h (1 to 12): ")))
        print("Validation passed." if h == int(h) and (h > 0 and h < 12) else "Please enter valid data!")

    m = int(input("Enter m (0 to 59): "))

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
