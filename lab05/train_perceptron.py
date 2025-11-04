import numpy as np
import random

class Perceptron():
    def __init__(self ,inputs_num, weights , bias , learning_rate  ,epochs):
        self.weights = np.zeros(inputs_num)
        self.bais = 0 
        self.epochs = epochs
        self.learning_rate = learning_rate
     
    def step(self , x):
        return 1 if x >= 0 else 0
    
    def predict(self , x):
        result = np.dot(x , self.weights) + self.bais
        return self.step(result)
    
    def train(self , X ,y):
        for _  in range(self.epochs):
            for i , x in enumerate(X):
                y_hat = self.predict(x)
                self.weights += self.learning_rate * (y[i] - y_hat) * x
                self.bais += self.learning_rate * (y[i] - y_hat)


X = [ [x,y] for x in range(2)  for y in range(2)]
X = np.array(X)

y = [x[0] and x[1] for x in X]
y = np.array(y)

perceptron = Perceptron(inputs_num=2 , weights=None , bias=None , learning_rate=1 , epochs=10)
perceptron.train(X , y)

print(perceptron.weights, perceptron.bais)

for i , x in enumerate(X):
    print(perceptron.predict(x) , "expected: " , y[i])
    


