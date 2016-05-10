#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/25 下午7:46
# @Author  : ZHZ
# @Description  : 根据num_days去划分数据集并图表显示,默认值是14

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter
xmajorLocator = MultipleLocator(1)
xmajorLocator = MultipleLocator(1)

num_days = 14
sum_flag_temp = 0

days_20141009 = datetime.datetime(2014, 10, 9)
item_id_dict = {}
all_item_sum = []
kid_item_sum = []
count1 = []
count2 = []
new_father_kid_item_x = []

'''生成新的days_20141009列'''
filtered_outlier_if = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1_filtered_3std.csv");
filtered_outlier_if['days_20141009'] = filtered_outlier_if['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

filtered_outlier_isf = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1_filtered_3std.csv");
filtered_outlier_isf['days_20141009'] = filtered_outlier_isf['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

def countByDays_if(dataframe, start_day, end_day):

    if start_day > end_day:
        return None
    dataframe = dataframe[dataframe['days_20141009']>=start_day]
    dataframe = dataframe[dataframe['days_20141009']<=end_day]
    print dataframe[['date','qty_alipay_njhs']]

    if len(dataframe)<=0:
        return None
    per = float(num_days)/float(end_day-start_day+1)
    temp = {}
    temp['twoWeek'] = (end_day-1)/num_days
    temp['date'] = str(start_day)+"_"+str(end_day)
    temp['item_id'] = item_id_dict[int(dataframe.item_id.mean())]
    temp['qty'] = dataframe.qty_alipay_njhs.sum()*per
    print temp
    return temp

def TransferDataByDays_if():

    flag = 0
    for i,father_kid_item in filtered_outlier_if.groupby(['item_id']):
        first_day = father_kid_item.days_20141009.min()
        last_day = father_kid_item.days_20141009.max()
        flag_day = last_day
        father_kid_item  = father_kid_item.sort_values('days_20141009')
        new_father_kid_item_temp=[]
        while(flag_day>=first_day):
            flag_day = flag_day - num_days
            if (flag_day<=first_day):
                ff = countByDays_if(father_kid_item, first_day, flag_day+num_days)
            else:
                ff = countByDays_if(father_kid_item, flag_day+1, flag_day+num_days)
            if ff == None:
                print "这里有个None"
                continue
            new_father_kid_item_x.append(ff)
            new_father_kid_item_temp.append(ff)
        showGraph_all(new_father_kid_item_temp)
        # return
        new_father_kid_item_temp = []
        flag = flag+1
    print new_father_kid_item_x
    dataframe = pd.DataFrame(new_father_kid_item_x,columns=['twoWeek','date','item_id','qty'])
    dataframe.to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/if_all_14.csv",index = None,columns=None)
    return dataframe

def TransferDataByDays_isf():

    flag = 0
    for i,father_kid_item in filtered_outlier_isf.groupby(['item_id','store_code']):
        first_day = father_kid_item.days_20141009.min()
        last_day = father_kid_item.days_20141009.max()
        flag_day = last_day
        father_kid_item  = father_kid_item.sort_values('days_20141009')
        new_father_kid_item_temp=[]
        while(flag_day>=first_day):
            flag_day = flag_day - num_days
            if (flag_day<=first_day):
                ff = countByDays_if(father_kid_item, first_day, flag_day+num_days)
            else:
                ff = countByDays_if(father_kid_item, flag_day+1, flag_day+num_days)
            if ff == None:
                print "这里有个None"
                continue
            new_father_kid_item_x.append(ff)
            new_father_kid_item_temp.append(ff)
        showGraph_kid(new_father_kid_item_temp,i[1])
        new_father_kid_item_temp = []
        flag = flag+1
        # if flag>10:
        #     return
    print new_father_kid_item_x
    dataframe = pd.DataFrame(new_father_kid_item_x,columns=['twoWeek','date','item_id','qty'])
    dataframe.to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/if_all_14.csv",index = None,columns=None)
    return dataframe


def showGraph_kid(dataframe,store_code):
    if len(dataframe)<4:
        return
    df = pd.DataFrame(dataframe,columns=['twoWeek','date','item_id','qty'])
    plt.plot(df.twoWeek,df.qty)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.tick_params(labelright=True)
    plt.savefig('/Users/zhuohaizhen/Desktop/figure/'+str(df.item_id.max())+"_"+str(store_code)+".jpg")
    #plt.show()
    plt.close('all')


def showGraph_all(dataframe):
    if len(dataframe)<4:
        return
    df = pd.DataFrame(dataframe,columns=['twoWeek','date','item_id','qty'])
    plt.plot(df.twoWeek,df.qty)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.tick_params(labelright=True)
    plt.savefig('/Users/zhuohaizhen/Desktop/figure/'+str(df.item_id.max())+"_all"+".jpg")
    #plt.show()
    plt.close('all')


def transItemID():
    item_ids = filtered_outlier_if.item_id.value_counts().sort_values().index
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
TransferDataByDays_if()
TransferDataByDays_isf()