#!/bin/python3

import math
import os
import random
import re
import sys


def mapToBinaries(s, n):
    binarized_array = []
    for k in range(n):
        if s[k] == 'U':
            binarized_array.append(1)
        else:
            binarized_array.append(-1)
    return binarized_array


def sumMap(binarized_array, n):
    sum_arr = []
    sum = 0
    for j in range(n):
        sum = binarized_array[j] + sum
        sum_arr.append(sum)
    return sum_arr


# Complete the countingValleys function below.
def countingValleys(n, s):
    binarized_array = mapToBinaries(s, n)
    sum_arr = sumMap(binarized_array, n)
    pos = 0
    valley_count = 0
    i = 0
    while i < n:
        if sum_arr[i] < 0:
            pos = i
            while sum_arr[pos + 1] < 0:
                pos = pos + 1
            valley_count = valley_count + 1
            i = pos + 1
        else:
            i = i + 1
    return valley_count


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)

