#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/17 上午8:57
# @Author  : ZHZ
import pandas as pd
import numpy as np


def showGroups():
    df = pd.read_csv("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/OutputData/2_isf2.csv",index_col=0)
    for i,j in df.groupby([df['cate_level_id'],df['cate_id']]):
        print i



