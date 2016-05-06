#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/23 下午2:50
# @Author  : ZHZ
# @Description  : 根据num_days去划分数据集,默认值是14

import pandas as pd
import numpy as np
import datetime

num_days = 14
days_20141009 = datetime.datetime(2014, 10, 9)
#filtered_outlier_if = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/FilteredData/filtered_outlier_if.csv");
filtered_outlier_if = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv");
filtered_outlier_if['days_20141009'] = filtered_outlier_if['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

#filtered_outlier_isf = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/FilteredData/filtered_outlier_isf.csv");
filtered_outlier_isf = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv");
filtered_outlier_isf['days_20141009'] = filtered_outlier_isf['date'].\
    map(lambda x:(datetime.datetime(x / 10000, x / 100 % 100, x % 100) - days_20141009).days)

def countByDays_if(dataframe, start_day, end_day):
    if start_day > end_day:
        return
    dataframe = dataframe[dataframe['days_20141009']>=start_day]
    dataframe = dataframe[dataframe['days_20141009']<=end_day]
    #print start_day,end_day,dataframe.date.sort_values().head(1),dataframe.days_20141009.max()
    temp = {}
    temp['date'] = str(dataframe.date.min())+"_"+str(dataframe.date.max())
    temp['item_id'] = dataframe.item_id.mean()
    temp['cate_id'] = dataframe.cate_id.mean()
    temp['cate_level_id'] = dataframe.cate_level_id.mean()
    temp['brand_id'] = dataframe.brand_id.mean()
    temp['supplier_id'] = dataframe.supplier_id.mean()
    temp['pv_ipv'] = dataframe.pv_ipv.sum()
    temp['pv_uv'] = dataframe.pv_uv.sum()
    temp['cart_ipv'] = dataframe.cart_ipv.sum()
    temp['cart_uv'] = dataframe.cart_uv.sum()
    temp['collect_uv'] = dataframe.collect_uv.sum()
    temp['num_gmv'] = dataframe.num_gmv.sum()
    temp['amt_gmv'] = dataframe.amt_gmv.sum()
    temp['qty_gmv'] = dataframe.qty_gmv.sum()
    temp['unum_gmv'] = dataframe.unum_gmv.sum()
    temp['amt_alipay'] = dataframe.amt_alipay.sum()
    temp['num_alipay'] = dataframe.num_alipay.sum()
    temp['qty_alipay'] = dataframe.qty_alipay.sum()
    temp['unum_alipay'] = dataframe.unum_alipay.sum()
    temp['ztc_pv_ipv'] = dataframe.ztc_pv_ipv.sum()
    temp['tbk_pv_ipv'] = dataframe.tbk_pv_ipv.sum()
    temp['ss_pv_ipv'] = dataframe.ss_pv_ipv.sum()
    temp['jhs_pv_ipv'] = dataframe.jhs_pv_ipv.sum()
    temp['ztc_pv_uv'] = dataframe.ztc_pv_uv.sum()
    temp['tbk_pv_uv'] = dataframe.tbk_pv_uv.sum()
    temp['ss_pv_uv'] = dataframe.ss_pv_uv.sum()
    temp['jhs_pv_uv'] = dataframe.jhs_pv_uv.sum()
    temp['num_alipay_njhs'] = dataframe.num_alipay_njhs.sum()
    temp['amt_alipay_njhs'] = dataframe.amt_alipay_njhs.sum()
    temp['qty_alipay_njhs'] = dataframe.qty_alipay_njhs.sum()
    temp['unum_alipay_njhs'] = dataframe.unum_alipay_njhs.sum()
    temp['days_20141009'] = str(dataframe.days_20141009.min())+"_"+str(dataframe.days_20141009.max())

    return temp

def TransferDataByDays_if():
    for i,father_kid_item in filtered_outlier_if.groupby([filtered_outlier_if['cate_level_id'],
                                            filtered_outlier_if['cate_id'],
                                            filtered_outlier_if['item_id']]):

        new_father_kid_item_data = []
        first_day = father_kid_item.days_20141009.min()
        last_day = father_kid_item.days_20141009.max()
        flag_day = first_day-1
        #print first_day,last_day

        father_kid_item  = father_kid_item.sort_values('days_20141009')

        #print father_kid_item[father_kid_item['days_20141009']==last_day]
        while(flag_day<=last_day):
            flag_day = flag_day + num_days
            if (flag_day>=last_day):
                temp = countByDays_if(father_kid_item, flag_day - num_days + 1, last_day)
            else:
                temp = countByDays_if(father_kid_item, flag_day - num_days + 1, flag_day)
            if temp ==None:
                print "这里有个None"
            else:
                new_father_kid_item_data.append(temp)

        new_father_kid_item = pd.DataFrame(new_father_kid_item_data,columns=[
            "date","item_id","cate_id","cate_level_id","brand_id","supplier_id","pv_ipv,pv_uv","cart_ipv,cart_uv",
            "collect_uv","num_gmv","amt_gmv","qty_gmv","unum_gmv","amt_alipay","num_alipay","qty_alipay","unum_alipay",
            "ztc_pv_ipv","tbk_pv_ipv","ss_pv_ipv","jhs_pv_ipv","ztc_pv_uv","tbk_pv_uv","ss_pv_uv","jhs_pv_uv","num_alipay_njhs",
            "amt_alipay_njhs","qty_alipay_njhs","unum_alipay_njhs"]
                                           ).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/FilteredData/item_all/"+str(i)+"_"+str(num_days)+"_all.csv",index = None,columns=None)

def TransferDataByDays_isf():
    for i,father_kid_item in filtered_outlier_isf.groupby([filtered_outlier_isf['cate_level_id'],
                                            filtered_outlier_isf['cate_id'],
                                            filtered_outlier_isf['item_id'],
                                            filtered_outlier_isf['store_code']]):

        new_father_kid_item_data = []
        first_day = father_kid_item.days_20141009.min()
        last_day = father_kid_item.days_20141009.max()
        flag_day = first_day-1
        #print first_day,last_day

        father_kid_item  = father_kid_item.sort_values('days_20141009')

        #print father_kid_item[father_kid_item['days_20141009']==last_day]
        while(flag_day<=last_day):
            flag_day = flag_day + num_days
            if (flag_day>=last_day):
                temp = countByDays_if(father_kid_item, flag_day - num_days + 1, last_day)
            else:
                temp = countByDays_if(father_kid_item, flag_day - num_days + 1, flag_day)
            if temp ==None:
                print "这里有个None"
            else:
                new_father_kid_item_data.append(temp)

        new_father_kid_item = pd.DataFrame(new_father_kid_item_data,columns=[
            "date","item_id","cate_id","cate_level_id","brand_id","supplier_id","pv_ipv,pv_uv","cart_ipv,cart_uv",
            "collect_uv","num_gmv","amt_gmv","qty_gmv","unum_gmv","amt_alipay","num_alipay","qty_alipay","unum_alipay",
            "ztc_pv_ipv","tbk_pv_ipv","ss_pv_ipv","jhs_pv_ipv","ztc_pv_uv","tbk_pv_uv","ss_pv_uv","jhs_pv_uv","num_alipay_njhs",
            "amt_alipay_njhs","qty_alipay_njhs","unum_alipay_njhs"]
                                           ).to_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/"
                                        "Data/FilteredData/item_kid/"+str(i)+"_"+str(num_days)+"_"+str(i[3])+".csv",index = None,columns=None)


TransferDataByDays_if()
TransferDataByDays_isf()
