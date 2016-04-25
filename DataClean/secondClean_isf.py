#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/16 上午8:53
# @Author  : ZHZ

import pandas as pd

#isf1 = pd.read_csv("../Data/OriginData/1_isf1.csv",index_col = 0)
#config = pd.read_csv("../Data/OriginData/1_config1.csv",index_col = 0)

isf1_dic = {}
config_dic = {}

isf1 = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1.csv",'r')
isf2 = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv",'wb+')
config1 = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_config1.csv",'r')

i = 0
for line in config1.readlines():
    list1 = line.strip().split(',')
    key = str(list1[1])+str(list1[2])
    config_dic[key] = list1[3]

for line in isf1.readlines():
    if i==0:
        line = line.strip() + ",less,more"
        i = 1
        isf2.writelines(line+'\n')
        continue
    list1 = line.strip().split(',')
    key  = str(list1[2])+str(list1[3])
    a_b = config_dic[key]
    line = line.strip() + ","+config_dic[key].split('_')[0]+"," + config_dic[key].split('_')[1]
    isf2.writelines(line+'\n')
    #print config_dic[key]

isf2.close()