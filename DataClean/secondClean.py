#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/24 下午1:38
# @Author  : ZHZ

import pandas as pd

if1  = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_if1.csv",index_col = 0)
# isf1  = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_isf1.csv",index_col = 0)
config = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/1_config1.csv",index_col = 0)

config_less_dic = {}
config_more_dic = {}

def getCost_dict():
    for i,j in config.groupby([config['item_id'],config['store_code']]):
        key = str(i[0])+'_'+str(i[1])
        value_less = j.a_b.max().split('_')[0]
        value_more = j.a_b.max().split('_')[1]
        config_less_dic[key] = value_less
        config_more_dic[key] = value_more


def addLessMoreTo_if():
    i = 0

if __name__ == '__main__':
    getCost_dict()
    print len(config_less_dic),len(config_more_dic)
