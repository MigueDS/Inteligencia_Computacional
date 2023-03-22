######################################################################
#
#   Autor: Miguel Domínguez
#   Subject: Intelligence Computing
#   Date: 22/03/2023
#
#   Title: First Example
#
######################################################################


import random

# define the initialisation function
def initialize_population():
    population = []
    for i in range(population_size):
        solution = [random.choice([True, False]) for i in range(len(weights))]
        population.append(solution)
    return population

    # define the fitness function
def fitness(solution):
    total_weight = sum(weights[i] for i in range(len(weights)) if solution[i])
    if total_weight > max_weight:
        return 0
    return sum(values[i] for i in range(len(values)) if solution[i])

# define the parent selection function
def select_parents(population):
    fitnesses = [fitness(solution) for solution in population]
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    parents = []
    for i in range(2): #Select to parents   
        selected = False
        while not selected:
            for j in range(len(population)):
                if random.random() < probabilities[j]:
                    parents.append(population[j])
                    selected = True
                    break
    return parents

# define the crossover function
def crossover(parents):
    crossover_point = random.randint(1, len(weights) - 1)
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
    return [child1, child2]

# define the mutation function
def mutate(solution):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = not solution[i]
    return solution

# define the genetic algorithm
def genetic_algorithm():
    population = initialize_population()
    for i in range(num_generations):
        parents = select_parents(population)
        children = crossover(parents)
        population = [mutate(child) for child in children]
    fitnesses = [fitness(solution) for solution in population]
    best_fitness = max(fitnesses)
    best_solution = population[fitnesses.index(best_fitness)]
    best_weight = sum(weights[i] for i in range(len(weights)) if best_solution[i])
    return (best_solution, best_fitness, best_weight)

# define the problem instance
weights = [10, 20, 30, 40, 50]
values = [100, 50, 150, 200, 300]
max_weight = 100

# define genetic algorithm parameters
population_size = 50
num_generations = 100
mutation_rate = 0.01

# run the genetic algorithm and print the result
best_solution, best_fitness, best_weight = genetic_algorithm()
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
print("Best weight:", best_weight)