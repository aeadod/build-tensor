import  tensorflow  as  tf
state=tf.Variable(10, name = "counter" )#定义一个变量初始化为1
print(type(state))

one=tf.constant(1)#定义一个常量，值1
print(type(one))

new_value=tf.add(state,one) #实现加法
print(type(new_value))

update=tf.assign(state,new_value) # state=new_value
print(type(update))
init=tf.global_variables_initializer()#初始化全局变量方法


def main(_): #tenforflow是个框架，python控制执行 ，_代表参数
    with  tf.Session() as sess:  #会话过程
        sess.run(init) #初始化
        print(sess.run(state)) #打印状态
        print(sess.run(one)) #打印状态
        print(sess.run(new_value)) #打印状态
        
        for  i  in range(3):
            sess.run(update)
            print("********",sess.run(state))
       
if __name__ == "__main__":
    tf.app.run() #执行过程
