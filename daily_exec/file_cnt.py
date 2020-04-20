# coding=utf-8
#遍历文件夹下所有文件，并将文件名存入数组中
"""
import os
path = '/home/fandong/fandong/code/rubik'    #获取当前路径
count = 0
for root,dirs,files in os.walk(path):    #遍历统计
      for each in files:
             count += 1   #统计文件夹下文件个数
print (count)               #输出结果

for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root,file))
"""
print([]is None)