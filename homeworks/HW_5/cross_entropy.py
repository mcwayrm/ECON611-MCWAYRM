# Dependencies
import numpy as np

# Class
class Cross_Entropy:
    '''The Cross Entropy Class'''
    def __init__(self, x, y):
        self.betas = np.zeros(len(x[0]))
        self.x = np.array(x)
        self.y = np.eye(len(x))
    
    def sigmoid(self):
        '''The Sigmoid form for the log likelihood function'''
        return 1 / (1 + np.exp(-self.x * self.betas))
    
    def regression(self):
        '''The Log Likelihood Function'''
        return -sum((y * np.log(self.sigmoid()) + (1 - y) * np.log(1 - self.sigmoid())))
    
    def fit_approx(self):
        '''Make an approximate fit using gradient optimizer'''
        ## Unsure how to import a py script
        
        '''The gradient optimizer from before'''
        def gradient(f, x0):
        grad = []
        for current_x in x0:
            xplus_eps = current_x + eps
            xminus_eps = current_x - eps
            derv = (f(xplus_eps) - f(xminus_eps))/(2 * eps)
            grad.append(derv)
        return grad
        def gradient_optimizer(f, x, eps = 0.0001, t = 0.01, num_iter = 1000):
        for i in range(num_iter):
            # Gradient with updated X
            grad = gradient(f, x)
            # Check if within acceptable range
            if all(value < eps for value in grad):
                return x
            # Scalar Step
            t_into_grad = [t * grads for grads in gradient(f, x)]
            # Subtract each gradient from Xs, update X vector
            x = [x_old - g for x_old, g in zip(x, t_into_grad)]
        fitted_approx = gradient_optimizer(regression(), self.betas)
        
        return fitted_approx, x

    def fit(self):
        '''The actual cross gradient provided by Javi'''
        # A bit unsure how to implement this one
        beta_2 = zeros
        for i in num_epochs:
            p = sigmoid(self.x, beta_2)
            grad = self.x.T(self.y - p)
            beta_2 = beta_2 - t * grad

