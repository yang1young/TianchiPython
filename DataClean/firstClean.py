#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/10 上午9:12
# @Author  : ZHZ

import pandas as pd
import numpy as np
conf = pd.read_csv("../Data/OriginData/config1.csv",header=None)
if1 = pd.read_csv("../Data/OriginData/item_feature1.csv",header=None)
isf1 = pd.read_csv("../Data/OriginData/item_store_feature1.csv",header=None)
sample = pd.read_csv("../Data/OriginData/sample_submission.csv",header=None)

def renameColumns():
    conf.columns = ['item_id','store_code','a_b']
    if1.columns = ['date','item_id','cate_id','cate_level_id','brand_id','supplier_id','pv_ipv','pv_uv','cart_ipv','cart_uv',
              'collect_uv','num_gmv','amt_gmv','qty_gmv','unum_gmv','amt_alipay','num_alipay','qty_alipay','unum_alipay','ztc_pv_ipv',
              'tbk_pv_ipv','ss_pv_ipv','jhs_pv_ipv','ztc_pv_uv','tbk_pv_uv','ss_pv_uv','jhs_pv_uv','num_alipay_njhs','amt_alipay_njhs','qty_alipay_njhs'
              ,'unum_alipay_njhs']
    isf1.columns = ['date','item_id','store_code','cate_id','cate_level_id','brand_id','supplier_id','pv_ipv','pv_uv','cart_ipv'
               ,'cart_uv','collect_uv','num_gmv','amt_gmv','qty_gmv','unum_gmv','amt_alipay','num_alipay','qty_alipay','unum_alipay'
               ,'ztc_pv_ipv','tbk_pv_ipv','ss_pv_ipv','jhs_pv_ipv','ztc_pv_uv','tbk_pv_uv','ss_pv_uv','jhs_pv_uv','num_alipay_njhs','amt_alipay_njhs'
               ,'qty_alipay_njhs','unum_alipay_njhs']
    sample.columns = ['item_id','store_code','target']

def saveToFile():
    conf.to_csv("../Data/OutputData/1_config1.csv")
    if1.to_csv("../Data/OutputData/1_if1.csv")
    isf1.to_csv("../Data/OutputData/1_isf1.csv")
    sample.to_csv("../Data/OutputData/1_sample.csv")


if __name__ == '__main__':
    renameColumns()
    saveToFile()
    print conf.columns
    print if1.columns
    print isf1.columns
    print sample.columns