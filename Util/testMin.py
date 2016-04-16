#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/13 上午10:47
# @Author  : ZHZ
from pandas import *
import numpy
from scipy.optimize import *

x_true = numpy.arange(0,10,0.1)
m_true = 2.5
b_true = 1.0
y_true = m_true*x_true + b_true

def func(params, *args):
    x = args[0]
    y = args[1]
    m, b = params
    y_model = m*x+b
    error = y-y_model
    return sum(error**2)

initial_values = numpy.array([1.0, 0.0])
mybounds = [(None,2), (None,None)]

print fmin_l_bfgs_b(func, x0=initial_values, args=(x_true,y_true), approx_grad=True)
print fmin_l_bfgs_b(func, x0=initial_values, args=(x_true, y_true), bounds=mybounds, approx_grad=True)
