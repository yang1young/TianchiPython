#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/19 下午3:17
# @Author  : ZHZ
import pandas as pd
import datetime
#20151228-20160110

config = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_config1.csv",index_col=0)
sample = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_sample.csv",index_col=0)
item_store_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv", index_col=0)
#没有加cost,记得加上
#item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_if2.csv", index_col=0)
item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv", index_col=0)
days_20141009 = datetime.datetime(2014, 10, 9)
days_20151228 = datetime.datetime(2015, 12, 28)
days_20160110 = datetime.datetime(2016, 01, 10)

days_20141228 = datetime.datetime(2014, 12, 28)
days_20150110 = datetime.datetime(2015, 01, 10)

item_store_feature['days_20141009'] = item_store_feature['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)
item_feature['days_20141009'] = item_feature['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

def filterItem(temp,days_start,days_end):

    #return
    start = (days_start-days_20141009).days
    end = (days_end-days_20141009).days
    temp = temp[temp['days_20141009']>=start]
    temp = temp[temp['days_20141009']<=end]
    return temp

#filtered_item_feature = filterItem(item_feature,days_20141228,days_20150110)
#filtered_item_store_feature = filterItem(item_store_feature,days_20141228,days_20150110)
filtered_item_feature = item_feature
filtered_item_store_feature = item_store_feature

#得到所有仓库的一个test结果,第一个test以均值来得到
def getAllStoreTestResult():
    item = []
    items = []
    for i,j in filtered_item_feature.groupby([filtered_item_feature['item_id']]):
        item.append(i)
        item.append('all')
        item.append(j.qty_alipay_njhs.sum()/28)
        items.append(item)
        item = []
        #break
        pd.DataFrame(items,columns=None).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/TestData/test1_sample_all.csv",index = None,columns=None)

#得到所有仓库的一个test结果,第一个test以均值来得到
def getKidStoreTestResult():
    item = []
    items = []
    for i,j in filtered_item_store_feature.groupby([filtered_item_store_feature['item_id'],
                                                    filtered_item_store_feature['store_code']]):
        #print j
        item.append(i[0])
        item.append(i[1])
        item.append(j.qty_alipay_njhs.sum()/28)

        items.append(item)
        print item
        item = []
        #break
        pd.DataFrame(items,columns=None).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/TestData/test1_sample_kid.csv",index = None,columns=None)


getAllStoreTestResult()
getKidStoreTestResult()




