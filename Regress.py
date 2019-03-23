import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

point_num=100
vectors=[]
#正太随机100个点，这些点的（X《Y）的坐标值对应线性方程y=0.1*x+0.2
#权重是0.1，偏差是0.2
for i in range(point_num):
    x1=np.random.normal(0.0,0.66)
    y1=0.1*x1+0.2+np.random.normal(0.0,0.04)
    vectors.append([x1,y1])

x_data=[v[0] for v in vectors]
y_data=[v[1] for v in vectors]

plt.plot(x_data,y_data,'r*',label='Orginal data')
plt.title('Linear Regression using Gradient Descent')
plt.show()

w =tf.Variable(tf.random_uniform([1],-1.0,1.0))
b=tf.Variable(tf.zeros([1]))
y=w*x_data+b
#模型计算的y

#损失函数

#计算y-y_data的平方的和/N
loss=tf.reduce_mean(tf.square(y-y_data))

#用梯度下降优化器优化loss
optimizer=tf.train.GradientDescentOptimizer(0.5)
#设置学习率0.5
train=optimizer.minimize(loss)

#创建会话
sess= tf.Session()

#初始化变量
init=tf.global_variables_initializer()
sess.run(init)

#训练20
for step in range(20):
    sess.run(train)
    #打印损失
    print(("step=%d,loss=%f,[weight=%f bias=%f]")\
    %(step,sess.run(loss),sess.run(w),sess.run(b)))

plt.plot(x_data,y_data,'r*',label='Orginal data')
plt.title('Linear Regression using Gradient Descent')
plt.plot(x_data,sess.run(w)*x_data+sess.run(b),label='Fitted line')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
sess.close()