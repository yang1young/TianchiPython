#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/4 下午8:32
# @Author  : Li Yaxi
import pandas as pd
from sklearn import linear_model
from PaperUtil import getBeginOfMonth,getDataFromDate,getGroupDict,getRootMSE

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
    resutl_list = []
    for i,j in dataframe.groupby(['group_id']):
        X = []
        Y = []
        print "*******************"
        print j
        for k,m in j.groupby("DATE"):
            X.append([float(m.EWRETD.mean())])
            Y.append(float(m.RET.mean()))
        clf.fit (X, Y)
        beta = clf.coef_
        intercept = clf.intercept_
        epsilon = getRootMSE(X,Y,beta[0],intercept)
        resutl_list.append([i,beta[0],epsilon])
        # print resutl_list
        # break
    return resutl_list

#第二步计算
def second_step(startDate,endDate,secondPathName):
    global group_dict
    #读取数据
    period = (endDate-startDate)-50000
    months_start = getBeginOfMonth(startDate,startDate+period)
    months_end = getBeginOfMonth(endDate-period,endDate)
    dataframe2 = getDataFromDate("filteredData.csv", startDate,endDate)
    group_dict = getGroupDict(secondPathName)
    dataframe2['group_id'] = dataframe2.PERMNO.map(lambda x: get_group_id(x))
    dataframe2 = dataframe2[dataframe2['group_id']!=-1]
    file2 = open(secondPathName,"wb+")
    file2.writelines("Date,Group_id,Beta,Epsilon\n")
    for i in range(0,len(months_start)):
        dataframe = dataframe2[dataframe2['DATE']>=months_start[i]]
        dataframe = dataframe[dataframe['DATE']<=months_end[i]]
        resutl_list = getBetaAndCasu(dataframe)

        for j in range(0,len(resutl_list)):
            print months_end[i],resutl_list[j][0],resutl_list[j][1],resutl_list[j][2]
            file2.writelines(str(months_end[i])+','+str(resutl_list[j][0])+','
                             +str(resutl_list[j][1])+','+str(resutl_list[j][2])+'\n')
        print len(months_start),len(months_end)



if __name__ == '__main__':
    second_step(19300101,19390101,'1-2.csv')
    second_step(19340101,19430101,'2-2.csv')
    second_step(19380101,19470101,'3-2.csv')
    second_step(19420101,19510101,'4-2.csv')
    second_step(19460101,19550101,'5-2.csv')
    second_step(19500101,19590101,'6-2.csv')
    second_step(19540101,19630101,'7-2.csv')
    second_step(19580101,19670101,'8-2.csv')
    second_step(19620101,19710101,'9-2.csv')
