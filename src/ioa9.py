import random

import numpy as np

R = 15
N = 20

def euclidean_norm(x):
    return np.math.sqrt(np.sum(np.power(x, 2)))

def point_distance(P1, P2):
    return np.math.sqrt(np.power(P1[0]-P2[0], 2) + np.power(P1[1]-P2[1], 2))

def get_x(i):
    return R * np.cos(2 * np.pi * i/20)

def get_y(i):
    return R * np.sin(2 * np.pi * i/20)

def select_3_random(selection_arr, i):
    found_num = 0
    while True:
        found = True
        selection_arr[found_num] = int(random.randrange(0, 50))
        for j in range(found_num):
            if selection_arr[j] == selection_arr[found_num]:
                found = False

        if selection_arr[found_num] == i:
            found = False
        if found:
            found_num += 1
        if found_num == 3:
            break

def optimization_function(s, P1, P2, A1, A2):
    if euclidean_norm(P1) < R and euclidean_norm(P2) < R:
        sum = 0
        for i in range(20):
            P = []
            P.append(get_x(i))
            P.append(get_y(i))
            sum += np.power((1.0*A1) / point_distance(P, P1) + (1.0*A2) / point_distance(P, P2) - s[i], 2)
        return sum
    return 100


def differential_evolution(s):
    F = 0.8
    CR = 0.9
    population_size = 50
    var_num = 6
    x = np.zeros((population_size, var_num))
    z = np.zeros((population_size, var_num))
    y = np.zeros((population_size, var_num))
    selection_arr = np.zeros(3)
    min_opt = np.inf
    # Random initialization
    for i in range(population_size):
        for j in range(var_num):
            x[i][j] = int(random.randrange(-15, 16))
    while True:

        # Check optimization function
        for i in range(population_size):
            opt = optimization_function(s, x[i][0:2], x[i][2:4], x[i][4], x[i][5])
            if opt < min_opt:
                min_opt = opt
                print("Min optimization function value: "+str(min_opt))
            if opt < pow(10, -14):
                return x[i]

        for i in range(population_size):
            # Mid
            select_3_random(selection_arr, i)
            z[i] = x[int(selection_arr[0])] + F * (x[int(selection_arr[1])] - x[int(selection_arr[2])])
            # Cross
            r = random.randrange(0, var_num)
            for j in range(var_num):
                if j == r or random.uniform(0, 1) < CR:
                    y[i][j] = z[i][j]
                else:
                    y[i][j] = x[i][j]

            if optimization_function(s, x[i][0:2], x[i][2:4], x[i][4], x[i][5]) > optimization_function(s, y[i][0:2], y[i][2:4], y[i][4], y[i][5]):
                x[i] = y[i]




s = [2.424595205726587e-01, 1.737226395065819e-01, 1.315612759386036e-01,
     1.022985539042393e-01, 7.905975891960761e-02, 5.717509542148174e-02,
     3.155886625106896e-02, -6.242228581847679e-03, -6.565183775481365e-02,
     -8.482380513926287e-02, -1.828677714588237e-02, 3.632382803076845e-02,
     7.654845872485493e-02, 1.152250132891757e-01, 1.631742367154961e-01,
     2.358469152696193e-01, 3.650430801728451e-01, 5.816044173713664e-01,
     5.827732223753571e-01, 3.686942505423780e-01]

print("Solution: "+str(differential_evolution(s)))