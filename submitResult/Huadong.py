#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/5 上午9:47
# @Author  : ZHZ
import pandas as pd
import numpy as np
import datetime

global sum_flag
num_days = 14
sum_flag_temp = 0
huadong = 14
days_20141009 = datetime.datetime(2014, 10, 9)
item_id_dict = {}
all_item_sum = []
kid_item_sum = []
count1 = []
count2 = []
flag = {}
flag['flag'] = False
filtered_outlier_if = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1_filtered_3std.csv");
filtered_outlier_if['days_20141009'] = filtered_outlier_if['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

nonworkday_list = {20141111,20141212,20141225,20150101,20150214,20150218,20150219,20150305,20150307,
                   20150308,20150405,20150501,20150502,20150503,20150510,20150601,
                   20150620,20150621,20150820,20150910,20150927,
                   20151001,20151002,20151003,20151004,20151005,20151006,20151007,
                   20151111,20151212,20151225,20160101
                   }


def getWeekdays(dataframe,startday,endday):
    temp = {}
    return_temp = {}
    temp['Week_1'] = 0
    temp['Week_2'] = 0
    temp['Week_3'] = 0
    temp['Week_4'] = 0
    temp['Week_5'] = 0
    temp['Week_6'] = 0
    temp['Week_7'] = 0
    temp['Valentine_Day'] = 0   # 2.14
    temp['Qingming_Day'] = 0    # 4.4/4.5
    temp['Christmas_Day'] = 0   # 12.25
    temp['Thanksgiving_Day'] = 0    # 2014.11.27 2015.11.26
    temp['Teacher_Day'] = 0     # 9.10
    temp['Women_Day'] = 0   # 3.8
    temp['National_Day'] = 0    # 10.1-10.7
    temp['Labour_Day'] = 0  # 5.1-5.3?
    temp['Dragon_Boat_Day'] = 0    #
    temp['Spring_Day'] = 0     #
    temp['NewYears_Day'] = 0 # 0101——0103
    temp['Nonworkdays'] = 0
    temp['Workdays'] = 0

    for i,j in dataframe.groupby(dataframe['date']):
        weekday = datetime.datetime(i/ 10000, i / 100 % 100, i % 100).weekday()
        key = "Week_"+str(weekday+1)
        temp[key] = temp[key] + 1
        if weekday!=6 and weekday!=5 and i in nonworkday_list:
            temp['Nonworkdays'] = temp['Nonworkdays']+1


    return_temp['Weekend'] = temp['Week_7']+temp['Week_6']
    return_temp['Nonworkdays'] = return_temp['Weekend']+temp['Nonworkdays']
    return_temp['Workdays'] = endday-startday+1-return_temp['Nonworkdays']

    return return_temp

def countByDays_if(dataframe, start_day, end_day):

    if start_day > end_day:
        return None,0
    huadong_dataframe = dataframe
    huadong_dataframe = huadong_dataframe[huadong_dataframe['days_20141009']>=(start_day+huadong)]
    huadong_dataframe = huadong_dataframe[huadong_dataframe['days_20141009']<=(end_day+huadong)]


    dataframe = dataframe[dataframe['days_20141009']>=start_day]
    dataframe = dataframe[dataframe['days_20141009']<=end_day]


    if len(dataframe)<=0:
        return None,0

    per = float(num_days)/len(dataframe)
    if(len(huadong_dataframe)==0 or dataframe.days_20141009.max()==444):
        huadong_per = 0
    elif(len(huadong_dataframe)<(num_days)/2):
        return None,0
    elif(len(huadong_dataframe)>0):
        huadong_per = (num_days)/float(len(huadong_dataframe))




    #print huadong_per,"***************"


    temp = getWeekdays(dataframe,start_day,end_day)
    temp['date'] = end_day+huadong
    temp['item_id'] = item_id_dict[int(dataframe.item_id.mean())]
    temp['cate_id'] = dataframe.cate_id.max()
    temp['cate_level_id'] = dataframe.cate_level_id.max()
    temp['brand_id'] = dataframe.brand_id.max()
    temp['supplier_id'] = dataframe.supplier_id.max()
    temp['pv_ipv'] = dataframe.pv_ipv.sum()*per
    temp['pv_uv'] = dataframe.pv_uv.sum()*per
    temp['cart_ipv'] = dataframe.cart_ipv.sum()*per
    temp['cart_uv'] = dataframe.cart_uv.sum()*per
    temp['collect_uv'] = dataframe.collect_uv.sum()*per
    temp['num_gmv'] = dataframe.num_gmv.sum()*per
    temp['amt_gmv'] = dataframe.amt_gmv.sum()*per
    temp['qty_gmv'] = dataframe.qty_gmv.sum()*per
    temp['unum_gmv'] = dataframe.unum_gmv.sum()*per
    temp['amt_alipay'] = dataframe.amt_alipay.sum()*per
    temp['num_alipay'] = dataframe.num_alipay.sum()*per
    temp['qty_alipay'] = dataframe.qty_alipay.sum()*per
    temp['unum_alipay'] = dataframe.unum_alipay.sum()*per
    temp['ztc_pv_ipv'] = dataframe.ztc_pv_ipv.sum()*per
    temp['tbk_pv_ipv'] = dataframe.tbk_pv_ipv.sum()*per
    temp['ss_pv_ipv'] = dataframe.ss_pv_ipv.sum()*per
    temp['jhs_pv_ipv'] = dataframe.jhs_pv_ipv.sum()*per
    temp['ztc_pv_uv'] = dataframe.ztc_pv_uv.sum()*per
    temp['tbk_pv_uv'] = dataframe.tbk_pv_uv.sum()*per
    temp['ss_pv_uv'] = dataframe.ss_pv_uv.sum()*per
    temp['jhs_pv_uv'] = dataframe.jhs_pv_uv.sum()*per
    temp['num_alipay_njhs'] = dataframe.num_alipay_njhs.sum()*per
    temp['amt_alipay_njhs'] = dataframe.amt_alipay_njhs.sum()*per
    temp['unum_alipay_njhs'] = dataframe.unum_alipay_njhs.sum()*per
    temp['qty_alipay_njhs'] = huadong_dataframe.qty_alipay_njhs.sum()*huadong_per
    temp['is_final'] = False

    sum_flag_temp = dataframe.qty_alipay_njhs.sum()*per
    if temp['date'] == (444+huadong):
        count2.append(0)
        temp['is_final'] = True

    if temp['is_final']==True:
        flag['flag'] = True
    return temp,sum_flag_temp


def TransferDataByDays_if():
    new_father_kid_item_x = []
    new_father_kid_item_all = []
    for i,father_kid_item in filtered_outlier_if.groupby([filtered_outlier_if['cate_level_id'],
                                            filtered_outlier_if['cate_id'],
                                            filtered_outlier_if['item_id']]):

        first_day = father_kid_item.days_20141009.min()
        last_day = father_kid_item.days_20141009.max()
        flag_day = last_day-num_days+1
        #print first_day,last_day
        father_kid_item  = father_kid_item.sort_values('days_20141009')

        while(flag_day>=first_day):
            flag_day = flag_day - 1
            if (flag_day<=first_day):
                temp,sum_flag_temp = countByDays_if(father_kid_item, first_day, flag_day+num_days)
            else:
                temp,sum_flag_temp = countByDays_if(father_kid_item, flag_day+1, flag_day+num_days)
            if temp == None:
                continue

            #temp['qty_alipay_njhs']  = sum_flag
            #sum_flag = sum_flag_temp
            new_father_kid_item_x.append(temp)
            new_father_kid_item_all.append(temp)
        if flag['flag']==False and last_day<444-num_days+1:
            print item_id_dict[temp['item_id']],"**************"
            new_temp = {"item_id":temp['item_id'],"date":(444+huadong),"pv_ipv":0,"pv_uv":0,"cart_ipv":0,"cart_uv":0,
            "collect_uv":0,"num_gmv":0,"amt_gmv":0,"qty_gmv":0,"unum_gmv":0,"amt_alipay":0,"num_alipay":0,"qty_alipay":0
                           ,"unum_alipay":0,
            "ztc_pv_ipv":0,"tbk_pv_ipv":0,"ss_pv_ipv":0,"jhs_pv_ipv":0,"ztc_pv_uv":0,"tbk_pv_uv":0,"ss_pv_uv":0,"jhs_pv_uv":0
                           ,"num_alipay_njhs":0,
            "amt_alipay_njhs":0,"unum_alipay_njhs":0,"is_final":True,"qty_alipay_njhs":0}
            new_father_kid_item_all.insert(0,new_temp)
            new_father_kid_item_x.insert(0,new_temp)
        flag['flag'] = False

        new_father_kid_item_train = pd.DataFrame(new_father_kid_item_x,columns=[
            "item_id","date","pv_ipv","pv_uv","cart_ipv","cart_uv",
            "collect_uv","num_gmv","amt_gmv","qty_gmv","unum_gmv","amt_alipay","num_alipay","qty_alipay","unum_alipay",
            "ztc_pv_ipv","tbk_pv_ipv","ss_pv_ipv","jhs_pv_ipv","ztc_pv_uv","tbk_pv_uv","ss_pv_uv","jhs_pv_uv","num_alipay_njhs",
            "amt_alipay_njhs","unum_alipay_njhs","is_final","Workdays","qty_alipay_njhs"])

        #new_father_kid_item_train = new_father_kid_item_train[new_father_kid_item_train['is_final']==False]
        # new_father_kid_item_train.drop(["is_final"],axis = 1).\

        new_father_kid_item_train[new_father_kid_item_train['is_final']==False].drop(["is_final",'date'],axis = 1).\
            to_csv('/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/2016_05_05_3std/train'+str(item_id_dict[i[2]])+'_all.csv',index = None,columns=None)
        new_father_kid_item_x = []
        print item_id_dict[i[2]],i,"******************"
        print father_kid_item[['days_20141009','pv_ipv','qty_alipay_njhs']]
        # if(len(count2)==10):
        #     break
    print len(count1),len(count2)

    new_father_kid_item_all = pd.DataFrame(new_father_kid_item_all,columns=[
            "item_id","date","pv_ipv","pv_uv","cart_ipv","cart_uv",
            "collect_uv","num_gmv","amt_gmv","qty_gmv","unum_gmv","amt_alipay","num_alipay","qty_alipay","unum_alipay",
            "ztc_pv_ipv","tbk_pv_ipv","ss_pv_ipv","jhs_pv_ipv","ztc_pv_uv","tbk_pv_uv","ss_pv_uv","jhs_pv_uv","num_alipay_njhs",
            "amt_alipay_njhs","unum_alipay_njhs","is_final","Workdays","qty_alipay_njhs"])

    new_father_kid_item_all.to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/2016_05_05_3std/if_all.csv",index = None,columns=None)
    if_all_predict = new_father_kid_item_all[new_father_kid_item_all['is_final']].drop(["is_final"],axis = 1)

    if_all_predict = if_all_predict.sort_values('item_id').drop(["date"],axis = 1)
    # if_all_predict = new_father_kid_item_all.drop(["item_id"],axis = 1)
    if_all_predict.to_csv('/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/2016_05_05_3std/if_all_predict.csv',index = None,columns=None)

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
