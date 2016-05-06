#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/4/27 下午7:42
# @Author  : ZHZ

line1 = raw_input()
n = line1.strip().split()[0]
K = line1.strip().split()[1]
string_list = []
all_str_list = []
count = 0
#得到所有字符串字典
for i in range(0,int(n)):
    line = raw_input().strip()
    string_list.append(line.strip())

#递归全排列，start 为全排列开始的下标， length 为str数组的长度
def AllRange(str,str_list,start,length):
    if start == length-1:
        all_str_list.append(str+str_list[start])
    else:
        for i in range(start,length):
            (str_list[i],str_list[start]) = (str_list[start],str_list[i])
            AllRange(str+str_list[start],str_list,start+1,length)
            (str_list[i],str_list[start]) = (str_list[start],str_list[i])


AllRange("",string_list,0,int(n))
all_str_set = set(all_str_list)

def leftString(string):
    string = string[1:-1]+string[-1]+string[0]
    return string


for str in all_str_list:
    temp_count = 0
    temp_str = str
    for i in range(1,len(temp_str)+1):
        temp_str = leftString(temp_str)
        if temp_str==str:
            temp_count = temp_count+1
    if temp_count==int(K):
        count = count+1

print count
'''
3 2
AB
RAAB
RA
'''