#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/24 上午10:15
# @Author  : ZHZ
import pandas as pd
import datetime

item_store_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv", index_col=0)
item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv", index_col=0)

days_20141009 = datetime.datetime(2014, 10, 9)
num_days = 14
#item_store_feature['days_20141009'] = item_store_feature['date'].\
#    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)
item_feature['days_20141009'] = item_feature['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

result_data = []

for i,j in item_feature.groupby(item_feature['item_id']):
    temp = {}
    temp['item_id'] = i
    temp['store_code'] = 'all'
    index = j.sort_values('date').tail(num_days)
    temp['target'] = index.qty_alipay_njhs.sum()
    print temp
    result_data.append(temp)

for i,j in item_store_feature.groupby([item_store_feature['item_id'],item_store_feature['store_code']]):
    temp = {}
    temp['item_id'] = i[0]
    temp['store_code'] = i[1]
    index = j.sort_values('date').tail(num_days)
    temp['target'] = index.qty_alipay_njhs.sum()
    print temp
    result_data.append(temp)

result_if = pd.DataFrame(result_data,columns=['item_id','store_code','target']).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/Last14Records.csv",index = None,columns=None)