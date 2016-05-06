#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/4 下午8:32
# @Author  : ZHZ
import pandas as pd
from sklearn import linear_model
from PaperUtil import getBeginOfMonth,getDataFromDate,getGroupDict,getRootMSE

months_start = getBeginOfMonth(19300101,19331201)
months_end = getBeginOfMonth(19350101,19381201)
group_dict = {}
clf = linear_model.LinearRegression()
X = []
Y = []
B = 0.00
result = {}

def get_group_id(x):
    if group_dict.has_key(x):
        return group_dict[x]
    else:
        return -1

# 得到Beta和残差标准差
def getBetaAndCasu(dataframe):
    flag = 0
    resutl_list = []
    for i,j in dataframe.groupby(['group_id']):
        print j
        flag = 0
        X = []
        Y = []
        for k,m in j.groupby("DATE"):
            flag = flag+1
            X.append([float(m.EWRETD.mean())])
            Y.append(float(m.RET.mean()))
        clf.fit (X, Y)
        beta = clf.coef_
        intercept = clf.intercept_
        epsilon = getRootMSE(X,Y,beta[0],intercept)
        resutl_list.append([i,beta[0],epsilon])
        print beta,intercept
        break

    return resutl_list

#第二步
def second_step(startDate,endDate,secondPathName):
    global group_dict
    dataframe2 = getDataFromDate("filteredData.csv", startDate,endDate)
    group_dict = getGroupDict(secondPathName)

    dataframe2['group_id'] = dataframe2.PERMNO.map(lambda x: get_group_id(x))
    print len(dataframe2[dataframe2['group_id']!=-1].PERMNO.value_counts())
    dataframe2 = dataframe2[dataframe2['group_id']!=-1]

    file2 = open(secondPathName,"wb+")
    file2.writelines("Date,Group_id,Beta,Epsilon\n")
    for i in range(0,len(months_start)):
        dataframe = dataframe2[dataframe2['DATE']>=months_start[i]]
        dataframe = dataframe[dataframe['DATE']<=months_end[i]]
        resutl_list = getBetaAndCasu(dataframe)
        for i in range(0,len(resutl_list)):
            file2.writelines(str(endDate)+','+str(resutl_list[i][0])+','
                             +str(resutl_list[i][1])+','+str(resutl_list[i][2])+'\n')
        break


if __name__ == '__main__':
    second_step(19300101,19381201,'1-2.csv')
