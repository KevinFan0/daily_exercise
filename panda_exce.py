#! /usr/bin/env python
# coding=utf-8
import pandas as pd
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=pd.DataFrame(data)
#print(frame)
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
# print(frame2.columns)
data2=[1,2,3,4,5]
df=pd.DataFrame(data2)
# print(df)



d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
data3 = [0,1,2,3,4]
s = pd.Series(data3)
df2 = pd.DataFrame(d)
# print (df2)

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print(df)
# Drop rows with label 0
df = df.drop(0)