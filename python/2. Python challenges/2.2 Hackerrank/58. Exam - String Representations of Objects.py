#!/bin/python3

import math
import os
import random
import re
import sys

#                                    My part
#                                    __________

class Car:
    def __init__(self, carspeed, unit):
        self.carspeed = carspeed
        self.unit = unit
    
    def __str__(self):
        return "Car with the maximum speed of %s %s" % (self.carspeed,self.unit) 
    pass

class Boat:
    def __init__(self,boatspeed):
        self.boatspeed = boatspeed
        
    def __str__(self):
        return "Boat with the maximum speed of %s knots" % (self.boatspeed) 
    pass
#                                    __________

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
