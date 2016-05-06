#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/24 下午2:28
# @Author  : ZHZ
# @Description  : 将predict行记录增加至1000条

import pandas as pd

num_days = 7
final_date = 444/num_days
if_all_predict = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/if_all_predict.csv",'r')
if_all_predict_1000 = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/if_all_predict_1000.csv",'wb+')
if_all_predict_dict = {}
temp_line = "0,0,0,0,0,0,0," \
            "0,0,0,0,0,0,0," \
            "0,0,0,0,0,0,0," \
            "0,0,0,0,0"
column_line = ""

is_first = True
for line in if_all_predict.readlines():
    if is_first:
        is_first = False
        if_all_predict_1000.writelines(line.strip()+'\n')
        continue

    line = line.strip()
    key = int(line.split(',')[1])
    value = line
    if_all_predict_dict[key] = value

for i in range(0,1000):
    if if_all_predict_dict.has_key(i):
        if_all_predict_1000.writelines(if_all_predict_dict[i]+'\n')
    else:
        if_all_predict_1000.writelines(str(final_date)+","+str(i)+","+temp_line+'\n')
