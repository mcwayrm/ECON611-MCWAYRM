     
def gradient_optimizer(f, x, eps = 0.0001, t = 0.01, num_iter = 1000):
    def gradient(f, x0):
    '''Calculate derivations of each element in x, store gradient'''
    grad = []
    for current_x in x0:
        xplus_eps = current_x + eps
        xminus_eps = current_x - eps
        derv = (f(xplus_eps) - f(xminus_eps))/(2 * eps)
        grad.append(derv)
    return grad
    '''Gradient Optimizer over numerous iterations'''
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