import tensorflow as tf

input1=tf.placeholder(tf.float32) #两个变量，没有初始化，指定类型
input2=tf.placeholder(tf.float32)

output=tf.multiply(input1,input2) #输出

def main(_): #tenforflow是个框架，python控制执行 ，_代表参数
    with  tf.Session() as sess:  #会话过程
        result=sess.run(output,feed_dict={input1:[8.0],input2:[2.0]}) #执行乘法之前先赋值
        print(result)

if __name__ == "__main__":
    tf.app.run() #执行过程
