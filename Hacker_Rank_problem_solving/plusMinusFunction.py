#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    lenght = len(arr)
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for i in arr:
        if i < 0:
            count_neg += 1
        elif i > 0:
            count_pos += 1
        else:
            count_zero += 1
    prop_pos = count_pos / lenght
    prop_neg = count_neg / lenght
    prop_zero = count_zero / lenght

    print('%.6f'%prop_pos)
    print('%.6f'%prop_neg)
    print('%.6f'%prop_zero)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
