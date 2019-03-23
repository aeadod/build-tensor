#使用生成器函数实现可迭代对象 yield
class prime:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isprime(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i==0:
                return  False
        return  True
    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isprime(k):
                yield k
for x in  prime(1,100):
    print(x)

#反向迭代
class floatrange:
    def __init__(self,start,end,step=0.1):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):
        t=self.start
        while t<=self.end:
            yield t
            t+=self.step
    def __reversed__(self):
        t=self.end
        while t>=self.start:
            yield  t
            t-=self.step

for x in reversed(floatrange(1.0,4.0,0.5)):
    print(x)


#对迭代器做切片操作

from itertools import islice
f=open("C:/Users/aeado/Desktop/a.txt",'r')

islice(f,100,300)
for line in islice(f,100,300):
    print(line)
f.close()

#迭代多个对象

from random import  randint
chinese=[randint(60,100) for i in range(40)]
english=[randint(60,100) for i in range(40)]
math=[randint(60,100) for i in range(40)]
for i in range(len(math)):
    summ=chinese[i]+math[i]+english[i]

total=[]
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)

from itertools import  chain

c1=[randint(60,100) for i in range(40)]
c2=[randint(60,100) for i in range(40)]
c3=[randint(60,100) for i in range(40)]
count=0
for s in chain(c1,c2,c3):
    if s>90:
        count +=1
print(count)