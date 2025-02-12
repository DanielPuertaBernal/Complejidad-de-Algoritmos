#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    print("lista" + str(unsorted))
    n = len(unsorted)
    for j in range(n-1):
        for i in range(j + 1, n):
            #print(str(unsorted[j]) +">"+ str(unsorted[i + 1]) + " = " + str(unsorted[j] > unsorted[i + 1]))

            if unsorted[j] > unsorted[i]:
                aux = unsorted[j]
                unsorted[j] = unsorted[i]
                unsorted[i] = aux
        print("lista" + str(unsorted))
    return unsorted


if __name__ == '__main__':



    unsorted = [31415926535897932384626433832795,1,3,10,3,5]
    result = bigSorting(unsorted)
    print(result)
