#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/22 上午9:10
# @Author  : ZHZ
# @Description : 过滤离群点,主要通过设置number或是设置百分比来


import pandas as pd
import numpy as np
item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv",index_col=0)
#item_store_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1.csv",index_col=0)

def filterOutlierByNum_max(dataframe,num_max=0,num_min=0):
    series_ascend = dataframe.qty_alipay_njhs.sort_values()
    dataframe = dataframe.drop(series_ascend.tail(num_max).index)
    dataframe = dataframe.drop(series_ascend.head(num_min).index)
    return dataframe

def filterOutlierByPercent(dataframe,percent_max,percent_min):
    num_max = int(len(dataframe)*percent_max)
    num_min = int(len(dataframe)*percent_min)
    return filterOutlierByNum_max(dataframe,num_max,num_min)





all_max = 0.01
all_min = 0.01
father_max = 0.01
father_min = 0.01
kid_max = 0.01
kid_min = 0.01
item_max = 0.01
item_min = 0.01


#全部商品的1%过滤掉
filtered_item_feature = filterOutlierByPercent(item_feature,all_max,all_min)
#filtered_item_feature = filterOutlierByPercent(item_store_feature,all_max,all_min)

print len(filtered_item_feature)
for i,j in filtered_item_feature.groupby([filtered_item_feature['cate_level_id']]):
    series_ascend = j.qty_alipay_njhs.sort_values()
    filtered_item_feature = filtered_item_feature.drop(series_ascend.tail(int(len(j)*father_max)).index)

print len(filtered_item_feature)
for i,j in filtered_item_feature.groupby([filtered_item_feature['cate_level_id']]):
    series_ascend = j.qty_alipay_njhs.sort_values()
    filtered_item_feature = filtered_item_feature.drop(series_ascend.head(int(len(j)*father_min)).index)


print len(filtered_item_feature)
for i,j in filtered_item_feature.groupby([filtered_item_feature['cate_level_id'],filtered_item_feature['cate_id']]):
    series_ascend = j.qty_alipay_njhs.sort_values()
    filtered_item_feature = filtered_item_feature.drop(series_ascend.tail(int(len(j)*kid_max)).index)

print len(filtered_item_feature)
for i,j in filtered_item_feature.groupby([filtered_item_feature['cate_level_id'],filtered_item_feature['cate_id']]):
    series_ascend = j.qty_alipay_njhs.sort_values()
    filtered_item_feature = filtered_item_feature.drop(series_ascend.head(int(len(j)*kid_min)).index)

print len(filtered_item_feature)
for i,j in filtered_item_feature.groupby([filtered_item_feature['cate_level_id'],filtered_item_feature['cate_id'],filtered_item_feature['item_id']]):
    series_ascend = j.qty_alipay_njhs.sort_values()
    filtered_item_feature = filtered_item_feature.drop(series_ascend.tail(int(len(j)*item_max)).index)

print len(filtered_item_feature)
for i,j in filtered_item_feature.groupby([filtered_item_feature['cate_level_id'],filtered_item_feature['cate_id'],filtered_item_feature['item_id']]):
    series_ascend = j.qty_alipay_njhs.sort_values()
    filtered_item_feature = filtered_item_feature.drop(series_ascend.head(int(len(j)*item_min)).index)

print len(filtered_item_feature)

filtered_item_feature.to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                             "Data/FilteredData/filtered_outlier_isf.csv",index=False)

print "*********"
'''
filtered_item_feature.to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                             "Data/FilteredData/filtered_outlier_if.csv",index=False)
'''
#print item_feature.qty_alipay_njhs.sort_values().tail(10)
#print filtered_item_feature.qty_alipay_njhs.sort_values().tail(5)
