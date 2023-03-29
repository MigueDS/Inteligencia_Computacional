
Ejercicio 2
```python
######################################################################
#
#   Autor: Miguel Domínguez
#   Subject: Intelligence Computing
#   Date: 29/03/2023
#
#   Title: Solution to question 2 
#   Question 2: With the current parent selection mechanism, 
#   could both parents be the same individual? If so, 
#   how could we modify select_parents to avoid that behaviour?
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
def select_parents(population, fitnesses):
    total_fitness = sum(fitnesses)
    if (total_fitness != 0):
      probabilities = [fitness / total_fitness for fitness in fitnesses]
    else:
      probabilities = [1 / len(population) for individual in population]
    parents = []
    fp = -1          #ID of the first parent
    for i in range(2): #Select 2 parents
        selected = False
        while not selected:
            rand = random.uniform(0, 1)
            accum = 0
            for j in range(len(population)):
                accum += probabilities[j]
                if rand < accum:
                    if j != fp: #Check is not the first parent
                        parents.append(population[j])
                        fp = j #Take the first parent
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
        fitnesses = [fitness(solution) for solution in population]
        children_population = []
        while (len(children_population) < population_size):
          parents = select_parents(population, fitnesses)
          children = crossover(parents)
          children_population.extend([mutate(child) for child in children])
        population = children_population
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
```

