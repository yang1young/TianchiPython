#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/20 下午8:07
# @Author  : ZHZ

import pandas as pd
import numpy as np

sample = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/TestData/sample_submission.csv",'r')
test_submit = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                          "Data/TestData/test1_sample.csv",'r')
new_test_submit = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                          "Data/TestData/new_test1_sample.csv",'wb+')
test_submit_dict = {}

for line in sample.readlines():
    line_list = line.strip().split(",")
    key = str(line_list[0])+"_"+str(line_list[1])
    test_submit_dict[key] = 0


for line in test_submit.readlines():
    line_list = line.strip().split(",")
    key = str(line_list[0])+"_"+str(line_list[1])
    test_submit_dict[key] = line_list[2]

num = 0
for i in test_submit_dict:
    #line = i
    line = str(str(i).split("_")[0])+","+str(str(i).split("_")[1])+","+str(test_submit_dict[i])
    new_test_submit.writelines(line+'\n')
    print line
    num = num+1
print len(test_submit_dict)
print num
