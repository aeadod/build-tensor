import tensorflow as tf

hw=tf.constant("hello")

sess=tf.Session()

print(sess.run(hw))

sess.close()

const=tf.constant(3)
print(const)
var=tf.Variable(3)
print(var)
var2=tf.Variable(4,dtype=tf.int64)
print(var2)
named_var=tf.Variable([5,6],name='namedok')
print(named_var)