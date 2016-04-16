#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/13 上午10:51
# @Author  : ZHZ

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
    return x*2+3*y

initial_values = numpy.array([1.0, 0.0])
mybounds = [(0,2-y_true), (None,y_true)]

print fmin_l_bfgs_b(func, x0=initial_values)
print fmin_l_bfgs_b(func, x0=initial_values, args=(x_true, y_true), bounds=mybounds, approx_grad=True)
