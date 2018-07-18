import numpy as np

class NeuralNet:
    def __init__(self,sizes):
        self.numLayers = len(sizes)
        self.sizes = sizes
        self.weights = [np.random.randn(i,j) for i,j in zip(sizes[:-1],sizes[1:])]

    def sigmoid(self,x):
        return 1.0/(1.0+np.exp(-x))

    def sigmoid_prime(self,x):
        return x*(1-x)
        
    def Run(self, data, answer):
        #Feed Forward
        layers = []
        layers.append(data)
        for l in range(self.numLayers-1):
            layers.append(self.sigmoid(np.dot(layers[l],self.weights[l])))
            
        out_error = answer - layers[-1]
        out_delta = out_error * self.sigmoid_prime(layers[-1])

        errors = []
        deltas = []
        errors.append(out_error)
        deltas.append(out_delta)
        for l in range(self.numLayers-2,0,-1):
            err = deltas[len(errors)-1].dot(self.weights[l].T)
            delt = err * self.sigmoid_prime(layers[l])
            errors.append(err)
            deltas.append(delt)
        
        for l in range(self.numLayers-1):
            self.weights[self.numLayers-2-l] += layers[self.numLayers-2-l].T.dot(deltas[l])

        return np.mean(np.abs(out_error))