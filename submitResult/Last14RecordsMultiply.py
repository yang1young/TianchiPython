#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/7 下午8:58
# @Author  : ZHZ

import pandas as pd
df = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1.csv",index_col = 0)
last14records = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/Last14Records.csv","r+")
resutl_14Multiply = open("resutl_14Multiply.csv","wb")
percent = {}
last14_sample_final_dict = {}
last14records_all = {}
last14records_kid = {}


def getLast14_sample_dict():
    for line in last14records.readlines():
        line = line.strip()
        key = str(line.split(',')[0])+"_"+str(line.split(',')[1])
        value = line
        last14_sample_final_dict[key] = value
    print len(last14_sample_final_dict),"****"

getLast14_sample_dict()

for i,j in df.groupby("item_id"):
    for k,m in j.groupby("store_code"):
        m = m.sort_values("date")
        # print m[['date','qty_alipay_njhs']]
        last = m.tail(28).qty_alipay_njhs.sum()
        this = m.tail(14).qty_alipay_njhs.sum()
        key = str(i)+"_"+str(k)
        if this==0:
            percent[key] = 0
        else:
            percent[key] = (float)(last-this)/this
        num = percent[key]* this
        resutl_14Multiply.writelines(str(i)+","+str(k)+","+str(num)+"\n")
        if last14records_all.has_key(i):
            last14records_all[i] = last14records_all[i]+num
        else:
            last14records_all[i] = num




for i in last14records_all:
    num = last14records_all[i]
    line = str(i) + "," + "all" + "," +str(num)
    resutl_14Multiply.writelines(line+"\n")