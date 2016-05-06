#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/22 上午9:10
# @Author  : ZHZ
# @Description : 过滤离群点,主要通过3std原则来过滤


import pandas as pd
import numpy as np
if1 = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv",index_col=0)
print "orginal",if1.qty_alipay_njhs.mean(),len(if1)


def filteredDataframe(if1,name):
    for i,temp_df in if1.groupby([if1['cate_level_id'],if1['cate_id'],if1['item_id']]):
        mean_temp = temp_df.qty_alipay_njhs.mean()
        new_temp_fd = temp_df[np.abs(temp_df.qty_alipay_njhs-temp_df.qty_alipay_njhs.mean())>(2*temp_df.qty_alipay_njhs.std())]
        if1 = if1.drop(new_temp_fd.index)
        new_temp_fd.qty_alipay_njhs = mean_temp
        if1 = if1.append(new_temp_fd,ignore_index=True)
    if1.to_csv('/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/'+name,index=None,columns=None)
    print len(if1)
filteredDataframe(if1,"1_if1_filtered_2std.csv")
#filteredDataframe(isf1,"1_isf1_filtered.csv")