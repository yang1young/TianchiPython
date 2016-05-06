#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/24 下午3:47
# @Author  : ZHZ
from decimal import Decimal

all_kid_percent = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/all_kid_percent.csv","r")
result_20160434_6000 = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/result_20160505_6000.csv","wb+")
result_20160434_1000 = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/result_20160505_1000.csv","r")
item_id = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/item_id.csv","r")
last14records = open("/Users/zhuohaizhen/PycharmProjects/Tianchi_Python/Data/Last14Records.csv", 'r')

percent_dict = {}
id_dict = {}
last14_sample_final_dict = {}


def get_percent_dict():
    for line in all_kid_percent.readlines():
        line = line.strip()
        line_list = line.split(",")
        key_all = str(line_list[0])+"_all"
        value_all = str(line_list[1])
        key_1 = str(line_list[0])+"_1"
        value_1 = str(line_list[2])
        key_2 = str(line_list[0])+"_2"
        value_2 = str(line_list[3])
        key_3 = str(line_list[0])+"_3"
        value_3 = str(line_list[4])
        key_4 = str(line_list[0])+"_4"
        value_4 = str(line_list[5])
        key_5 = str(line_list[0])+"_5"
        value_5 = str(line_list[6])
        percent_dict[key_all] = value_all
        percent_dict[key_1] = value_1
        percent_dict[key_2] = value_2
        percent_dict[key_3] = value_3
        percent_dict[key_4] = value_4
        percent_dict[key_5] = value_5
    print percent_dict
    print len(percent_dict)


def getLast14_sample_dict():
    for line in last14records.readlines():
        line = line.strip()
        key = str(line.split(',')[0])+"_"+str(line.split(',')[1])
        value = line
        last14_sample_final_dict[key] = value
    print len(last14_sample_final_dict),"****"

def getID_dict():
    for line in item_id.readlines():
        line = line.strip()
        line_list = line.split(",")
        key = str(line_list[1])
        value = str(line_list[0])
        id_dict[key] = value
    print len(id_dict)

def get_result_20160434_6000():
    id = 0
    for line in result_20160434_1000.readlines():
        line,if_ok,num_records = line.strip().split(",")
        if if_ok=='0' or int(num_records)<=4:
            key_all = id_dict[str(id)]+'_all'
            key_1 = id_dict[str(id)]+'_1'
            key_2 = id_dict[str(id)]+'_2'
            key_3 = id_dict[str(id)]+'_3'
            key_4 = id_dict[str(id)]+'_4'
            key_5 = id_dict[str(id)]+'_5'
            if last14_sample_final_dict.has_key(key_all):
                result_20160434_6000.writelines(last14_sample_final_dict[key_all]+'\n')
            if last14_sample_final_dict.has_key(key_1):
                result_20160434_6000.writelines(last14_sample_final_dict[key_1]+'\n')
            if last14_sample_final_dict.has_key(key_2):
                result_20160434_6000.writelines(last14_sample_final_dict[key_2]+'\n')
            if last14_sample_final_dict.has_key(key_3):
                result_20160434_6000.writelines(last14_sample_final_dict[key_3]+'\n')
            if last14_sample_final_dict.has_key(key_4):
                result_20160434_6000.writelines(last14_sample_final_dict[key_4]+'\n')
            if last14_sample_final_dict.has_key(key_5):
                result_20160434_6000.writelines(last14_sample_final_dict[key_5]+'\n')
            id = id+1
            continue
        #line = line.strip()
        new_line = str(id_dict[str(id)])+",all,"+str(Decimal(float(line)).quantize(Decimal('0.00')))
        result_20160434_6000.writelines(new_line+'\n')
        for i in range(1,6):
            key = str(id_dict[str(id)])+"_"+str(i)
            new_line = str(id_dict[str(id)])+","+str(i)+","+\
                       str(Decimal(float(float(line)*float(percent_dict[key]))).quantize(Decimal('0.00')))
            result_20160434_6000.writelines(new_line+'\n')
        id = id+1


get_percent_dict()
getLast14_sample_dict()
getID_dict()
get_result_20160434_6000()
result_20160434_6000.close()