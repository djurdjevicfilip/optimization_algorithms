import numpy as np
import random as rand
import math
import matplotlib.pyplot as plt

def optimization_function(x, s):
    F = 2 ** 26 - np.sum(np.array(x) * np.array(s))
    if F < 0:
        F = 2 ** 26

    return F

final_x = []
final_opt = 0
def simulated_annealing(s, absolute_min):
    global final_x
    global final_opt
    cummulative_min = np.inf
    cummulative_matrix_row = []
    opt_matrix_row = []
    max_iterations = 100000
    h_min = 2
    h_max = 5
    T = 32 * (1024 ** 2)
    modified_x = [0] * 64
    x = [0] * 64
    last_optimization = current_optimization = optimization_function(x, s)

    if(last_optimization != 0):
        for i in range(0, max_iterations):
            hamming_distance = (h_min - h_max) / (max_iterations - 1) * (i - 1) + h_max

            rand_array = rand.sample(range(64), int(hamming_distance))
            for rand_pick in rand_array:
                modified_x[rand_pick] = 1 - modified_x[rand_pick]

            current_optimization = optimization_function(modified_x, s)

            if current_optimization < cummulative_min:
                cummulative_min = current_optimization
            if current_optimization < absolute_min:
                absolute_min = current_optimization
                final_x = modified_x.copy()
                final_opt = current_optimization
            cummulative_matrix_row.append(cummulative_min)
            opt_matrix_row.append(current_optimization)
            if current_optimization < last_optimization:
                x = modified_x.copy()
                last_optimization = current_optimization
            else:

                p = math.exp((last_optimization-current_optimization) / T)
                if last_optimization - current_optimization == 0:
                    p = 0.5
                if rand.uniform(0, 1) > p:
                    x = modified_x.copy()
                    last_optimization = current_optimization


            T *= 0.95

    return cummulative_matrix_row, opt_matrix_row, cummulative_min, absolute_min


s = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
1841018, 1915571]

cummulative_min = np.inf
absolute_min = np.inf
cummulative_matrix = []
opt_matrix = []
x = np.arange(0,100000, 1)
for i in range(20):
    [cummulative_matrix_row, opt_matrix_row, cummulative_min, absolute_min] = simulated_annealing(s, absolute_min)
    cummulative_matrix.append(cummulative_matrix_row)
    opt_matrix.append(opt_matrix_row)

    plt.plot(x, cummulative_matrix[i], label='it'+str(i))


print("Final x: "+str(final_x))
print("Final opt_func_value: "+str(final_opt))

plt.legend()
plt.yscale('log')
plt.xscale('log')

average_array = np.sum(cummulative_matrix, axis=0) / len(cummulative_matrix)
plt.figure(2)

plt.plot(x, average_array)

plt.yscale('log')
plt.xscale('log')

plt.show()