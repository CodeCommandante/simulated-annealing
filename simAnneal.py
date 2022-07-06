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
Created on Sat Jan 23 00:13:43 2021

@author: jimleon

Runs the simulated annealing plot
"""
import matplotlib.pyplot as plt
import math
import random
import time
import estVSit

def calculateFunction(x):
    exp1 = -2*((x-0.1)/9)
    exp2 = math.pow(2,exp1)
    exp3 = math.pow(math.sin(5*math.pi*x),6)
    y = exp2*exp3
    return y

def perturbX(x):
    xPrime = x + random.uniform(-1,1)
    while xPrime >= 1 or xPrime <= 0:
        xPrime = x + random.uniform(-1,1)
    return xPrime

def annealing(plt, pointx, pointy):
    plt.plot(pointx, pointy, 'go')
    plt.annotate("Start",(pointx,pointy))
    plt.pause(0.0001)
    StartTime = time.perf_counter()
    PointArray = {}
    jumps = 0
    Temp = 1000
    checks = 0
    while Temp > 0.001:
        Newx = perturbX(pointx)
        Newy = calculateFunction(Newx)
        if (Newy > pointy) or (random.uniform(0,1) < math.exp((Newy-pointy)/Temp)):
            pointx = Newx
            pointy = Newy
            plt.plot(pointx,pointy,'y^')
            jumps = jumps + 1
            plt.pause(0.0001)
        Temp = Temp*0.99
        PointArray[checks] = pointy
        checks = checks + 1
    StopTime = time.perf_counter()
    TotalTime = StopTime - StartTime
    print("Global maximum estimate:  (",round(pointx,4),", ",round(pointy,4),")")
    print("Time elapsed:  ",round(TotalTime,2)," seconds" )
    print("Total optimizations:  ",jumps )
    print("Total iterations:  ",checks )
    print("Ratio (opts/its):  ",round((jumps/checks)*100,2),"%")
    return plt, pointx, pointy, PointArray

def plotTheFunction():
    xarray = []
    yarray = []
    x = 0.0
    while(x < 1):
        xarray.append(x)
        yarray.append(calculateFunction(x))
        x = x + 0.001
    plt.plot(xarray, yarray, '-')
    plt.title('Simulated Annealing')
    plt.xlabel('x')
    plt.ylabel('Eval(x)')
    return plt

def simAnneal():
    plt = plotTheFunction()
    pointx = random.uniform(0,1)
    pointy = calculateFunction(pointx)
    plt, pointx, pointy, PointArray = annealing(plt, pointx, pointy)
    plt.plot(pointx, pointy, 'ro')
    plt.annotate("Terminal",(pointx,pointy))
    plt.pause(0.001)
    plt.grid()
    plt.axis([0,1,0,1])
    plt.show()
    estVSit.plotEstVsIteration(PointArray)
    return 0

simAnneal()
