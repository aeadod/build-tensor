import numpy
import scipy.special
import matplotlib.pyplot


class neuralnetwork:
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes=inputnodes
        self.hnodes=hiddennodes
        self.onodes=outputnodes
        self.lr=learningrate
        #self.wih=(numpy.random.rand(self.hnodes,self.inodes)-0.5)
        #self.who=(numpy.random.rand(self.onodes,self.hnodes)-0.5)
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        self.activation_function=lambda x:scipy.special.expit(x)
        pass
    def train(self,inputs_list,targets_list):
        inputs=numpy.array(inputs_list,ndmin=2).T
        targets=numpy.array(targets_list,ndmin=2).T
        hidden_inputs=numpy.dot(self.wih,inputs)
        hidden_outputs=self.activation_function(hidden_inputs)
        final_inputs=numpy.dot(self.who,hidden_outputs)
        final_outputs=self.activation_function(final_inputs)

        output_errors=targets - final_outputs

        hidden_errors=numpy.dot(self.who.T,output_errors)

        self.who+=self.lr*numpy.dot((output_errors*final_outputs*(1.0-final_outputs)),numpy.transpose(hidden_outputs))

        self.wih+=self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),numpy.transpose(inputs))
        pass
    def query(self,input_list):
        inputs=numpy.array(input_list,ndmin=2).T
        hidden_inputs=numpy.dot(self.wih,inputs)
        hidden_outputs=self.activation_function(hidden_inputs)
        final_inputs=numpy.dot(self.who,hidden_outputs)
        final_outputs=self.activation_function(final_inputs)
        return final_outputs


input_nodes=784
hidden_nodes=200
output_nodes=10
learning_rate=0.1
n=neuralnetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

training_data_file=open("C:/Users/aeado/Desktop/mnist_dataset/mnist_train_100.csv",'r')
training_data_list=training_data_file.readlines()
training_data_file.close()

#onodes=10
#targets=numpy.zeros(onodes)+0.01
#targets[int(all_values[0])]=0.99
#print(targets)

#shidai
epochs=7
for e in range(epochs):
    for record in training_data_list:
        all_values=record.split(',')
        inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass
#for record in training_data_list:
#   all_values = record.split(',')
#    inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01
#    targets=numpy.zeros(output_nodes)+0.01
#    targets[int(all_values[0])]=0.99
#    n.train(inputs,targets)
#    pass


test_data_file=open("C:/Users/aeado/Desktop/mnist_dataset/mnist_test_10.csv",'r')
test_data_list=test_data_file.readlines()
test_data_file.close()

all_values=test_data_list[0].split(',')
print(all_values[0])

image_array=numpy.asfarray(all_values[1:]).reshape((28,28))
matplotlib.pyplot.imshow(image_array,cmap='Greys',interpolation='None')

n.query((numpy.asfarray(all_values[1:])/255.0*0.99)+0.01)

scorecard=[]
for record in test_data_list:
    all_values=record.split(',')
    correct_label=int(all_values[0])
    print(correct_label,'correct_label')
    inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01
    outputs=n.query(inputs)
    label =numpy.argmax(outputs)
    print(label,'network answer')
    if (label==correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass
    pass

print(scorecard)
scorecard_array=numpy.asanyarray(scorecard)
print('performance=',scorecard_array.sum()/scorecard_array.size)
