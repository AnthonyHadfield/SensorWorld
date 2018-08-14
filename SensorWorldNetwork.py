from decimal import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

"""y_ is the appended list of J values as we step through the train method and decrease the Error """
y_ = []
# """X_ is the list of epoch numbers relative to y_ item."""
X_ = []


class SWNetwork:

    def __init__(self):
        self.target = []
        self.data = []
        self.targetN  = []
        self.dataN = []
        self.dataW1 = []
        self.dataW2 = []
        self.dataW3 = []
        theta = ()

    def tanh(self, z):
        return np.tanh(z)

    def tanhprime(self, z):
        return 1.0 - np.tanh(z) ** 2

    def data_sets(self):

        self.target = np.array([[2.7], [3.0], [3.3], [3.7], [4.1], [4.5], [5.0], [3.7], [1.0], [3.7], [1.0], [3.3],
                                [2.7], [2.4], [1.0], [3.7], [4.1], [4.5], [5.0]])
        self.data = np.array([[2.7], [3.0], [3.3], [3.7], [4.1], [4.5], [5.0], [3.7], [1.0], [3.7], [1.0], [3.3], [2.7],
                              [2.4], [1.0], [3.7], [4.1], [4.5], [5.0]])
        """Normalize DATA"""
        self.dataN = self.data / np.amax(self.data)
        """Get weights/ W1 = row vector, W2 = square matrix, W3 = column vector"""
        # self.dataW1 = np.random.normal(-0.1, 1.1, (1, 19))
        # self.dataW2 = np.random.normal(-0.1, 1.1, (19, 19))
        # self.dataW3 = np.random.normal(-0.1, 1.1, (19, 1))
        self.dataW1 = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/RobotSensors/W1_update.npy')
        self.dataW2 = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/RobotSensors/W2_update.npy')
        self.dataW3 = np.load('C:/Users/user/PycharmProjects/Reinforcement Learning/RobotSensors/W3_update.npy')

    def train(self):
        total_accuracy = 0
        self.data_sets()
        epoch = 200000
        theta = 0.0098
        b = 1
        for i in range(2, epoch):
            """Forward Network, has ONE input layer, TWO hidden layers, and 
            ONE output layer, comprising of z2 = square matrix, a2 = square matrix, 
            z3 = square matrix, a3 square matrix, z4 = column vector, 
            yHat = column vector"""
            z2 = (np.dot(self.dataN, self.dataW1) + b)
            a2 = self.tanh(z2)
            z3 = (np.dot(a2, self.dataW2) + b)
            a3 = self.tanh(z3)
            z4 = (np.dot(a3, self.dataW3) + b)
            yHat = self.tanh(z4)
            """Loss function J"""
            J = 0.5 * sum((self.dataN - yHat) ** 2)
            X_.append(i)
            y_.append(J)
            """delta4 is column vector resulting from column data"""
            """dJdW3 = a3.T is a transposed square matrix times a column vector delta4"""
            """delta3 is a square matrix, resulting from delta4 a column vector times 
            self.dataW3.T = row vector"""
            """dJdW2 is a square matrix resulting from the multiple of TWO square
                matrices delta3, and a2"""
            """self.dataW2 = square matrix"""
            """delta2 is a square matrix resulting from the multiple of TWO square
            matrices delta3, and self.dataW2"""
            """dJdW1 is a column vector resulting from the multiple of delta2 a square matrix
                and self.dataN a column vector"""
            delta4 = np.multiply(-(self.dataN - yHat), self.tanhprime(z4))
            dJdW3 = np.dot(a3.T, delta4)
            delta3 = np.dot(delta4, self.dataW3.T) * self.tanhprime(z3)
            dJdW2 = np.dot(delta3, a2)
            delta2 = np.dot(delta3, self.dataW2)
            dJdW1 =  np.dot(self.dataN.T, delta2)
            """ Backpropagation"""
            """Updating the weights: define next set of weights"""
            W1_grad_applied = np.dot(theta, dJdW1)
            W2_grad_applied = np.dot(theta, dJdW2)
            W3_grad_applied = np.dot(theta, dJdW3)
            self.dataW1 = self.dataW1 - W1_grad_applied
            self.dataW2 = self.dataW2 - W2_grad_applied
            self.dataW3 = self.dataW3 - W3_grad_applied
            print('Epoch : {0}, Error = {1}'.format(i, J))
        for i in range(0, 19):
            accuracy = ((yHat[i] * 5) / self.data[i]) * 100
            print('%0.1f, %0.1f, %0.1f ' % ((self.data[i]), yHat[i] * 5, accuracy))
            total_accuracy = total_accuracy + accuracy
            ave_accuracy = total_accuracy/19
        print('Ave Accuracy =', ave_accuracy)

data = SWNetwork()
# data.data_sets()
data.train()

plt.scatter(X_[3000 :], y_[3000 :], s=25, c="blue")
plt.xlabel('Epochs # training cycles')
plt.ylabel('Error (Cost function J')
plt.show()
