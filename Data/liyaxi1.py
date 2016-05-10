#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/4 下午8:32
# @Author  : Li Yaxi
import pandas as pd
from sklearn import linear_model
from PaperUtil import getGroupList,getDataFromDate


def first_step(startDate, endDate,groupfileName):
    dataframe1 = getDataFromDate("filteredData.csv", startDate,endDate)
    clf = linear_model.LinearRegression()
    X = []
    Y = []
    B = {}
    for i,j in dataframe1.groupby("PERMNO"):
        X = []
        Y = []
        for k,m in j.groupby("DATE"):
            X.append([float(j.EWRETD.min())])
            Y.append(float(j.RET.min()))
        clf.fit (X, Y)
        B[i] = clf.coef_
        print clf.coef_,len(B)

    A = sorted(B.items(), lambda x, y: cmp(x[1], y[1]))

    file = open(groupfileName,"wb+")
    group_length = getGroupList(len(A))

    flag = 0
    file.writelines('id,groupid'+'\n')
    for i in range(0,len(group_length)):
        for j in range(0,group_length[i]):
            file.writelines(str(A[flag][0])+","+str(i+1)+'\n')
            flag = flag+1


if __name__ == '__main__':
    first_step(19260101, 19300101,"1-1.csv")
    first_step(19270101, 19340101,"2-1.csv")
    first_step(19310101, 19380101,"3-1.csv")
    first_step(19350101, 19420101,"4-1.csv")
    first_step(19390101, 19460101,"5-1.csv")
    first_step(19430101, 19500101,"6-1.csv")
    first_step(19470101, 19540101,"7-1.csv")
    first_step(19510101, 19580101,"8-1.csv")
    first_step(19550101, 19620101,"9-1.csv")
