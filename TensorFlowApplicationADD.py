import tensorflow as tf

mx1=tf.constant([[3.0,3.0]]) #1*2的二维数组
mx2=tf.constant([[2.0],[2.0]])#2*1的二维数组
product=tf.matmul(mx1,mx2) #乘法 

def main(_): #tenforflow是个框架，python控制执行 ，_代表参数
    with  tf.Session() as sess:  #会话过程
        result= sess.run(product) #执行
        print(result)

if __name__ == "__main__":
    tf.app.run() #执行过程


