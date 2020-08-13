#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    final = []

    for grade in grades:
        if not (grade% 5 == 0):
            if grade<38:
                final.append(grade)
                continue
            for i in range(grade,101):
                if (i%5 == 0):
                    final_grad = i
                    break
            if((final_grad-grade)<3):
                final.append(final_grad)
            else:
                final.append(grade)
        else:
            final.append(grade)
    return final
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
