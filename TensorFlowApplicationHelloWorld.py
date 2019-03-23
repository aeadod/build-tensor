import numpy as np  #numpy基础上构建tensorflow
import sys  #sys系统
import os  #执行系统功能
import tensorflow as tf  #别名tf

def main(_): #tenforflow是个框架，python控制执行 ，_代表参数
    with tf.Session() as sess: #创建一个会话过程
        welcome1 = sess.run(tf.constant("Hello, TensorFlow!"))
        welcome2 = sess.run(tf.constant("Hello, baby!"))
        print(welcome1)
        print(welcome2)
 
if __name__ == "__main__":
    tf.app.run()
