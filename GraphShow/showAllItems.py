#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/17 上午9:06
# @Author  : ZHZ

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
#item_store_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv",index_col=0)
#item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv",index_col=0)
item_feature = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/FilteredData/filtered_outlier_if.csv")

#每天采样记录条数的图表
def saveDaysFigureToFile(df,filename):
    path = "/Users/zhuohaizhen/Desktop/Item/"
    df = pd.DataFrame(df['days_20141009'].value_counts())
    df.columns = ['num']
    df["days_20141009"] = df.index
    print df
    plt.plot(df.days_20141009,df.num)
    plt.savefig(path+str(filename).replace(",","_").replace("(","").replace(")","").replace(" ","")+".jpg")
    plt.close('all')

def save_father_kid_item_day_records(df,filename):
    print "****************"
    df = pd.DataFrame(df.days_20141009.value_counts())
    df.columns = ['records']
    df['date'] = df.index
    plt.plot(df.date,df.records,'ro')
    plt.savefig(filename)
    plt.close('all')

#每天非聚划算交易数量的图表
def save_father_kid_item_day_num(df,filename):
    print "****************"
    plt.plot(df.days_20141009,df.qty_alipay_njhs,'ro')
    plt.savefig(filename)
    plt.close('all')


#每天非聚划算交易数量的图表
def save_father_kid_day_records(df,filename):
    print "****************"
    df = pd.DataFrame(df['days_20141009'].value_counts())
    df.columns = ['num']
    df["days_20141009"] = df.index
    print df
    plt.plot(df.days_20141009,df.num,'ro')
    plt.savefig(filename)
    plt.close('all')

#每天非聚划算交易数量的图表
def save_father_kid_day_num(df,filename):
    print "****************"
    date = []
    date_sum = []
    date_sum2 = []
    sum = []
    for i,j in df.groupby([df['days_20141009']]):
        #num = j['qty_alipay_njhs'].count
        #print num
        date.append(i)
        sum.append(j.qty_alipay_njhs.sum())
        date_sum.append(i)
        date_sum.append(j.qty_alipay_njhs.sum())
        date_sum2.append(date_sum)
        date_sum = []
        print i
        print j.qty_alipay_njhs.sum()

        #print j.qty_alipay_njhs.describe().count
        #break
    #return
    plt.plot(date,sum,'ro')

    temp = pd.DataFrame(date_sum2,columns=['date','sum'])
    #print temp.to_csv(temp)
    #temp = pd.DataFrame.from_dict(date_sum2)
    temp.to_csv(filename.replace("jpg",'csv'),index=False)
    plt.savefig(filename)
    plt.close('all')

#每个子类每个商品每天的交易记录数
def father_kid_item_day_records():
    item_feature['days_20141009'] = item_feature.date
    days_20141009 = datetime.datetime(2014, 10, 9)
    item_feature['days_20141009'] = item_feature['days_20141009'].map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    for i,j in item_feature.groupby([item_feature['cate_level_id'],item_feature['cate_id'],item_feature['item_id']]):
        path = "/Users/zhuohaizhen/Desktop/data of cainiao/father_kid_item_day_records/"
        #j = filterOutlier.filterOutlierByPercent(j,0.01,0.01)
        path = path + str(i[0]) +"_"+ str(i[1])
        if not os.path.isdir(path):
            os.makedirs(path)
        print j.qty_alipay_njhs.value_counts()
        path = path+"/"+str(i[2])+"_"+str(len(j))+".jpg"
        print j.date.value_counts().size
        save_father_kid_item_day_records(j,path)
        #break

#每个子类每个商品每天的交易件数
def father_kid_item_day_num():
    item_feature['days_20141009'] = item_feature.date
    days_20141009 = datetime.datetime(2014, 10, 9)
    item_feature['days_20141009'] = item_feature['days_20141009'].map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    for i,j in item_feature.groupby([item_feature['cate_level_id'],item_feature['cate_id'],item_feature['item_id']]):
        path = "/Users/zhuohaizhen/Desktop/data of cainiao/father_kid_item_day_num/"
        #j = filterOutlier.filterOutlierByPercent(j,0.01,0.01)
        print str(i)+str(len(j))
        path = path + str(i[0]) +"_"+ str(i[1])
        if not os.path.isdir(path):
            os.makedirs(path)
        print j.qty_alipay_njhs.value_counts()
        #print j.qty_alipay_njhs.describe()
        #print j[['date','qty_alipay_njhs']]
        path = path+"/"+str(i[2])+".jpg"
        print j.date.value_counts().size
        save_father_kid_item_day_num(j,path)


#每一天每个子类的交易记录数量
def father_kid_day_records():
    item_feature['days_20141009'] = item_feature.date
    days_20141009 = datetime.datetime(2014, 10, 9)
    item_feature['days_20141009'] = item_feature['days_20141009'].map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    for i,j in item_feature.groupby([item_feature['cate_level_id'],item_feature['cate_id']]):
        path = "/Users/zhuohaizhen/Desktop/data of cainiao/the records of kid class every day/"
        #j = filterOutlier.filterOutlierByPercent(j,0.01,0.01)
        print str(i)+str(len(j))
        #path = path + str(i[0]) +"_"+ str(i[1])
        if not os.path.isdir(path):
            os.makedirs(path)
        print j.days_20141009.value_counts()
        print j.days_20141009.value_counts().size
        path = path+"/" +str(len(j)) +"_"+ str(i[0])+"_"+ str(i[1])+".jpg"
        save_father_kid_day_records(j,path)


#每一天每个子类的交易件数数量
def father_kid_day_num():
    item_feature['days_20141009'] = item_feature.date
    days_20141009 = datetime.datetime(2014, 10, 9)
    item_feature['days_20141009'] = item_feature['days_20141009']\
        .map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    for i,j in item_feature.groupby([item_feature['cate_level_id'],item_feature['cate_id']]):
        path = "/Users/zhuohaizhen/Desktop/data of cainiao/the sum of kid class'qty_alipay_njhs every day/"
        #j = filterOutlier.filterOutlierByPercent(j,0.01,0.01)
        print str(i)+str(len(j))
        if not os.path.isdir(path):
            os.makedirs(path)
        path = path+"/" +str(len(j)) +"_"+ str(i[0])+"_"+ str(i[1])+".jpg"
        save_father_kid_day_num(j,path)
        #break

#每一天每个父类的交易记录数量
def father_day_records():
    item_feature['days_20141009'] = item_feature.date
    days_20141009 = datetime.datetime(2014, 10, 9)
    item_feature['days_20141009'] = item_feature['days_20141009'].map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    for i,j in item_feature.groupby([item_feature['cate_level_id']]):
        path = "/Users/zhuohaizhen/Desktop/data of cainiao/the records of father class every day/"
        #j = filterOutlier.filterOutlierByPercent(j,0.01,0.01)
        print str(i)+str(len(j))
        if not os.path.isdir(path):
            os.makedirs(path)
        print j.days_20141009.value_counts()
        print j.days_20141009.value_counts().size
        path = path+"/" +str(len(j)) +"_"+ str(i)+".jpg"
        save_father_kid_day_records(j,path)


#每一天每个父类的交易件数数量
def father_day_num():
    item_feature['days_20141009'] = item_feature.date
    days_20141009 = datetime.datetime(2014, 10, 9)
    item_feature['days_20141009'] = item_feature['days_20141009'].map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    for i,j in item_feature.groupby([item_feature['cate_level_id']]):
        path = "/Users/zhuohaizhen/Desktop/data of cainiao/the sum of father class'qty_alipay_njhs every day/"
        print str(i)+str(len(j))
        if not os.path.isdir(path):
            os.makedirs(path)
        path = path+"/" +str(len(j)) +"_"+ str(i)+".jpg"
        save_father_kid_day_num(j,path)
        #break


father_day_records()
father_day_num()
father_kid_day_records()
father_kid_day_num()
father_kid_item_day_records()
father_kid_item_day_num()
