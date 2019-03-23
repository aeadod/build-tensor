import tensorflow as tf
c=tf.constant([[2,3],[4,5]],name='const1',dtype=tf.int64)
sess=tf.Session()

print(sess.run(c))
sess.close()
if c.graph is tf.get_default_graph():
    print(666)


#kaishi
const1=tf.constant([[1,2]])
const2=tf.constant([[4],
                    [3]])

multiple=tf.matmul(const1,const2)

sess1=tf.Session()

print(sess1.run(multiple))

if const1.graph is tf.get_default_graph:
    print(7777)


with tf.Session() as sess2:
    result2=sess1.run(multiple)
    print("789")