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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:26:47 2021

@author: jimleon

Estimate vs iteration plot for simAnnealing
"""

import matplotlib.pyplot as plt

def plotEstVsIteration(pointArray):
    i = 0
    while i < (len(pointArray)-1):
        x = [i,i+1]
        y = [pointArray[i],pointArray[i+1]]
        plt.plot(x,y,'black','-')
        i = i + 1
    plt.grid()
    plt.axis([0,len(pointArray),0.0,1.0])
    plt.yticks([0.0,0.5,1.0,1.5],[0,0.5,1.0,1.5])
    plt.xlabel('Iterations')
    plt.ylabel('Eval(x)')
    plt.title('Eval(x) vs Iterations')
    plt.show()
    return