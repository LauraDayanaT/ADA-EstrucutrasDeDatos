#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Solucion
    pila = []
    max_area = 0
    h.append(0)
    
    for i in range(len(h)):
        while pila and h[i] < h[pila[-1]]:
            altura_edificio = h[pila.pop()]
            ancho = i if not pila else i - pila[-1] - 1
            max_area = max(max_area, altura_edificio * ancho)
        pila.append(i)
        
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
