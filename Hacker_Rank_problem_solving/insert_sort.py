#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    # for i in range(n-1 , 0, -1):
    #     temp = arr[i]
    #
    #     j = i - 1
    #     while  j>= 0:
    #         if (arr[j] > temp):
    #             arr[j + 1] = arr[j]
    #         else:
    #             arr[j] = temp
    #         # print(arr)
    #         j -= 1
    #     arr[j+1] = temp
    #     # arr[j+1] = temp
    #
    #     # if arr[j]<0 or j<0:
    #     #     arr[j] = temp

    # Traverse through 1 to len(arr)
    for i in range(n - 2, -1, -1):

        key = arr[i + 1]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = 0
        while j <= n - 2 and key < arr[j]:
            arr[j - 1] = arr[j]
            j += 1
        if (j > n - 2):
            arr[j - 1] = key

    print(arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
