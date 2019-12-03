# Dependencies
import numpy as np
import matplotlib.pyplot as plt 
import scipy
from scipy import optimize

# SciPy Gradient Optimizer
def gradient_optimizer(f, x0, eps=.0001, t = .01, num_iter=1000000):
    for i in range(num_iter):
        grad = optimize.approx_fprime(x0, f, eps)
        if all(z < eps for z in grad):
            x0 = x0 - t * grad
            return x0 
        else:
            x0 = x0 - t * grad
            grad = optimize.approx_fprime(x0, f, eps)
            
# Class
class Cross_Entropy:
    '''The Cross Entropy Class'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.beta = np.zeros((x.shape[1], 1))
    
    def sigmoid(self):
        '''The Sigmoid form for the log likelihood function''' 
        return 1 / (1 + np.exp(np.dot(-self.x, self.beta)))
    
    def reg(self):
        '''The Log Likelihood Function'''
        return -sum(y * np.log(self.sigmoid()) + (1 - y) * np.log(1 - self.sigmoid()))
    
    def fit_approx(self):
        '''Make an approximate fit using gradient optimizer'''
#         %run gradient_optimizer.py
        fitted_approx = gradient_optimizer(self.reg(), self.beta)   
        return fitted_approx, x

    def fit(self, x, y, t = 0.01, num_epochs = 1000):
        '''The actual cross gradient provided by Javi'''
        beta_2 = np.zeros((x.shape[1], 1))
        for i in num_epochs:
            p = self.sigmoid(x, beta_2)
            grad = x.T(y - p)
            beta_2 = beta_2 - t * grad

