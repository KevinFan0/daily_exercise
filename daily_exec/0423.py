#! /usr/bin/env python
# coding=utf-8
from datetime import datetime

def init(data):
    data['first']={}
    data['m'] = {}
    data['l'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data,*full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names)==2:names.insert(1,'')
        labels='first','m','l'
        for label,name in zip(labels,names):
            people=lookup(data,label,name)
            if people:
                people.append(full_name)
            else:
                data[label][name]=[full_name]

mynames={}
init(mynames)
store(mynames,"Magnus Lie Hetland","sun hao","ma hua teng")
# print(lookup(mynames,'m', ''))

"""
#参数练习
def story(**kwds):
    return 'once upon a time, there was a %(job)s called %(name)s.' % kwds
def power(x,y,*others):
    if others:
        print('received redundant parameters:',others)
    return pow(x,y)

def interval(start,stop=None,step=1):
    'imitates range() for step>0'
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

params=(5,)*2
# print(power(*params))
#
# print(interval(10))
# print(interval(3,12,4))

str="最近1个月被 1家机构以“贷前审批”原因查询"
str2=str.strip()
print(str2)
def match1(str):
    str.strip()
    print(str)
    j=str.find("月被")
    m=str.find("家机构")
    if j+2<m and str[j+2:m].isdigit():
        return str[j+2:m]
    return -1
print(match1(str))

str2="0200"
if str2.isdigit():
    print(int(str2))

result="1493110806000"
insert_time = datetime.fromtimestamp(int(result) // 1000).strftime("%Y-%m-%d %H:%M:%S")
print(insert_time)


userid=123
url="/v2/detail/%u" % userid
print(url)

str=".11"
str1=float(str)
str2=int(str1)
print(str2)
"""
import pandas as pd
columns={
    "userid",
    "id_number",
    "email"
}
columns1={
    "userId",
    "id",
    "email"
}
res={'age': 26, 'email': 'aaa', 'gender': 1, 'id_number': '342425199211220418', 'insert_time': '2007-06-21 09:41:36', 'phone': '18801613469', 'qq': '458043389', 'real_name': 'luopengfei', 'reg_step_id': 1, 'role': 1, 'update_time': '2017-11-18 14:28:35', 'user_name': 'sixi2014', 'userid': 123}
new_res={
    'userId':1233,
    'id':12345,
    'email':'aa'
}
df=pd.DataFrame(res,columns=columns,index=[0])
df_new=pd.DataFrame(new_res,columns=columns1,index=[0])
df_middle=df.merge(
    df_new,
    how="inner"
    )
# print(df_middle)
df_middle2=df.merge(
    df_new,
    left_on="email",
    right_on="id",
    how="left"
)
df_middle3=df_middle2.merge(
    df_middle,
    how="outer"
)
print(df_middle2)

"""
from datetime import datetime,timedelta
maxtime="2017-11-29 16:14:49"
if maxtime>(datetime.now()-timedelta(days=180)).strftime("%Y-%m-%d %H:%M:%S"):
    print(1)
else:
    print(0)

arr=[1,2,3,4,5]

str1=",".join(str(s) for s in arr)
print(str1)
"""