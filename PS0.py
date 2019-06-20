#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:52:51 2019

@author: max
"""

#PS0
#Ask user to enter number "x"
#Ask user to enter number "y"
#Print out number "x" raised to the power of "y"
#Print out the log (base 2) of "x"

#Ask user to enter number "x"
x = int(input("Please enter a number from 0-9 "))
#Ask user to enter number "y"
y = int(input("Please enter another number from 0-9 "))
#do x**y
z = x**y
#show x**y
print("X**y =",z)
#Load numpy for log
import numpy
#do log
logx = numpy.log2(x)
#show log2
print("Log(x) =",logx)