import numpy as np
import tensorflow as tf
#(55000*28*28)55000张训练图像
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets('mnist_data',one_hot=True)

input_x=tf.placeholder(tf.float32,[None, 28*28])/255
output_y=tf.placeholder(tf.int32,[None,10])#输出10个数字的标签
#NONE表示张良的有第一个维度是任意长度
input_x_images=tf.reshape(input_x,[-1,28,28,1])#改变形状

#从test数据集中选取3000个图片和对应标签
test_x=mnist.test.images[:3000]#图片
test_y=mnist.test.labels[:3000]#标签

#构建卷积神经网络
#第一层 5*5卷积，变成28*28*32
conv1=tf.layers.conv2d(
    inputs=input_x_images, #形状【28，28，1】
    filters=32,#32个卷积核，输出的深度是32
    kernel_size=[5,5],#卷积核大小
    strides=1,#步长
    padding='same',#表示输出的大小不变，在外围补零2圈
    activation=tf.nn.relu
)#形成【28,28,32】
#第一层池化（亚采样）
pool1=tf.layers.max_pooling2d(
    inputs=conv1,#28*28*32
    pool_size=[2,2],#过滤器大小
    strides=2#步长
)#形状【14，14，32】
#第二层卷积
conv2=tf.layers.conv2d(
    inputs=pool1, #形状【14，14，32】
    filters=64,#64个卷积核，输出的深度是32
    kernel_size=[5,5],#卷积核大小
    strides=1,#步长
    padding='same',#表示输出的大小不变，在外围补零2圈
    activation=tf.nn.relu
)#形成【14,14,64】
#第2层池化（亚采样）
pool2=tf.layers.max_pooling2d(
    inputs=conv2,#14*14*64
    pool_size=[2,2],#过滤器大小
    strides=2#步长
)#形状【7，7，64】
#平坦化（flat）
flat=tf.reshape(pool2,[-1,7*7*64])#变成7*7*64

#1024个神经元的全连接层
dense=tf.layers.dense(inputs=flat,units=1024,activation=tf.nn.relu)

#丢弃一半 rate=0.5
dropout=tf.layers.dropout(inputs=dense,rate=0.5)

#构建10个神经元的全连接层，不用激活函数非线性
logits=tf.layers.dense(inputs=dropout,units=10)
#输出1*1*10
#计算误差（Cross entropy 交叉熵），再用softmax计算百分比概率

loss=tf.losses.softmax_cross_entropy(onehot_labels=output_y,logits=logits)

#用Adam优化器来最小化误差，学习率0.001
train_op=tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

#计算预测值和标签的匹配程度
#返回(accuracy,update_op),会创建两个局部变量
accuracy=tf.metrics.accuracy(
    labels=tf.argmax(output_y,axis=1),
    predictions=tf.argmax(logits,axis=1),)[1]


#创建会话
sess=tf.Session()
#初始化全局和局部
init=tf.group(tf.global_variables_initializer(),tf.local_variables_initializer())
#运行
sess.run(init)
for i in range(20000):
    batch=mnist.train.next_batch(50)#从train数据集里取下一组50个样本
    train_loss,train_op_=sess.run([loss,train_op],{input_x:batch[0],output_y:batch[1]})
    if i%100==0:
        test_accuracy=sess.run(accuracy,{input_x:test_x,output_y:test_y})
        print('step=%d,train loss =%f,[test accuracy=%f]'%(i,train_loss,test_accuracy))

#测试：打印20个预测值和真实值的对
test_output=sess.run(logits,{input_x:test_x[:20]})
inferenced_y=np.argmax(test_output,1)
print(inferenced_y,'Inferenced numbers')#推测的数字
print(np.argmax(test_y[:20],1),'Real numbers')