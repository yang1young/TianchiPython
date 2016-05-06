#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/5 下午8:36
# @Author  : ZHZ
import pandas as pd
import numpy as np

# 得到时间范围内每个月的月初日期列表
def getBeginOfMonth(startDate,endDate):
    months = []
    if startDate>endDate:
        return months
    tempDate = startDate
    while(tempDate<=endDate):
        months.append(tempDate)
        tempDate = getNextMonth(tempDate)
    return months

#得到下个月月初数据
def getNextMonth(currentMonth):
    if currentMonth%10000/100<12:
        currentMonth = currentMonth+100
    else:
        currentMonth = currentMonth + 8900
    return currentMonth

#获得残差标准差
def getRootMSE(X,Y,beta,intercept):
    residules = []
    for i in range(0,len(Y)):
        x = X[i][0]
        y = Y[i]
        residules.append(float(y)-float(x)*beta-intercept)
    return np.std(residules)

# 得到分组数量情况
def getGroupList(companySum):
    groups = 20 #分为20组
    groups_list = []
    middle = companySum/groups
    start = (companySum-(groups-2)*middle)/2
    end = companySum-(groups-2)*middle - start

    groups_list.append(start)
    for i in range(1,groups-1):
        groups_list.append(middle)
    groups_list.append(end)
    return groups_list


#读取分组字典
def getGroupDict(fileName):
    newFileName = fileName.split('-')[0]+"-1.csv"
    group_dict = {}
    print newFileName
    group_file = open(newFileName,'r')
    group_file.readline()
    for line in group_file.readlines():
        line_list = line.strip().split(",")
        group_dict[int(line_list[0])] = int(line_list[1])
    return group_dict

# 得到指定目录指定时间数据
def getDataFromDate(filePath,startDate,endDate):
    df = pd.read_csv("filteredData.csv")
    df = df[df['DATE']<=endDate]
    df = df[df['DATE']>=startDate]
    return  df

# print getBeginOfMonth(19290101,19390101)
# print len(getGroupDict("1-2.csv"))
# print getRootMSE([[1],[2],[3]],[1,2,4],1.5,-0.66666666)