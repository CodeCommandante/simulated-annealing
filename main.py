"""    
    Program exploring stochastic search.
    Copyright (C) 2021  Jim Leon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#! /usr/bin/python3

"""
Created on Fri Jan 22 21:03:13 2021

@author: jimleon

Main executable for the hillclimbing algorithm
"""

import matplotlib.pyplot as plt
import math
import random

def calculateFunction(x):
    exp1 = -2*((x-0.1)/9)
    exp2 = math.pow(2,exp1)
    exp3 = math.pow(math.sin(5*math.pi*x),6)
    y = exp2*exp3
    return y

def getNextPoint(x, y):
    if calculateFunction(x - 0.001) > y:
        x = x - 0.001
        y = calculateFunction(x)
        return False, x, y
    if calculateFunction(x + 0.001) > y:
        x = x + 0.001
        y = calculateFunction(x)
        return False, x, y
    return True, x, y

def climbTheHill(plt, pointx, pointy):
    var = 0
    done = False
    plt.plot(pointx, pointy, 'go')
    plt.annotate('Start',(pointx,pointy))
    plt.pause(0.01)
    plt.show()
    plotTheFunction()
    plt.plot(pointx, pointy, 'go')
    plt.annotate('Start',(pointx,pointy))
    plt.title('Deterministic Hill Climb')
    while var < 1000 and done==False:
        plt.plot(pointx, pointy, 'y^')
        plt.pause(0.01)
        done, pointx, pointy = getNextPoint(pointx, pointy)
        var = var + 1
    plt.plot(pointx, pointy, 'ro')
    plt.annotate('Terminal',(pointx,pointy))
    plt.pause(0.01)
    return var, pointx, pointy

def plotTheFunction():
    xarray = []
    yarray = []
    x = 0.0
    while(x < 1):
        xarray.append(x)
        yarray.append(calculateFunction(x))
        x = x + 0.001
    plt.plot(xarray, yarray, '-')
    return plt

def main():
    plt = plotTheFunction()
    pointx = random.uniform(0,1)
    pointy = calculateFunction(pointx)
    TotalIterations, pointx, pointy = climbTheHill(plt, pointx, pointy)
    plt.show()
    print( "Global max:  (",pointx,", ",pointy,")")
    print( "Steps used to reach summit:  ",TotalIterations )
    return 0

main()
