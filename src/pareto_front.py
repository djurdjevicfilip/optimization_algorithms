import random
import matplotlib.pyplot as plt
import numpy as np

def f1(x1, x2):
    return 2*x1**2 + x2**2

def f2(x1, x2):
    return -(x1-x2)**2

def satisfyConstraint(x, y):
    while x*y + 1.0/4.0 <0:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
    return x,y

def fillPoints(points, x ,y):
    point = [f1(x, y), f2(x, y)]
    points.append(point)

def pointNotPareto(point1, point2):
    return point1[0] > point2[0] and point1[1] > point2[1]

def findPareto(points):
    pareto_array = []
    non_pareto_array = []
    for point1 in points:
        pareto = True
        for point2 in points:
            if(pointNotPareto(point1,point2)):
                non_pareto_array.append(point1)
                pareto = False
                break
        if pareto:
            pareto_array.append(point1)
    return pareto_array, non_pareto_array

def drawPareto(pareto_array, non_pareto_array):

    pareto_array = np.array(pareto_array)
    non_pareto_array = np.array(non_pareto_array)
    plt.scatter(non_pareto_array[:,0], non_pareto_array[:,1], marker='o', s=1, c='lightgray')
    plt.scatter(pareto_array[:, 0], pareto_array[:, 1], marker='x', s=1, c='blue')


def pareto():
    ELEMENT_CNT = 10000
    points = []
    points_add = []
    pareto_array = []
    non_pareto_array = []
    for i in range(0, ELEMENT_CNT):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        fillPoints(points, x, y)

        x, y = satisfyConstraint(x, y)

        fillPoints(points_add, x, y)
        
    pareto_array, non_pareto_array = findPareto(points)
    drawPareto(pareto_array, non_pareto_array)

    plt.figure();

    pareto_array, non_pareto_array = findPareto(points_add)
    drawPareto(pareto_array, non_pareto_array)


    plt.show()

pareto()
