import math
import random


class NN:
    """
    Back-Propagation Neural Networks
    Inspired by Neil Schemenauer <nas@arctrix.com>
    
    Papers:
    A New Approach to Content-based File Type Detection, Mehdi Chehel Amirani
    """
    # calculate a random number where:  a <= rand < b
    def rand(self, a, b):
        random.seed(0)
        return (b-a)*random.random() + a
    
    # Make a matrix (we could use NumPy to speed this up)
    def makeMatrix(self, I, J, fill=0.0):
        m = []
        for i in range(I):
            m.append([fill]*J)
        return m
    
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.input_nodes = ni + 1 # +1 for bias node
        self.hidden_nodes = nh
        self.output_nodes = no

        # activations for nodes
        self.input_activation = [1.0] * self.input_nodes
        self.hidden_activation = [1.0] * self.hidden_nodes
        self.output_activation = [1.0] * self.output_nodes

        # create weights
        self.wi = self.makeMatrix(self.input_nodes, self.hidden_nodes)
        self.wo = self.makeMatrix(self.hidden_nodes, self.output_nodes)
        # set them to random vaules
        for i in range(self.input_nodes):
            for j in range(self.hidden_nodes):
                self.wi[i][j] = self.rand(-0.2, 0.2)
        for j in range(self.hidden_nodes):
            for k in range(self.output_nodes):
                self.wo[j][k] = self.rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = self.makeMatrix(self.input_nodes, self.hidden_nodes)
        self.co = self.makeMatrix(self.hidden_nodes, self.output_nodes)
    
    # our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
    def sigmoid(self, x):
        return math.tanh(x)
    
    # derivative of our sigmoid function, in terms of the output (i.e. y)
    def dsigmoid(self, y):
        return 1.0 - y**2

    def update(self, inputs):
        if len(inputs) != self.input_nodes - 1:
            raise ValueError, 'wrong number of inputs'

        # input activations
        for i in range(self.input_nodes - 1):
            #self.input_activation[i] = sigmoid(inputs[i])
            self.input_activation[i] = inputs[i]

        # hidden activations
        for j in range(self.hidden_nodes):
            summ = 0.0
            for i in range(self.input_nodes):
                summ = summ + self.input_activation[i] * self.wi[i][j]
            self.hidden_activation[j] = self.sigmoid(summ)

        # output activations
        for k in range(self.output_nodes):
            summ = 0.0
            for j in range(self.hidden_nodes):
                summ = summ + self.hidden_activation[j] * self.wo[j][k]
            self.output_activation[k] = self.sigmoid(summ)

        return self.output_activation[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.output_nodes:
            raise ValueError, 'wrong number of target values'

        # calculate error terms for output
        output_deltas = [0.0] * self.output_nodes
        for k in range(self.output_nodes):
            error = targets[k] - self.output_activation[k]
            output_deltas[k] = self.dsigmoid(self.output_activation[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.hidden_nodes
        for j in range(self.hidden_nodes):
            error = 0.0
            for k in range(self.output_nodes):
                error = error + output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = self.dsigmoid(self.hidden_activation[j]) * error

        # update output weights
        for j in range(self.hidden_nodes):
            for k in range(self.output_nodes):
                change = output_deltas[k] * self.hidden_activation[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M * self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.input_nodes):
            for j in range(self.hidden_nodes):
                change = hidden_deltas[j] * self.input_activation[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M * self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5 * (targets[k] - self.output_activation[k]) ** 2
        return error


    def test(self, patterns):
        for p in patterns:
            print p[0], '->', self.update(p[0])

    def weights(self):
        print 'Input weights:'
        for i in range(self.input_nodes):
            print self.wi[i]
        print
        print 'Output weights:'
        for j in range(self.hidden_nodes):
            print self.wo[j]

    def train(self, patterns, iterations = 1000, N = 0.5, M = 0.1):
        # N: learning rate
        # M: momentum factor
        for i in xrange(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                pass #print 'error %-14f' % error


def demo():
    # Teach network XOR function
    pat3 = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]
    
    pat = [
           [[ 0.16452143,  0.11296437, 0.1014837 ], [ 0.16452143,  0.11296437, 0.1014837 ]],
           [[ 0.16452143,  0.11296437, 0.1014837 ], [ 0.16452143,  0.11296437, 0.1014837 ]],
           [[ 0.00824927, -0.04947465, -0.03494394], [ 0.00824927, -0.04947465, -0.03494394]]
          ]
    
    # create a network with two input, two hidden, and one output nodes
    n = NN(3, 2, 3)
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat)
    n.weights()



if __name__ == '__main__':
    demo()