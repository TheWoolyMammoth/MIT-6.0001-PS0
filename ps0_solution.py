#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 04:21:51 2021

@author: joeywaner
"""
import numpy 

x_input = input("Enter a number x: ")
y_input = input("Enter a number y: ")
x = int(x_input)
y = int(y_input)
print("x to the power of y: ", x**y)
log_x = numpy.log2(x)
print("The log of x is ",log_x)