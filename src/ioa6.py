from math import sqrt

from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def getYout(x, w):
    tmp = 0
    for k in range(0, 5):
        tmp += w[k+5] * np.tanh(w[k]*x)
    return np.tanh(tmp)

def getYtr(x):
    return (1/2.0)*np.sin(np.pi*x)

def optimizationFunction(w):
    tmp=0
    for xin in np.arange(-1.0, 1.1, 0.1):
        tmp += pow(getYout(xin, w) - getYtr(xin),2 )
    tmp = sqrt(tmp)
    # penalty
    for ww in w:
        if ww > 10 or ww < -10:
            tmp+=10
    return tmp

w=np.linspace(2,10,10)
fun = 1

optPenalty = 100

print("Initial values: "+str(w))

while fun>=pow(10,-2):
    resComplete = optimize.minimize(x0=w, method='nelder-mead', fun=optimizationFunction)
    w = resComplete.x
    fun = resComplete.fun
print("Final values: "+str(w))
print("Optimization function value: "+str(fun))

X = np.arange(-1,1,0.001)

finalYout = []
finalYtr = []

for i in X:
    finalYtr.append(getYtr(i))

plt.plot(X,finalYtr, label='Y training')

X = np.arange(-1,1.05,0.05)
for i in X:
    finalYout.append(getYout(i, w))

plt.plot(X, finalYout, 'rx', label='Y out')
plt.legend()
plt.show()
