import copy
import functools
import time

import numpy as np
import random as rand
import math
import matplotlib.pyplot as plt

s = [173669, 275487, 1197613, 1549805, 502334, 217684, 1796841, 274708,
631252, 148665, 150254, 4784408, 344759, 440109, 4198037, 329673, 28602,
144173, 1461469, 187895, 369313, 959307, 1482335, 2772513, 1313997, 254845,
486167, 2667146, 264004, 297223, 94694, 1757457, 576203, 8577828, 498382,
8478177, 123575, 4062389, 3001419, 196884, 617991, 421056, 3017627, 131936,
1152730, 2676649, 656678, 4519834, 201919, 56080, 2142553, 326263, 8172117,
2304253, 4761871, 205387, 6148422, 414559, 2893305, 2158562, 465972, 304078,
1841018, 1915571]

def fitness(x):
    F = 2 ** 26 - np.sum(np.array(x) * np.array(s))
    if F < 0:
        F = 2 ** 26

    return F
def compare(item1, item2):
    if fitness(item1) < fitness(item2):
        return -1
    elif fitness(item1) > fitness(item2):
        return 1
    else:
        return 0

final_x = []
final_opt = 0
min = np.inf
def genetic_algorithm(s, absolute_min):
    global final_x
    global min
    global final_opt
    min = np.inf
    cummulative_min = np.inf
    cummulative_matrix_row = []
    opt_matrix_row = []
    crossover_probability_threshold = 0.7
    mutation_probability_threshold = 0.15
    max_generations = 50
    population = []
    population_fitness = []

    for i in range(2000):
        individual = []
        for j in range(64):
            individual.append(rand.randrange(2))
        population.append(individual)
        population_fitness.append(fitness(individual))

    for i in range(max_generations):
        population_fitness, population = zip(*sorted(zip(population_fitness, population)))
        current_optimal = population_fitness[0]

        if current_optimal < absolute_min:
            absolute_min = current_optimal
            final_x = copy.deepcopy(population[0])

        selected_individuals = list(population[0:400])
        population_fitness = list(population_fitness[0:400])
        #print(selected_individuals)

        while len(selected_individuals) < 2000:
            first_parent_index = rand.randrange(0, 400)
            second_parent_index = rand.randrange(0, 400)
            while second_parent_index == first_parent_index:
                second_parent_index = rand.randrange(0, 400)

            if crossover_probability_threshold > rand.uniform(0,1):
                continue

            crossover = rand.randrange(1, 64)

            new_individual = selected_individuals[first_parent_index][0:crossover] + \
                              selected_individuals[second_parent_index][crossover:64]

            selected_individuals.insert(0,new_individual)
            #print(new_individual)
            population_fitness.insert(0,0)


        for individual_index in range(len(selected_individuals)):
            selected_individual = selected_individuals[individual_index]
            index = rand.randrange(0,64)
            #for index in range(len(selected_individual)):
            if rand.uniform(0,1) < mutation_probability_threshold:
                selected_individual[index] = 1 - selected_individual[index]

            population_fitness[individual_index] = fitness(selected_individual)

        for j in range(2000):
            if population_fitness[j] < min:
                min = population_fitness[j]
            cummulative_matrix_row.append(min)
        population = selected_individuals
    return cummulative_matrix_row, opt_matrix_row, cummulative_min, absolute_min


cummulative_min = np.inf
absolute_min = np.inf
cummulative_matrix = []
opt_matrix = []
x = np.arange(0,100000, 1)

starting_time = time.time()



for i in range(20):
    [cummulative_matrix_row, opt_matrix_row, cummulative_min, absolute_min] =genetic_algorithm(s, absolute_min)
    cummulative_matrix.append(cummulative_matrix_row)
    opt_matrix.append(opt_matrix_row)

    print("Iteration #" + str(i+1) + " -> Current Min = " + str(absolute_min))
    plt.plot(x, cummulative_matrix[i], label='it'+str(i))


print("Final x: "+str(final_x))
print("Final fitness value: "+str(absolute_min))
print("Execution time: "+str(time.time()-starting_time))

plt.legend()
plt.yscale('log')
plt.xscale('log')

average_array = np.sum(cummulative_matrix, axis=0) / len(cummulative_matrix)
plt.figure(2)

plt.plot(x, average_array)

plt.yscale('log')
plt.xscale('log')

plt.show()