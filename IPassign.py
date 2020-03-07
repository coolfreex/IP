#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/24 17:02
# @Author : so:Lo
# @File : Iptxt.py
#
#This script is to find all txt files inside current folder
#All the txt files made by masscan and all I need is to take IP address and port out
#
import re
import os
import sys
import time

localtime = time.asctime( time.localtime(time.time()) )


pattern = re.compile(r'(?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?')
pattern2 = re.compile(r'portid="\w+')

dir = input("输入路径：")

#print(dir)

filepath = dir

List = []


# find all txt file in this folder
def find_txt (path,List):
    filelist = os.listdir(path)
    for filename in filelist:
        de_path= os.path.join(path, filename)
        if os.path.isfile(de_path):
            if de_path.endswith(".txt"):
                List.append(de_path)
        else:
            find_txt(de_path, List)
    return List


# read all txt file and write into one file
def txt_read():
    for j in List:
        #print(j)
        with open (j, mode='r') as f:
            data = f.read()
            with open("results.txt", "a") as f2:
                f2.write(data)



# find all IP and port in txt file
def organize_ip():
    with open('results.txt', mode='r') as f:
        data = f.readlines()
        for line in data:
            result1 = pattern.findall(line)
            #print(result1)
            result2 = pattern2.findall(line)
            result3 = str(result2).replace('portid="', ':')
            data2 = str(result1) + result3
            #print(result1)
            final_result = str(data2).replace("['", '').replace("']", '').replace("[]", "")
            print(final_result)
            with open('ip_port.txt', mode='a') as f2:
                f2.write(final_result+'\r')
    with open('ip_port.txt',mode='a') as f3:
        f3.write(localtime)


def clear():
    jugde = input("是否清楚之前数据：是/否"+"\n")

    if jugde == "是":
       with open("ip_port.txt","w") as f4:
          f4.write("")
    else:
        pass


def run():
    clear()
    find_txt(filepath, List)
    txt_read()
    organize_ip()

if __name__ == '__main__':
    run()
