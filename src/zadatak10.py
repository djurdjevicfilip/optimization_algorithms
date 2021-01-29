import numpy as np
import random as rand
import math as m

def cost(x):
    a = [1,5,1] 
    b = [3,2,0]
    c = [5,7,1]
    d = [6,3,3]
    
    suma = m.sqrt(pow(a[0] - x[0],2) + pow(a[1] - x[1],2) + pow(a[2] - x[2],2)) + m.sqrt(pow(b[0] - x[0],2) + pow(b[1] - x[1],2) + pow(b[2] - x[2],2)) + m.sqrt(pow(c[0] - x[3],2) + pow(c[1] - x[4],2) + pow(c[2] - x[5],2)) + m.sqrt(pow(d[0] - x[3],2) + pow(d[1] - x[4],2) + pow(d[2] - x[5],2)) + m.sqrt(pow(x[0] - x[3],2) + pow(x[1] - x[4],2) + pow(x[2] - x[5],2))
    return suma

def main():
    w = 0.729
    c1 = c2 = 1.494
    wmax = 0.2
    a = [1,5,1] 
    b = [3,2,0]
    c = [5,7,1]
    d = [6,3,3]
    flag = True
    x = np.zeros((100,6))
    v = np.zeros((100,6))
    brzina_trenutna = np.zeros((1,6))
    pbest = np.zeros((100,6))
    gbest = np.zeros((1,6))
    promena = np.zeros((1,6))
    for i in range(100):
        for j in range(6):
            x[i][j] = rand.uniform(0,5)
            v[i][j] = rand.uniform(0,0.2)
    brojac = 0
    while 1 == 1:
        
        print(brojac)
        if flag == True:
            print(flag)
            for i in range(100):
                pbest[i] = x[i]
            flag = False
            promena = x[0]
            for i in range(100):
                if cost(promena) > cost(x[i]):
                    promena = x[i]
                
            gbest = promena
        
        for i in range(100):
            brzina_trenutna = w*v[i] + c1*rand.uniform(0,1)*(pbest[i] - x[i]) + c2*rand.uniform(0,1)*(gbest - x[i])
            for j in range(6):
                if brzina_trenutna[j] > 0.2:
                    brzina_trenutna[j] = 0.2
            promena = x[i] + brzina_trenutna
            v[i] = brzina_trenutna
            if cost(promena) < cost(pbest[i]):
                pbest[i] = promena
            if cost(promena) < cost(gbest):
                gbest = promena
            x[i] = promena
        if cost(gbest) < 11.30:
            break
        
        brojac = brojac + 1
        
        
        
    print(gbest)
    print(cost(gbest))
    
    

    
    
    
if __name__ == '__main__':
    main()