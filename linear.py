#y=ax+b
import  tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#参数
learning_rate=0.01#训练速度
training_epochs=1800 #训练次数
display_step=50 #显示速度

train_x=np.linspace(0,10,num =20) +np.random.randn(20)#数组，1唯20个
train_y=np.linspace(1,4,num=20)   +np.random.randn(20)
print(train_x,train_y) #数据
print(train_x.shape,train_y.shape) #形状
n_samples=train_x.shape[0] #样本的数量
print(n_samples)
#plt.scatter(train_x,train_y)绘制散点图
#plt.show()


# y=f(x)=w*x+b  #线性回归
X=tf.placeholder("float")
Y=tf.placeholder("float")
W=tf.Variable(np.random.randn(),name ="weight") 
B=tf.Variable(np.random.randn(),name ="bias")

a = tf.constant(10) #常量




 #初始化

def main(_): #tenforflow是个框架，python控制执行 ，_代表参数
    with  tf.Session() as sess:  #会话过程
        init = tf.global_variables_initializer()
        sess.run(init)#初始化
        print(sess.run(W),sess.run(B))  #默认初始值
        y_pred=tf.add(tf.multiply(X,W),B)
        print(sess.run(y_pred,feed_dict={X:0})) #赋值并计算
        print(sess.run(W),sess.run(B))
        print(sess.run(tf.reduce_sum(train_y)))#求和的方式，降唯
        
        
        cost=tf.reduce_sum(tf.pow(y_pred-Y,2))/n_samples #差的平方除以平均值，均误差
        optimzer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)#梯度下降的算法优化，损失最低



        for epoch  in range(training_epochs):#定义训练次数
            for (x_t,y_t) in zip(train_x,train_y):  #循环train_x,trian_y
                sess.run(optimzer,feed_dict={X:x_t,Y:y_t}) #训练
            if    epoch%100==0:#每循环100次，显示
                cost_t=sess.run(cost,feed_dict={X:train_x,Y:train_y}) #运行
                print("epoch",epoch,"cost",cost_t,
                      "W",sess.run(W),
                      "B",sess.run(B))
        print("执行OK")
        training_cost=sess.run(cost,feed_dict={X:train_x,Y:train_y})
        print("平均偏差")
        print("平均偏差", training_cost,
                      "W",sess.run(W),
                      "B",sess.run(B))
        plt.plot(train_x,train_y,"ro",label="old data")
        plt.plot(train_x,sess.run(W)*train_x+sess.run(B),
                 label="fit data")
        plt.legend()
        plt.show()





if __name__ == "__main__":
    tf.app.run() #执行过程