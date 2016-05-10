#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/8 下午12:03
# @Author  : ZHZ

import pandas as pd
import datetime

item_store_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv", index_col=0)
item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1_filtered_3std.csv");
item_id_dict = {}
def transItemID():
    item_ids = item_feature.item_id.value_counts().sort_values().index
    df_data = []
    for i in range(0,len(item_ids)):
        temp = {}
        temp['item_id'] = item_ids[i]
        temp['new_id'] = i
        item_id_dict[item_ids[i]] = i
        #print i,item_ids[i]
        df_data.append(temp)
    pd.DataFrame(df_data,columns=['item_id','new_id']).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/item_id.csv",index = None,columns=None)

transItemID()

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
    index = j.sort_values('date').tail(num_days/2)
    temp['target'] = index.qty_alipay_njhs.sum()*2
    print temp
    result_data.append(temp)


for i,j in item_store_feature.groupby(item_store_feature['item_id']):
    for k,l in j.groupby(j['store_code']):
        temp = {}
        temp['item_id'] = i
        temp['store_code'] = k
        index = j.sort_values('date').tail(num_days/2)
        temp['target'] = index.qty_alipay_njhs.sum()*2
        print temp
        result_data.append(temp)


# for i,j in item_store_feature.groupby([item_store_feature['item_id'],item_store_feature['store_code']]):
#     temp = {}
#     temp['item_id'] = i[0]
#     temp['store_code'] = i[1]
#     index = j.sort_values('date').tail(num_days)
#     temp['target'] = index.qty_alipay_njhs.sum()
#     print temp
#     result_data.append(temp)
# def cmp(i,j):
#     if int(i['item_id'])-int(j['item_id'])>0:
#         return 1
#     elif i['item_id'] ==j['item_id']:
#         return 0
#     else:
#
#         return -1
# result_data.sort(cmp)
result_if = pd.DataFrame(result_data,columns=['item_id','store_code','target']).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/Last14Records_500.csv",index = None,columns=None)