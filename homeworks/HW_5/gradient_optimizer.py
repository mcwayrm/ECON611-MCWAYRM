class gradient_optimizer:
    def __init__(self, f, x):
        self.f = f
        self.x = x
    
    def gradient(self):
        '''Calculate derivations of each element in x, store gradient'''
        grad = []
        for current_x in self.x:
            xplus_eps = current_x + eps
            xminus_eps = current_x - eps
            derv = (self.f(xplus_eps) - self.f(xminus_eps))/(2 * eps)
            grad.append(derv)
        return grad
    def gradient_optimizer(self, eps = 0.0001, t = 0.01, num_iter = 1000):
        '''Gradient Optimizer over numerous iterations'''
        for i in range(num_iter):
            # Gradient with updated X
            grad = gradient()
            # Check if within acceptable range
            if all(value < eps for value in grad):
                return self.x
            # Scalar Step
            t_into_grad = [t * grads for grads in gradient()]
            # Subtract each gradient from Xs, update X vector
            self.x = [x_old - g for x_old, g in zip(self.x, t_into_grad)]