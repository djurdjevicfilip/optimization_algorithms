import random as rand
import numpy as np
# Parameters
from scipy.ndimage import shift

crossover_probability_threshold = 0.7
mutation_probability_threshold = 0.15
max_generations = 50
population_size = 2000
individual_size = 31
select_pool_size = 400


def cross_correlation(X, X0):
    same = 0
    different = 0
    for i in range(len(X)):
        first = X[i]
        second = X0[i]

        if(first == second):
            same += 1
        else:
            different += 1

    return same, different

def shifted_cross_correlation(X, X0, start):
    same_cnt = 0
    different_cnt = 0

    for i in range(start, 30):
        # Shift
        same, different = cross_correlation(X,X0[i:]+X0[:i])
        same_cnt += same
        different_cnt += different
    return same_cnt - different_cnt

# Fitness function
def fitness(individual, X0):
    cross_correlation_sum = 0
    auto_correlation_sum = 0
    correlation = shifted_cross_correlation(individual, X0, 0)
    if not (-4 < correlation < 6):
        if correlation >= 6:
            cross_correlation_sum += correlation - 5
        else:
            cross_correlation_sum += -3 - correlation

    # Autocorrelation
    correlation = shifted_cross_correlation(individual, individual, 1)
    if not (-18 < correlation < 12):
        if correlation >= 12:
            auto_correlation_sum += correlation - 11
        else:
            auto_correlation_sum += -17 - correlation

    add = 0
    return cross_correlation_sum + auto_correlation_sum + add


# Initialization
def init_genetic(population, population_fitness, X0):
    for i in range(population_size):
        individual = []
        for j in range(individual_size):
            individual.append(rand.randrange(2))
        population.append(individual)
        population_fitness.append(fitness(individual, X0))
    return population, population_fitness

# Sort
def sort_population(population, population_fitness):
    return zip(*sorted(zip(population_fitness, population)))


# Selection phase
def select_individuals_phase(population, population_fitness, size):
    return list(population[:size]).copy(), list(population_fitness[:size]).copy()


# Crossover phase
def select_parent_indices():
    first_parent_index = rand.randrange(0, select_pool_size)
    second_parent_index = rand.randrange(0, select_pool_size)
    while second_parent_index == first_parent_index:
        second_parent_index = rand.randrange(0, select_pool_size)

    return first_parent_index, second_parent_index


def crossover(population, fpi, spi):
    crossover_index = rand.randrange(0, individual_size)
    return population[fpi][0:crossover_index] + population[spi][crossover_index: individual_size]


def crossover_phase(population, population_fitness, X0):
    while (len(population) < population_size):
        # Select 2 indices
        first_parent_index, second_parent_index = select_parent_indices()

        # Skip probability
        if crossover_probability_threshold > rand.uniform(0, 1):
            continue

        new_individual = crossover(population, first_parent_index, second_parent_index)

        population.append(new_individual)
        population_fitness.append(0)

    return population, population_fitness


# Mutation phase

def mutation_phase(population, population_fitness, X0):
    for i in range(len(population)):
        individual = population[i]
        index = rand.randrange(0, individual_size)
        if (rand.uniform(0, 1) < mutation_probability_threshold):
            individual[index] = 1 - individual[index]

        population_fitness[i] = fitness(individual, X0)

    return population, population_fitness


# Genetic algorithm
def genetic_algorithm(s):
    population = []
    population_fitness = []
    selected_population = []

    # Initialize
    population, population_fitness = init_genetic(population, population_fitness, s)

    for i in range(max_generations):
        # Sort population
        population_fitness, population = zip(*sorted(zip(population_fitness, population)))
        print(population[0])
        # Select individuals
        selected_population, population_fitness = select_individuals_phase(population, population_fitness, select_pool_size)
        # Crossover
        selected_population, population_fitness = crossover_phase(selected_population, population_fitness, s)

        # Mutation
        selected_population, population_fitness = mutation_phase(selected_population, population_fitness, s)

        population = selected_population
    return population[0]
x = [0,0,0,0, 0,0,0,1, 0,0,0,1, 1,0,1,1, 0,0,0,0, 1,1,0,0, 1,1,1,0, 0,1,1]
print(fitness( [0,0,0,1, 1,1,0,1, 0,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,0,1, 0,1,0,1, 1,0,1], x))


sol = genetic_algorithm(x)



