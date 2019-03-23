from random import randint,sample
data=[randint(-10,10)for i in range(10)]
print(data)
filter(lambda x:x>0,data)

#最快（列表解析）
[x for x in data if x>=0]

d={x:randint(60,100)for x in range(1,21)}
{k:v for k,v in d.items() if v>90}

s=set(data)
{x for x in s if x%3==0}

student=('jim',16,'male','jin@163.com')
NAME=0
AGE=1
SEX=2
EMAIL=3
print(student[NAME])
if student[AGE]>=18:
    pass
from collections import  namedtuple
Student=namedtuple('student',['name','age','sex','email'])
s=Student('jim',16,'male','jin@163.com')
s.name
s.age
s.sex
isinstance(s,tuple)

#统计元素出现频度
data=[randint(0,20) for i in range(30)]
c=dict.fromkeys(data,0)
for x in data:
    c[x]+=1

from collections import Counter
c2=Counter(data)
c2.most_common(3)

import re
txt=open('C:/Users/aeado/Desktop/a.txt').read()
C3=Counter(re.split('\W+',txt))
C3.most_common(10)

#字典利用中值大小排序
d={ x : randint(60,100)for x in 'xyzabc'}
sorted(zip(d.values(),d.keys()))

sorted(d.items(),key=lambda x :x[1])

#找到多个字典中的公共健
sample('abcdefg',randint(3,6))
res=[]
s1={x:randint(1,4)for x in sample('abcdefg',randint(3,6))}
s2={x:randint(1,4)for x in sample('abcdefg',randint(3,6))}
s3={x:randint(1,4)for x in sample('abcdefg',randint(3,6))}
for k in s1:
    if k in s2 and k in s3:
        res.append(k)


#让字典保持有序
from collections import OrderedDict
d=OrderedDict()
d['jim']=(1,35)
d['leo']=(2,37)
d['bob']=(3,40)

players=list('ABCDEFGH')
from time import time
d=OrderedDict()
start=time()
for i in range(8):
    #input()
    p=players.pop(randint(0,7-i))
    end=time()
    print(i+1,p,end-start)
    d[p]=(i+1,end-start)
print()
for k in d:
    print(k,d[k])

#历史纪录功能
from collections import deque
history=deque([],5)
N=randint(0,100)
def guess(k):
    if k==N:
        print(66)
        return True
    if k<N:
        print('xiao')
    else:
        print('big')
    return False
while True:
    line=input("输入：")
    if line.isdigit():
        k=int(line)
        history.append(k)
        if guess(k):
            break
    elif line=='history' or line=='h?':
        print(history)

import pickle