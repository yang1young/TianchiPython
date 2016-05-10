#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/6 上午9:46
# @Author  : Li Yaxi
import pandas as pd
from sklearn import linear_model
from scipy import stats
from PaperUtil import getBeginOfMonth,getDataFromDate,getGroupDict,getRootMSE,getBetaEpsilon,getGroupsListByGroup,getTTest
import numpy as np
group_dict = {}
n_list = [48,48,48,48,48,48,48,48,18]
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
def getR1R2R3(dataframe):
    flag = 0
    resutl_list = []
    for i,j in dataframe.groupby(['group_id']):
        # print j
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
        print beta[0],intercept
        break

    return resutl_list

#第二步
def third_step(startDate,endDate,thirdPathName):
    global group_dict
    dataframe3 = getDataFromDate("filteredData.csv", startDate,endDate)
    group_dict = getGroupDict(thirdPathName)
    dataframe3['group_id'] = dataframe3.PERMNO.map(lambda x: get_group_id(x))
    dataframe3 = dataframe3[dataframe3['group_id']!=-1]
    file3 = open(thirdPathName,"wb+")
    second_result = getBetaEpsilon(thirdPathName)
    # second_result = [1,2]
    months = getBeginOfMonth(startDate,endDate)

    file3.writelines("Date,R0,R1,R2"+'\n')
    R0 = []
    R1 = []
    R2 = []
    for i in months:

        X = []
        Y = []
        for k,l in dataframe3.groupby("group_id"):
            l = l[l['DATE'].map(lambda x:x/100==(i/100))]
            key = str(i)[0:6]+"_"+str(k)
            value = second_result[key]
            X.append([value[0],value[1]])
            Y.append(float(l.RET.mean()))
        clf.fit(X, Y)
        beta = clf.coef_
        intercept = clf.intercept_
        print i,intercept,beta[0],beta[1]
        R0.append(intercept)
        R1.append(beta[0])
        R2.append(beta[1])
        print i
        file3.writelines(str(i)[0:6]+","+str(intercept)+","+str(beta[0])+","+str(beta[1])+'\n')


    file3.writelines("mean R0: "+ str(np.mean(R0))+'\n')
    file3.writelines("mean R1: "+ str(np.mean(R1))+'\n')
    file3.writelines("mean R2: "+ str(np.mean(R2))+'\n')

    file3.writelines("std R0: "+ str(np.std(R0))+'\n')
    file3.writelines("std R1: "+ str(np.std(R1))+'\n')
    file3.writelines("std R2: "+ str(np.std(R2))+'\n')
    file3.writelines("t R0: "+ str(getTTest(R0,int(n_list[int(thirdPathName.split('-')[0])-1])))+'\n')
    file3.writelines("t R1: "+ str(getTTest(R1,int(n_list[int(thirdPathName.split('-')[0])-1])))+'\n')
    file3.writelines("t R2: "+ str(getTTest(R2,int(n_list[int(thirdPathName.split('-')[0])-1])))+'\n')

    # file3.writelines("ttest R1: "+ str(stats.t(R1))+'\n')
    # file3.writelines("ttest R2: "+ str(stats.t(R2))+'\n')
    # file3.writelines("ttest R3: "+ str(stats.t(R3))+'\n')

if __name__ == '__main__':
    third_step(19350101,19390101,'1-3.csv')
    third_step(19390101,19430101,'2-3.csv')
    third_step(19430101,19470101,'3-3.csv')
    third_step(19470101,19510101,'4-3.csv')
    third_step(19510101,19550101,'5-3.csv')
    third_step(19550101,19590101,'6-3.csv')
    third_step(19590101,19630101,'7-3.csv')
    third_step(19630101,19670101,'8-3.csv')
    third_step(19670101,19680701,'9-3.csv')
