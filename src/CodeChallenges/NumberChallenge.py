#!/bin/python3

import math
import os
import random
import re
import sys

def isOdd(a):
    return a%2!=0

def inclusive25(a):
    return (a>=2 and a<=5)

def inclusive620(a):
    return (a>=6 and a<=20)

if __name__ == '__main__':
    n = int(input().strip())

    if n>=1 and n<=100:
        if isOdd(n): # Es par
            print("Weird")
        else: # Es impar
            if (n>=2 and n<=5):
                print("Not Weird")
            elif(n>=6 and n<=20):
                print("Weird")
            elif(n>20):
                print("Not Weird")
    else:
        print("Numero debe ser entre 1 y 100")

