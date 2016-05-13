#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/8 下午12:03
# @Author  : ZHZ

import pandas as pd
import datetime
from sklearn import linear_model
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

clf = linear_model.LinearRegression()

item_store_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1_filtered_3std.csv", index_col=0)
item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1_filtered_3std.csv", index_col=0);
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
item_store_feature['days_20141009'] = item_store_feature['date'].\
   map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)
item_feature['days_20141009'] = item_feature['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

result_data = []

def countDatafram(df):
    length = len(df)
    if length==0:
        return 0
    per =  (float)(num_days)/length
    sum = df.qty_alipay_njhs.sum()
    return sum*per

for i,j in item_feature.groupby(item_feature['item_id']):
    j = j[j['days_20141009']>444-num_days*5]
    if len(j)==0:
        continue
    x = []
    y = []
    j1 = j[j['days_20141009']>444-num_days*5]
    j1 = j1[j1['days_20141009']<=444-num_days*4]
    j2 = j[j['days_20141009']>444-num_days*4]
    j2 = j2[j2['days_20141009']<=444-num_days*3]
    j3 = j[j['days_20141009']>444-num_days*3]
    j3 = j3[j3['days_20141009']<=444-num_days*2]
    j4 = j[j['days_20141009']>444-num_days*2]
    j4 = j4[j4['days_20141009']<=444-num_days*1]
    j5 = j[j['days_20141009']>444-num_days*1]
    j5 = j5[j5['days_20141009']<=444-num_days*0]

    if(len(j5)!=0):
        x.append(1)
        x.append(2)
        x.append(3)
        x.append(4)
        x.append(5)
        y.append(countDatafram(j1))
        y.append(countDatafram(j2))
        y.append(countDatafram(j3))
        y.append(countDatafram(j4))
        y.append(countDatafram(j5))
    elif (len(j4)!=0):
        x.append(1)
        x.append(2)
        x.append(3)
        x.append(4)
        y.append(countDatafram(j1))
        y.append(countDatafram(j2))
        y.append(countDatafram(j3))
        y.append(countDatafram(j4))
    elif (len(j3)!=0):
        x.append(1)
        x.append(2)
        x.append(3)
        y.append(countDatafram(j1))
        y.append(countDatafram(j2))
        y.append(countDatafram(j3))
    else:
        continue
    clf.fit(x,y)
    temp = {}
    temp['item_id'] = i
    temp['store_code'] = 'all'
    if clf.predict(len(x)+1)<0:
        temp['target'] = 0
    else:
        temp['target'] = clf.predict(len(x)+1)
    print temp
    result_data.append(temp)


for i,j in item_store_feature.groupby(['item_id','store_code']):
    j = j[j['days_20141009']>444-num_days*5]
    if len(j)==0:
        continue
    x = []
    y = []
    j1 = j[j['days_20141009']>444-num_days*5]
    j1 = j1[j1['days_20141009']<=444-num_days*4]
    j2 = j[j['days_20141009']>444-num_days*4]
    j2 = j2[j2['days_20141009']<=444-num_days*3]
    j3 = j[j['days_20141009']>444-num_days*3]
    j3 = j3[j3['days_20141009']<=444-num_days*2]
    j4 = j[j['days_20141009']>444-num_days*2]
    j4 = j4[j4['days_20141009']<=444-num_days*1]
    j5 = j[j['days_20141009']>444-num_days*1]
    j5 = j5[j5['days_20141009']<=444-num_days*0]

    if(len(j5)!=0):
        x.append(1)
        x.append(2)
        x.append(3)
        x.append(4)
        x.append(5)
        y.append(countDatafram(j1))
        y.append(countDatafram(j2))
        y.append(countDatafram(j3))
        y.append(countDatafram(j4))
        y.append(countDatafram(j5))
    elif (len(j4)!=0):
        x.append(1)
        x.append(2)
        x.append(3)
        x.append(4)
        y.append(countDatafram(j1))
        y.append(countDatafram(j2))
        y.append(countDatafram(j3))
        y.append(countDatafram(j4))
    elif (len(j3)!=0):
        x.append(1)
        x.append(2)
        x.append(3)
        y.append(countDatafram(j1))
        y.append(countDatafram(j2))
        y.append(countDatafram(j3))
    else:
        continue
    clf.fit(x,y)
    temp = {}
    temp['item_id'] = i
    temp['store_code'] = str(i[1])
    if clf.predict(len(x)+1)<0:
        temp['target'] = 0
    else:
        temp['target'] = clf.predict(len(x)+1)

    print temp
    result_data.append(temp)

result_if = pd.DataFrame(result_data,columns=['item_id','store_code','target']).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/Last14Records_500.csv",index = None,columns=None)