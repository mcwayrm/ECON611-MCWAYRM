
## My First Attempt. 2 Demensional
# import numpy as np 
# x = np.array([1,2])
# def f(x):
#     return x ** 2
# def gradient_optimizer(f, x0 = np.array([1, 2]), eps = .0001, t = .01, num_iter = 1000):
#     iters = 1
#     past_step_size = 1
#     while t > eps and iters < num_iter:
#         # Initial Values
#         # Restart Iteration
#         prev_x = x0 
#         def gradient(f=f, x0=x0, eps=eps):
#             fprime = (f(x0 + eps) - f(x0))/eps
#             return fprime
#         # Gradient Descent
#         x0 = x0 - t * gradient()
#         # Reapproximate measurement
#         previous_step_size = abs(x0 - prev_x)
#         # Iterate again
#         iters = iters + 1
#         # Update Report
# #         print("Iteration ",iters,"\nX value is ",x0)
#     print('Gradient optimized at ', x0)
#     return x0 
# gradient_optimizer(f, 3)




## Second Attempt. K Demensionals
def f(y):
    return y ** 2
def gradient(f, x0):
    '''Calculate derivations of each element in x, store gradient'''
    grad = []
    for current_x in x0:
        xplus_eps = current_x + eps
        xminus_eps = current_x - eps
        derv = (f(xplus_eps) - f(xminus_eps))/(2 * eps)
        grad.append(derv)
    return grad
def gradient_optimizer(f, x, eps = 0.0001, t = 0.01, num_iter = 1000):
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
    
Xs = [1,2,3,4]
optimized_coordinate = gradient_optimizer(f, Xs)
print(optimized_coordinate)

# For Principle Components. Probably not going to do this one.
def plot(xs):
    return ""
    
    

class data_manager():
    def __init__():
        
        
        
    def describe():