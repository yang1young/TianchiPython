#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/23 下午10:08
# @Author  : ZHZ
from decimal import Decimal
import pandas as pd
item_ids = []
all_item_sum = {}
kid1_item_sum = {}
kid2_item_sum = {}
kid3_item_sum = {}
kid4_item_sum = {}
kid5_item_sum = {}

df_if = pd.read_csv('/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv',index_col=None)
df_isf = pd.read_csv('/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1.csv',index_col=None)
all_kid_percent = open('/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/all_kid_percent.csv','wb+')

for i,j in df_isf.groupby([df_isf['item_id'],df_isf['store_code']]):
    if i[1] ==1:
        kid1_item_sum[i[0]] = j.qty_alipay_njhs.sum()
    elif i[1] ==2:
        kid2_item_sum[i[0]] = j.qty_alipay_njhs.sum()
    elif i[1] ==3:
        kid3_item_sum[i[0]] = j.qty_alipay_njhs.sum()
    elif i[1] ==4:
        kid4_item_sum[i[0]] = j.qty_alipay_njhs.sum()
    elif i[1] ==5:
        kid5_item_sum[i[0]] = j.qty_alipay_njhs.sum()

for i,j in df_if.groupby([df_if['item_id']]):
    all_item_sum[i] = j.qty_alipay_njhs.sum()
    item_ids.append(i)

print len(kid1_item_sum),len(kid2_item_sum),len(kid3_item_sum),len(kid4_item_sum),len(kid5_item_sum)
print len(kid1_item_sum)+len(kid2_item_sum)+len(kid3_item_sum)+len(kid4_item_sum)+len(kid5_item_sum)
print len(all_item_sum)

line = "item_id,all,1,2,3,4,5"
all_kid_percent.writelines(line+'\n')
for i in item_ids:
    line = str(i)+','+'1,'
    j = all_item_sum[i]
    if kid1_item_sum.has_key(i):
        # line = line+str(float(kid1_item_sum[i])/float(j))+','
        line = line+str(Decimal(float(kid1_item_sum[i])/float(j)).quantize(Decimal('0.00')))+','
    else:
        line = line+"0"+','
    if kid2_item_sum.has_key(i):
        # line = line+str(float(kid2_item_sum[i])/float(j))+','
        line = line+str(Decimal(float(kid2_item_sum[i])/float(j)).quantize(Decimal('0.00')))+','

    else:
        line = line+"0"+','
    if kid3_item_sum.has_key(i):
        # line = line+str(float(kid3_item_sum[i])/float(j))+','
        line = line+str(Decimal(float(kid3_item_sum[i])/float(j)).quantize(Decimal('0.00')))+','
    else:
        line = line+"0"+','
    if kid4_item_sum.has_key(i):
        #line = line+str(float(kid4_item_sum[i])/float(j))+','
        line = line+str(Decimal(float(kid4_item_sum[i])/float(j)).quantize(Decimal('0.00')))+','
    else:
        line = line+"0"+','
    if kid5_item_sum.has_key(i):
        line = line+str(Decimal(float(kid5_item_sum[i])/float(j)).quantize(Decimal('0.00')))
    else:
        line = line+"0"

    all_kid_percent.writelines(line+'\n')
