#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/16 下午3:21
# @Author  : ZHZ

i
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def showCate_id(cateID,number):
    df = pd.read_csv("2_isf2.csv",index_col=0)
    df39 = df[df['cate_id']==cateID]
    df39_date = df39.date.value_counts()
    df39_date.sort_index()
    df39_date = pd.DataFrame(df39_date)
    df39_date.columns = ['num']
    df39_date['date'] = df39_date.index
    days_20141009 = datetime.datetime(2014, 10, 9)
    df39_date['days_20141009'] = df39_date['date'].map(lambda x:(datetime.datetime(x/10000,x/100%100,x%100)-days_20141009).days)
    plt.plot(df39_date.days_20141009,df39_date.num,'ro')
    #plt.show()
    plt.savefig('/Users/zhuohaizhen/Desktop/figure/'+str(number)+"-"+str(cateID)+".jpg")
    plt.show()
    plt.close('all')

showCate_id(39,1)
showCate_id(26,2)
showCate_id(13,3)
showCate_id(17,4)
showCate_id(32,5)
showCate_id(21,6)
showCate_id(35,7)
showCate_id(37,8)
showCate_id(18,9)
showCate_id(7,10)
showCate_id(4,11)
showCate_id(20,12)
showCate_id(22,13)
showCate_id(14,14)
showCate_id(33,15)
showCate_id(11,16)
showCate_id(30,17)
showCate_id(25,18)
showCate_id(36,19)
showCate_id(19,20)
showCate_id(10,21)
showCate_id(16,22)
showCate_id(9,23)
showCate_id(15,24)
showCate_id(5,25)
showCate_id(23,26)
showCate_id(28,27)
showCate_id(24,28)