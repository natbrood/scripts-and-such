#!/bin/python3

import math
import os
import random
import re
import sys

#                                    My part
#                                    __________


#a,b,r = "","",""

class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght
        
    def area(self):
        return self.width*self.lenght
    
    pass

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius**2)
    
    pass
#                                    __________

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()
