import numpy as np

def sample_data():
    numpos = 100
    numneg = 100
    
    mupos = [1.0, 1.0]
    covpos = np.array([[1.0, 0.0], [0.0, 1.0]])
    muneg = [-1.0, -1.0]
    covneg = np.array([[1.0, 0.0], [0.0, 1.0]])
    
    Xpos = np.ones((numpos, 3))
    for i in range(numpos):
        Xpos[i, 0:2] = np.random.multivariate_normal(mupos, covpos)
    Ypos = np.ones((numpos, 1))
        
    Xneg = np.ones((numneg, 3))
    for i in range(numneg):
        Xneg[i, 0:2] = np.random.multivariate_normal(muneg, covneg)
    Yneg = np.zeros((numneg, 1))
    
    X = np.concatenate((Xpos, Xneg))
    Y = np.concatenate((Ypos, Yneg))
    
    return X, Y, Xpos, Xneg

def plotline(beta, Xpos, Xneg):
    xVals = np.linspace(-3, 3, 100) # list of 100 evenly spaced numbers between xMin and xMax
    yVals = (-beta[0] * xVals - beta[2])/beta[1] # a1x + a2y+a3 = 0, so y = (-a1x-a3)/a2
    idxs = np.where((yVals >= -3) & (yVals <= 3))
    plt.scatter(Xpos[:,0],Xpos[:,1])
    plt.scatter(Xneg[:,0],Xneg[:,1])
    plt.plot(xVals[idxs], yVals[idxs])