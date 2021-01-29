import random as rand

# Parameters
crossover_probability_threshold = 0.7
mutation_probability_threshold = 0.15
max_generations = 50
population_size = 2000
individual_size = 64
select_pool_size = 400

# Fitness function
def fitness(individual):
    return 1

# Initialization
def init_genetic(population, population_fitness):
    for i in range(population_size):
        individual = []
        for j in range(individual_size):
            individual.append(rand.randrange(2))
        population.append(individual)
        population_fitness.append(fitness(individual))

# Sort
def sort_population(population, population_fitness):
    return zip(*sorted(zip(population_fitness, population)))

# Selection phase
def select_individuals_phase(population, population_fitness, size):
    return list(population[:size]), list(population_fitness[:size])

# Crossover phase
def select_parent_indices():
    first_parent_index = rand.randrange(0, individual_size)
    second_parent_index = rand.randrange(0, individual_size)
    while second_parent_index == first_parent_index:
        second_parent_index = rand.randrange(0, individual_size)

    return first_parent_index, second_parent_index

def crossover(population, fpi, spi):
    crossover_index = rand.randrange(0, individual_size)
    return population[fpi][0:crossover_index] + population[spi][crossover_index: individual_size]

def crossover_phase(population, population_fitness):
    while(len(population) < population_size):
        # Select 2 indices
        [first_parent_index, second_parent_index] = select_parent_indices()

        # Skip probability
        if crossover_probability_threshold > rand.uniform(1):
            continue

        new_individual = crossover(population, first_parent_index, second_parent_index)

        population.insert(0, new_individual)
        population_fitness.insert(0, 0)

    return population, population_fitness


# Mutation phase

def mutation_phase(population, population_fitness):
    for i in range(len(population)):
        individual = population[i]
        index = rand.randrange(0, individual_size)
        if (rand.uniform(0, 1) < mutation_probability_threshold):
            individual[index] = 1 - individual[index]

        population_fitness[i] = fitness(individual)

    return population, population_fitness

# Genetic algorithm
def genetic_algorithm(s):
    population = []
    population_fitness = []
    selected_population = []

    # Initialize
    init_genetic(population, population_fitness)

    for i in range(max_generations):

        # Sort population
        [population_fitness, population] = sort_population(population, population_fitness)

        # Select individuals
        [selected_population, population_fitness] = select_individuals_phase(population, population_fitness, select_pool_size)

        # Crossover
        [selected_population, population_fitness] = crossover_phase(selected_population, population_fitness)

        # Mutation
        [selected_population, population_fitness] = mutation_phase(selected_population, population_fitness)

        population = selected_population